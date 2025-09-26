# NEON AI (TM) SOFTWARE, Software Development Kit & Application Framework
# All trademark and other rights reserved by their respective owners
# Copyright 2008-2025 Neongecko.com Inc.
# Contributors: Daniel McKnight, Guy Daniels, Elon Gasper, Richard Leeds,
# Regina Bloomstine, Casimiro Ferreira, Andrii Pernatii, Kirill Hrymailo
# BSD-3 License
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
import copy
import time
import uuid

import pika
import pika.exceptions

from abc import ABC
from typing import Optional, Dict, Any, Union, Type

from pika.exchange_type import ExchangeType
from ovos_utils.log import LOG

from neon_mq_connector.config import load_neon_mq_config
from neon_mq_connector.consumers import BlockingConsumerThread, SelectConsumerThread

from neon_mq_connector.utils.connection_utils import wait_for_mq_startup, retry
from neon_mq_connector.utils.network_utils import dict_to_b64
from neon_mq_connector.utils.thread_utils import RepeatingTimer

# DO NOT REMOVE ME: Defined for backward compatibility
ConsumerThread = BlockingConsumerThread

ConsumerThreadInstance = Union[BlockingConsumerThread, SelectConsumerThread]

SUPPORTED_THREADED_CONSUMERS = (BlockingConsumerThread,
                                SelectConsumerThread,)


class MQConnector(ABC):
    """
    Abstract class implementing interface for attaching services to MQ server
    """

    __run_retries__ = 5
    __max_consumer_restarts__ = -1
    __consumer_join_timeout__ = 3

    async_consumers_enabled = os.environ.get("MQ_ASYNC_CONSUMERS", True)

    @staticmethod
    def init_config(config: Optional[dict] = None) -> dict:
        """ Initialize config from source data """
        config = config or load_neon_mq_config() or dict()
        config = config.get('MQ') or config
        return config

    def __init__(self, config: Optional[dict], service_name: str):
        """
            :param config: dictionary with current configurations.

            JSON Template of :param config :

            {
                "users": {
                    "<service_name>": {
                        "user": "<username of the service on mq server>",
                        "password": "<password of the service on mq server>"
                    }
                },
                "server": "<MQ Server hostname or IP>",
                "port": <MQ Server Port (default=5672)>,
                "<self.property_key (default='properties')>": {
                    <key of the configurable property>:<value of the configurable property>
                }
            }

            :param service_name: name of current service
       """
        self._config = config
        # Override self.property_key BEFORE base __init__ to initialise
        # properties under customized config location
        if not hasattr(self, 'property_key'):
            self.property_key = 'properties'
        self._service_id = None
        self.service_name = service_name
        self.consumers: Dict[str, ConsumerThreadInstance] = dict()
        self.consumer_properties = dict()
        self._vhost = None
        self._sync_thread = None
        self._observer_thread = None
        self._consumers_started = False

        # Define properties and initialize them
        self.sync_period = 0
        self.observe_period = 0
        self.vhost_prefix = ""
        self.default_testing_prefix = 'test'
        self.testing_envs = set()
        self.testing_prefix_envs = None
        self.__init_configurable_properties()

    @property
    def started(self):
        return self._consumers_started

    @property
    def config(self):
        if not self._config:
            self._config = self.init_config()
        return self._config

    @config.setter
    def config(self, new_config: dict):
        self._config = self.init_config(config=new_config)

    @property
    def service_config(self) -> dict:
        """ Returns current service config """
        return self.config.get('users', {}).get(self.service_name) or dict()

    @property
    def __basic_configurable_properties(self) -> Dict[str, Any]:
        """
        Mapping of basic configurable properties to their default values.
        WARNING: This method should be left untouched to prevent unexpected
        behaviour. To override values of the basic properties specify it in
        self.service_configurable_properties()
        """
        return {
            'sync_period': 10,  # in seconds
            'observe_period': 20,  # in seconds
            'vhost_prefix': '',  # Could be used for scalability purposes
            'default_testing_prefix': 'test',
            'testing_envs': (f'{self.service_name.upper()}_TESTING',
                             'MQ_TESTING',),  # order matters
            'testing_prefix_envs': (f'{self.service_name.upper()}'
                                    f'_TESTING_PREFIX',
                                    'MQ_TESTING_PREFIX',)  # order matters
        }

    @property
    def service_configurable_properties(self) -> Dict[str, Any]:
        """
        Mapping of service-related configurable properties to default values.
        Override to provide service-specific configurable properties AND to
        update the default values of basic properties
        """
        return {}

    @property
    def __configurable_properties(self):
        """
        Joins basic configurable properties with appended once
        WARNING: This method should NOT be modified by children to prevent
        unexpected behaviour
        """
        return {**self.__basic_configurable_properties,
                **self.service_configurable_properties}

    def __init_configurable_properties(self):
        """
        Initialize properties based on the config and configurable properties
        WARNING: This method should NOT be modified by children to prevent
        unexpected behaviour
        """
        for _property, default_value in self.__configurable_properties.items():
            setattr(self, _property,
                    self.service_config.get(self.property_key,
                                            {}).get(_property, default_value))

    @property
    def service_id(self):
        """
        ID of the service should be considered to be unique
        """
        if not self._service_id:
            self._service_id = self.create_unique_id()
        return self._service_id

    @property
    def mq_credentials(self):
        """
        Returns MQ Credentials object based on self.config values
        """
        if not self.service_config or self.service_config == dict():
            raise Exception(f'Configuration is not set for {self.service_name}')
        return pika.PlainCredentials(
            self.service_config.get('user', 'guest'),
            self.service_config.get('password', 'guest'))

    @property
    def testing_mode(self) -> bool:
        """
        Indicates if given instance is instantiated in testing mode
        """
        return any(os.environ.get(env_var, '0') == '1'
                   for env_var in self.testing_envs)

    @property
    def testing_prefix(self) -> str:
        """
        Returns testing mode prefix for the item
        """
        for env_var in self.testing_prefix_envs:
            prefix = os.environ.get(env_var)
            if prefix:
                return prefix
        return self.default_testing_prefix

    @property
    def vhost(self):
        if not self._vhost:
            self._vhost = '/'
        if self.vhost_prefix and self.vhost_prefix not in \
                self._vhost.split('_')[0]:
            self._vhost = f'/{self.vhost_prefix}_{self._vhost[1:]}'
        if self.testing_mode and self.testing_prefix not in \
                self._vhost.split('_')[0]:
            self._vhost = f'/{self.testing_prefix}_{self._vhost[1:]}'
        if self._vhost.endswith('_'):
            self._vhost = self._vhost[:-1]
        return self._vhost

    @vhost.setter
    def vhost(self, val: str):
        if not val:
            val = ''
        elif not isinstance(val, str):
            val = str(val)
        if not val.startswith('/'):
            val = f'/{val}'
        self._vhost = val

    def get_connection_params(self, vhost: str, **kwargs) -> \
            pika.ConnectionParameters:
        """
        Gets connection parameters to be used to create an mq connection
        :param vhost: virtual_host to connect to
        """
        connection_params = pika.ConnectionParameters(
            host=self.config.get('server', 'localhost'),
            port=int(self.config.get('port', '5672')),
            virtual_host=vhost,
            credentials=self.mq_credentials, **kwargs)
        return connection_params

    @staticmethod
    def create_unique_id():
        """Method for generating unique id"""
        return uuid.uuid4().hex

    @classmethod
    def emit_mq_message(cls,
                        connection: Union[pika.BlockingConnection,
                        pika.SelectConnection],
                        request_data: dict,
                        exchange: Optional[str] = '',
                        queue: Optional[str] = '',
                        exchange_type: Union[str, ExchangeType] =
                        ExchangeType.direct,
                        expiration: int = 1000) -> str:
        """
        Emits request to the neon api service on the MQ bus
        :param connection: pika connection object
        :param queue: name of the queue to publish in
        :param request_data: dictionary with the request data
        :param exchange: name of the exchange (optional)
        :param exchange_type: type of exchange to declare
            (defaults to direct)
        :param expiration: mq message expiration time in millis
            (defaults to 1 second)

        :raises ValueError: invalid request data provided
        :returns message_id: id of the sent message
        """
        # Make a copy of request_data to prevent modifying the input object
        request_data = dict(request_data)

        if not isinstance(request_data, dict):
            raise TypeError(f"Expected dict and got {type(request_data)}")
        if not request_data:
            raise ValueError('No request data provided')

        # Ensure `message_id` in data will match context in messagebus connector
        if request_data.get('message_id') is None:
            request_data['message_id'] = \
                request_data.get("context", {}).get("mq", {}).get("message_id")\
                or cls.create_unique_id()

        def _on_channel_open(new_channel):
            if exchange:
                new_channel.exchange_declare(exchange=exchange,
                                             exchange_type=exchange_type,
                                             auto_delete=False)
            if queue:
                declared_queue = new_channel.queue_declare(queue=queue,
                                                           auto_delete=False)
                if exchange_type == ExchangeType.fanout.value:
                    new_channel.queue_bind(queue=declared_queue.method.queue,
                                           exchange=exchange)
            new_channel.basic_publish(exchange=exchange or '',
                                      routing_key=queue,
                                      body=dict_to_b64(request_data),
                                      properties=pika.BasicProperties(
                                          expiration=str(expiration)))

            new_channel.close()

        if isinstance(connection, pika.BlockingConnection):
            LOG.debug(f"Using blocking connection for request: {request_data}")
            _on_channel_open(connection.channel())
        else:
            LOG.debug(f"Using select connection for queue: {queue}")
            connection.channel(on_open_callback=_on_channel_open)

        # LOG.debug(f"sent message: {request_data['message_id']}")
        return request_data['message_id']

    @classmethod
    def publish_message(cls,
                        connection: pika.BlockingConnection,
                        request_data: dict,
                        exchange: Optional[str] = '',
                        expiration: int = 1000) -> str:
        """
        Publishes message via fanout exchange, wrapper for emit_mq_message
        :param connection: pika connection object
        :param request_data: dictionary with the request data
        :param exchange: name of the exchange (optional)
        :param expiration: mq message expiration time in millis
            (defaults to 1 second)

        :raises ValueError: invalid request data provided
        :returns message_id: id of the sent message
        """
        return cls.emit_mq_message(connection=connection,
                                   request_data=request_data, exchange=exchange,
                                   queue='', exchange_type='fanout',
                                   expiration=expiration)

    def send_message(self,
                     request_data: dict,
                     vhost: str = '',
                     connection_props: dict = None,
                     exchange: Optional[str] = '',
                     queue: Optional[str] = '',
                     exchange_type: ExchangeType = ExchangeType.direct,
                     expiration: int = 1000) -> str:
        """
        Wrapper method for creation the MQ connection and immediate propagation
        of requested message with that

        :param request_data: dictionary containing requesting data
        :param vhost: MQ Virtual Host (if not specified, uses its object native)
        :param exchange: MQ Exchange name (optional)
        :param queue: MQ Queue name (optional for ExchangeType.fanout)
        :param connection_props: supportive connection properties while
            connection creation (optional)
        :param exchange_type: type of exchange to use
            (defaults to ExchangeType.direct)
        :param expiration: posted data expiration (in millis)

        :returns message_id: id of the propagated message
        """
        if not vhost:
            vhost = self.vhost
        if not connection_props:
            connection_props = {}
        # LOG.debug(f'Opening connection on vhost={vhost} queue={queue}')
        with self.create_mq_connection(vhost=vhost,
                                       **connection_props) as mq_conn:
            if exchange_type in (ExchangeType.fanout,
                                 ExchangeType.fanout.value,):
                # LOG.debug(f'Sending fanout request to exchange: {exchange}')
                msg_id = self.publish_message(connection=mq_conn,
                                              request_data=request_data,
                                              exchange=exchange,
                                              expiration=expiration)
            else:
                # LOG.debug(f'Sending {exchange_type} request to exchange '
                #           f'{exchange}')
                msg_id = self.emit_mq_message(mq_conn,
                                              queue=queue,
                                              request_data=request_data,
                                              exchange=exchange,
                                              exchange_type=exchange_type,
                                              expiration=expiration)
        # LOG.debug(f'Message propagated, id={msg_id}')
        return msg_id

    @retry(use_self=True, num_retries=__run_retries__)
    def create_mq_connection(self, vhost: str = '/', **kwargs):
        """
            Creates MQ Connection on the specified virtual host
            Note: Additional parameters can be defined via kwargs.

            :param vhost: address for desired virtual host
            :raises Exception if self.config is not set
        """
        if not self.config:
            raise Exception('Configuration is not set')
        return pika.BlockingConnection(
            parameters=self.get_connection_params(vhost, **kwargs))

    def register_consumer(self, name: str, vhost: str, queue: str,
                          callback: callable,
                          on_error: Optional[callable] = None,
                          auto_ack: bool = True, queue_reset: bool = False,
                          exchange: str = None, exchange_type: str = None,
                          exchange_reset: bool = False,
                          queue_exclusive: bool = False,
                          skip_on_existing: bool = False,
                          restart_attempts: int = __max_consumer_restarts__):
        """
        Registers a consumer for the specified queue.
        The callback function will handle items in the queue.
        Any raised exceptions will be passed as arguments to on_error.
        :param name: Human-readable name of the consumer
        :param vhost: vhost to register on
        :param queue: MQ Queue to read messages from
        :param queue_reset: to delete queue if exists (defaults to False)
        :param exchange: MQ Exchange to bind to
        :param exchange_reset: to delete exchange if exists (defaults to False)
        :param exchange_type: Type of MQ Exchange to use, documentation:
            https://www.rabbitmq.com/tutorials/amqp-concepts.html
        :param callback: Callback method on received messages
        :param on_error: Optional method to handle any exceptions
            raised in message handling
        :param auto_ack: Boolean to enable ack of messages upon receipt
        :param queue_exclusive: if Queue needs to be exclusive
        :param skip_on_existing: to skip if consumer already exists
        :param restart_attempts: max instance restart attempts
            (if < 0 - will restart infinitely times)
        """
        error_handler = on_error or self.default_error_handler
        consumer = self.consumers.get(name, None)
        if consumer:
            # Gracefully terminating
            if skip_on_existing:
                LOG.info(f'Consumer under index "{name}" already declared')
                return
            self.stop_consumers(names=(name,))
        self.consumer_properties.setdefault(name, {})
        self.consumer_properties[name]['properties'] = \
            dict(
                name=name,
                connection_params=self.get_connection_params(vhost),
                queue=queue,
                queue_reset=queue_reset,
                callback_func=callback,
                exchange=exchange,
                exchange_reset=exchange_reset,
                exchange_type=exchange_type,
                error_func=error_handler,
                auto_ack=auto_ack,
                queue_exclusive=queue_exclusive,
            )
        self.consumer_properties[name]['restart_attempts'] = int(restart_attempts)
        self.consumer_properties[name]['started'] = False

        if exchange_type == ExchangeType.fanout.value:
            LOG.debug(f'Subscriber exchange listener registered: '
                      f'[name={name},exchange={exchange},vhost={vhost},'
                      f'async={self.async_consumers_enabled}]')
        else:
            LOG.debug(f'Consumer queue listener registered: '
                      f'[name={name},queue={queue},vhost={vhost},'
                      f'async={self.async_consumers_enabled}]')

        self.consumers[name] = self.consumer_thread_cls(**self.consumer_properties[name]['properties'])

    @property
    def consumer_thread_cls(self) -> Type[ConsumerThreadInstance]:
        if self.async_consumers_enabled:
            return SelectConsumerThread
        return BlockingConsumerThread

    def check_health(self) -> bool:
        """
        Health check to determine if each consumer is in a healthy state.
        """
        if not self._consumers_started:
            LOG.info("Waiting for consumer start")
            return False
        for name, props in self.consumer_properties.items():
            thread = self.consumers.get(name)
            if thread and thread.is_alive():
                # Thread is alive, assume this one is fine
                continue
            elif thread and props.get("dead"):
                # Thread exists but is not alive
                LOG.error(f"Consumer {name} is dead and cannot be restarted")
                return False
            else:
                # The thread does not exist
                if props.get('restart_attempts',
                             self.__max_consumer_restarts__) >= self.__max_consumer_restarts__:
                    LOG.error(f"Consumer {name} has exceeded max restart attempts")
                elif props.get('dead'):
                    # Explicitly marked as dead after failure to restart
                    LOG.error(f"Consumer {name} is marked as dead")
                else:
                    # Consumers are started but this thread is missing
                    LOG.error(f"Consumer {name} is not running but not also "
                              f"not marked as dead.")
                return False
        # Nothing is dead, return True
        return True

    def restart_consumer(self, name: str):
        self.stop_consumers(names=(name,))
        consumer_data = self.consumer_properties.get(name, {})
        restart_attempts = consumer_data.get('restart_attempts',
                                             self.__max_consumer_restarts__)
        err_msg = ''
        if not consumer_data.get('properties'):
            err_msg = 'creation properties not found'
        elif 0 < restart_attempts < consumer_data.get('num_restarted', 0):
            err_msg = 'num restarts exceeded'
            self.consumers.pop(name, None)
        elif self.consumers[name].queue_exclusive:
            err_msg = 'Exclusive queue may not be restarted'
            self.consumers.pop(name, None)
            # TODO: Register a new subscriber?
        else:
            self.consumers[name] = self.consumer_thread_cls(**consumer_data['properties'])
            self.run_consumers(names=(name,))
            self.consumer_properties[name].setdefault('num_restarted', 0)
            self.consumer_properties[name]['num_restarted'] += 1
        if err_msg:
            self.consumer_properties[name]['dead'] = True
            LOG.error(f'Cannot restart consumer "{name}" - {err_msg}')

    def register_subscriber(self, name: str, vhost: str,
                            callback: callable,
                            on_error: Optional[callable] = None,
                            exchange: str = None,
                            exchange_reset: bool = False,
                            auto_ack: bool = True,
                            skip_on_existing: bool = False,
                            restart_attempts: int = __max_consumer_restarts__):
        """
        Registers fanout exchange subscriber, wraps register_consumer()
        Any raised exceptions will be passed as arguments to on_error.
        :param name: Human-readable name of the consumer
        :param vhost: vhost to register on
        :param exchange: MQ Exchange for binding to
        :param exchange_reset: delete exchange if exists (defaults to False)
        :param callback: Callback method on received messages
        :param on_error: Optional method to handle any exceptions raised
            in message handling
        :param auto_ack: Boolean to enable ack of messages upon receipt
        :param skip_on_existing: to skip if consumer already exists
            (defaults to False)
        :param restart_attempts: max instance restart attempts
            (if < 0 - will restart infinitely times)
        """
        # for fanout exchange queue does not matter unless its non-conflicting
        # and is bounded
        subscriber_queue = f'subscriber_{exchange}_{uuid.uuid4().hex[:6]}'
        return self.register_consumer(name=name, vhost=vhost,
                                      queue=subscriber_queue,
                                      callback=callback, queue_reset=False,
                                      on_error=on_error, exchange=exchange,
                                      exchange_type=ExchangeType.fanout.value,
                                      exchange_reset=exchange_reset,
                                      auto_ack=auto_ack, queue_exclusive=False,
                                      skip_on_existing=skip_on_existing,
                                      restart_attempts=restart_attempts)

    @staticmethod
    def default_error_handler(thread: ConsumerThreadInstance,
                              exception: Exception):
        LOG.error(f"{exception} occurred in {thread}")
        if isinstance(exception, pika.exceptions.AMQPError):
            LOG.info("Raising exception to exit")
            # This is a fatal error; raise it so this object can be re-created
            raise exception

    def run_consumers(self, names: Optional[tuple] = None, daemon=True):
        """
        Runs consumer threads based on the name if present
        (starts all of the declared consumers by default)

        :param names: names of consumers to consider
        :param daemon: to kill consumer threads once main thread is over
        """
        if not names:
            names = list(self.consumers)
        for name in names:
            if (isinstance(self.consumers.get(name), SUPPORTED_THREADED_CONSUMERS)
                    and self.consumers[name].is_consumer_alive
                    and not self.consumers[name].is_consuming):
                self.consumers[name].daemon = daemon
                self.consumers[name].start()
                self.consumer_properties[name]['started'] = True
        LOG.debug(f"Started consumers for {self.service_name}")

    def stop_consumers(self, names: Optional[tuple] = None):
        """
            Stops consumer threads based on the name if present
            (stops all of the declared consumers by default)
        """
        if not names:
            names = list(self.consumers)
        for name in names:
            try:
                if isinstance(self.consumers.get(name),
                              SUPPORTED_THREADED_CONSUMERS) and \
                        self.consumers[name].is_alive():
                    self.consumers[name].join(timeout=self.__consumer_join_timeout__)
                    if self.consumers[name].is_alive():
                        LOG.error(f"Failed to join consumer thread: {name} "
                                  f"after {self.__consumer_join_timeout__}s")
                    self.consumer_properties[name]['started'] = False
            except Exception as e:
                raise ChildProcessError(e)
        LOG.debug(f"Stopped consumers for {self.service_name}")

    @retry(callback_on_exceeded='stop_sync_thread', use_self=True,
           num_retries=__run_retries__)
    def sync(self, vhost: str = None, exchange: str = None, queue: str = None,
             request_data: dict = None):
        """
        Periodic notification message to be sent into MQ,
        used to notify other network listeners about this service health status

        :param vhost: mq virtual host (defaults to self.vhost)
        :param exchange: mq exchange (defaults to base one)
        :param queue: message queue prefix (defaults to self.service_name)
        :param request_data: data to publish in sync
        """
        vhost = vhost or self.vhost
        queue = f'{queue or self.service_name}_sync'
        exchange = exchange or ''
        request_data = request_data or {'service_id': self.service_id,
                                        'time': int(time.time())}

        with self.create_mq_connection(vhost=vhost) as mq_connection:
            LOG.debug(f'Emitting sync message to (vhost="{vhost}",'
                      f' exchange="{exchange}", queue="{queue}")')
            self.publish_message(mq_connection, exchange=exchange,
                                 request_data=request_data)

    @retry(callback_on_exceeded='stop', use_self=True,
           num_retries=__run_retries__)
    def run(self, run_consumers: bool = True, run_sync: bool = True,
            run_observer: Optional[bool] = None, **kwargs):
        """
        Generic method called on running the instance

        :param run_consumers: to run this instance consumers (defaults to True)
        :param run_sync: to run synchronization thread (defaults to True)
        :param run_observer: to run consumers state observation
            (defaults to True for Blocking Consumers, else False)
        """
        if run_observer is None:
            # Observer thread is default on for Blocking Consumer only
            run_observer = self.consumer_thread_cls == BlockingConsumerThread

        host = self.config.get('server', 'localhost')
        port = int(self.config.get('port', '5672'))
        if not wait_for_mq_startup(host, port, kwargs.get('mq_timeout', 120),
                                   connection_params=self.get_connection_params(
                                       self.vhost)):
            raise ConnectionError(f"Failed to connect to MQ at {host}:{port}")
        kwargs.setdefault('consumer_names', ())
        kwargs.setdefault('daemonize_consumers', False)
        self.pre_run(**kwargs)
        if run_consumers:
            self.run_consumers(names=kwargs['consumer_names'],
                               daemon=kwargs['daemonize_consumers'])
        if run_sync:
            self.sync_thread.start()
        if run_observer:
            self.observer_thread.start()
        self.post_run(**kwargs)
        self._consumers_started = True

    @property
    def sync_thread(self) -> RepeatingTimer:
        """Creates new synchronization thread if none is present"""
        if not (isinstance(self._sync_thread, RepeatingTimer) and
                self._sync_thread.is_alive()):
            self._sync_thread = RepeatingTimer(self.sync_period, self.sync)
            self._sync_thread.daemon = True
        return self._sync_thread

    def stop_sync_thread(self) -> None:
        """Stops synchronization thread and dereferences it"""
        if self._sync_thread:
            self._sync_thread.cancel()
            self._sync_thread = None

    def observe_consumers(self):
        """
        Iteratively observes each consumer, and if it was launched but is not
        alive - restarts it
        """
        # LOG.debug('Observers state observation')
        consumers_dict = copy.copy(self.consumers)
        for consumer_name, consumer_instance in consumers_dict.items():
            if (self.consumer_properties[consumer_name]['started'] and
                    not (isinstance(consumer_instance, SUPPORTED_THREADED_CONSUMERS)
                         and consumer_instance.is_alive()
                         and consumer_instance.is_consumer_alive)):
                LOG.info(f'Consumer "{consumer_name}" is dead, restarting')
                self.restart_consumer(name=consumer_name)

    @property
    def observer_thread(self):
        """Creates new observer thread if none is present"""
        if not (isinstance(self._observer_thread, RepeatingTimer) and
                self._observer_thread.is_alive()):
            self._observer_thread = RepeatingTimer(self.observe_period,
                                                   self.observe_consumers)
            self._observer_thread.daemon = True
        return self._observer_thread

    def stop_observer_thread(self):
        """Stops observer thread and dereferences it"""
        if self._observer_thread:
            self._observer_thread.cancel()
            self._observer_thread = None

    def stop(self):
        """Generic method for graceful instance stopping"""
        self.stop_consumers()
        self.stop_sync_thread()
        self.stop_observer_thread()
        self._consumers_started = False
        LOG.info(f"Stopped Connector {self.service_name}")

    def pre_run(self, **kwargs):
        """Additional logic invoked before method run()"""
        pass

    def post_run(self, **kwargs):
        """Additional logic invoked after method run()"""
        pass
