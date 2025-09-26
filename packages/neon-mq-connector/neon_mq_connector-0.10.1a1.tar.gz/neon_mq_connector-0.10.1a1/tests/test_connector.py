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

import threading
import time
import unittest
import pika
import pytest

from os import environ
from unittest.mock import Mock, patch
from ovos_utils.log import LOG
from pika.adapters.blocking_connection import BlockingConnection
from pika.adapters.select_connection import SelectConnection
from pika.exchange_type import ExchangeType

from neon_mq_connector.connector import MQConnector, ConsumerThreadInstance
from neon_mq_connector.utils import RepeatingTimer
from neon_mq_connector.utils.rabbit_utils import create_mq_callback

from neon_minerva.integration.rabbit_mq import rmq_instance  # noqa: F401

environ["TEST_RMQ_VHOSTS"] = "/neon_testing"


class MQConnectorChild(MQConnector):
    def __init__(self, config: dict, service_name: str):
        super().__init__(config=config, service_name=service_name)
        self.func_1_ok = False
        self.func_2_ok = False
        self.func_3_ok = False
        self.func_3_knocks = 0
        self.callback_ok = False
        self.exception = None
        self._consume_event = None
        self._consumer_restarted_event = None
        self._vhost = "/neon_testing"
        self.observe_period = 5

    @create_mq_callback(include_callback_props=('channel', 'method',))
    def callback_func_1(self, channel, method):
        if self.func_2_ok:
            self.consume_event.set()
        self.func_1_ok = True
        channel.basic_ack(delivery_tag=method.delivery_tag)

    @create_mq_callback(include_callback_props=('channel', 'method',))
    def callback_func_2(self, channel, method):
        if self.func_1_ok:
            self.consume_event.set()
        self.func_2_ok = True
        channel.basic_ack(delivery_tag=method.delivery_tag)

    @create_mq_callback(include_callback_props=())
    def callback_func_3(self):
        self.func_3_ok = False
        self.func_3_knocks += 1
        if self.func_3_knocks == 1:
            raise Exception('I am failing on the first knock')
        self.func_3_ok = True
        self.consume_event.set()

    @create_mq_callback(include_callback_props=('channel', 'method',))
    def callback_func_after_message(self, channel, method):
        self.consume_event.set()
        self.callback_ok = True
        channel.basic_ack(delivery_tag=method.delivery_tag)

    def callback_func_error(self, channel, method, properties, body):
        raise Exception("Exception to Handle")

    def handle_error(self, thread: ConsumerThreadInstance, exception: Exception):
        self.exception = exception
        self.consume_event.set()

    @property
    def consume_event(self):
        if not self._consume_event or self._consume_event.is_set():
            self._consume_event = threading.Event()
        return self._consume_event

    @property
    def consumer_restarted_event(self):
        if not self._consumer_restarted_event or self._consumer_restarted_event.is_set():
            self._consumer_restarted_event = threading.Event()
        return self._consumer_restarted_event

    def restart_consumer(self, name: str):
        super(MQConnectorChild, self).restart_consumer(name=name)
        if name == 'test3':
            self.consumer_restarted_event.set()


@pytest.mark.usefixtures("rmq_instance")
class MQConnectorChildTest(unittest.TestCase):
    connector_instance = None

    def setUp(self):
        if self.connector_instance is None:
            self.connector_instance = MQConnectorChild(
                config={"server": "127.0.0.1",
                        "port": self.rmq_instance.port,
                        "users": {
                            "test": {
                                "user": "test_user",
                                "password": "test_password"
                            }}},
                service_name='test')
            self.connector_instance.run(run_sync=False)

    @classmethod
    def tearDownClass(cls) -> None:
        try:
            if cls.connector_instance is not None:
                cls.connector_instance.stop()
        except ChildProcessError as e:
            LOG.error(e)

    def test_not_null_service_id(self):
        self.assertIsNotNone(self.connector_instance.service_id)

    def tearDown(self):
        self.connector_instance.stop_consumers()

    @pytest.mark.timeout(30)
    def test_mq_messaging(self):
        self.connector_instance.func_1_ok = False
        self.connector_instance.func_2_ok = False
        test_consumers = ('test1', 'test2',)

        self.connector_instance.register_consumer(name="test1",
                                                  vhost=self.connector_instance.vhost,
                                                  exchange='',
                                                  queue='test',
                                                  callback=self.connector_instance.callback_func_1,
                                                  auto_ack=False, )
        self.connector_instance.register_consumer(name="test2",
                                                  vhost=self.connector_instance.vhost,
                                                  exchange='',
                                                  queue='test1',
                                                  callback=self.connector_instance.callback_func_2,
                                                  auto_ack=False, )

        self.connector_instance.run_consumers(names=test_consumers)

        self.connector_instance.send_message(queue='test',
                                             request_data={'data': 'Hello!'},
                                             expiration=4000)
        self.connector_instance.send_message(queue='test1',
                                             request_data={'data': 'Hello 2!'},
                                             expiration=4000)

        self.connector_instance.consume_event.wait(10)

        self.assertTrue(self.connector_instance.func_1_ok)
        self.assertTrue(self.connector_instance.func_2_ok)

    @pytest.mark.timeout(30)
    def test_publish_subscribe(self):
        self.connector_instance.func_1_ok = False
        self.connector_instance.func_2_ok = False
        test_consumers = ('test1', 'test2',)

        self.connector_instance.register_subscriber(name="test1",
                                                    vhost=self.connector_instance.vhost,
                                                    exchange='test',
                                                    # exchange_reset=True,
                                                    callback=self.connector_instance.callback_func_1,
                                                    auto_ack=False, )
        self.connector_instance.register_subscriber(name="test2", vhost=self.connector_instance.vhost,
                                                    exchange='test',
                                                    callback=self.connector_instance.callback_func_2,
                                                    auto_ack=False, )

        self.connector_instance.run_consumers(names=test_consumers)
        time.sleep(0.5)

        self.connector_instance.send_message(exchange='test',
                                             exchange_type=ExchangeType.fanout,
                                             request_data={'data': 'Hello!'},
                                             expiration=4000)

        self.connector_instance.consume_event.wait(10)

        self.assertTrue(self.connector_instance.func_1_ok)
        self.assertTrue(self.connector_instance.func_2_ok)

    @pytest.mark.timeout(30)
    def test_error(self, ):
        self.connector_instance.register_consumer(
            name="error",
            vhost=self.connector_instance.vhost,
            queue="error",
            queue_reset=True,
            callback=self.connector_instance.callback_func_error,
            on_error=self.connector_instance.handle_error,
            auto_ack=False,
            restart_attempts=0
        )
        self.connector_instance.run_consumers(names=("error",))
        time.sleep(0.5)

        self.connector_instance.send_message(queue='error',
                                             request_data={'data': 'test'},
                                             expiration=4000)

        self.connector_instance.consume_event.wait(10)

        self.assertIsInstance(self.connector_instance.exception, Exception)
        self.assertEqual(str(self.connector_instance.exception), "Exception to Handle")

    @pytest.mark.timeout(30)
    def test_consumer_after_message(self, ):

        self.connector_instance.send_message(queue='test3',
                                             request_data={'data': 'test'},
                                             expiration=3000)

        self.connector_instance.register_consumer(name="test_consumer_after_message",
                                                  vhost=self.connector_instance.vhost,
                                                  queue="test3",
                                                  callback=self.connector_instance.callback_func_after_message,
                                                  auto_ack=False, )

        self.connector_instance.run_consumers(names=("test_consumer_after_message",))

        self.connector_instance.consume_event.wait(10)

        self.assertTrue(self.connector_instance.callback_ok)

    @pytest.mark.timeout(30)
    def test_consumer_restarted(self, ):
        self.connector_instance.register_consumer(
            name="test3",
            vhost=self.connector_instance.vhost,
            exchange='',
            queue='test_failing_once_queue',
            queue_reset=True,
            callback=self.connector_instance.callback_func_3,
            restart_attempts=1,
            auto_ack=False,
        )
        self.connector_instance.run_consumers(names=('test3',))
        time.sleep(0.5)

        self.connector_instance.send_message(queue='test_failing_once_queue',
                                             request_data={'data': 'knock'},
                                             expiration=4000)

        self.connector_instance.consumer_restarted_event.wait(self.connector_instance.observe_period + 5)

        self.connector_instance.send_message(queue='test_failing_once_queue',
                                             request_data={'data': 'knock'},
                                             expiration=4000)

        self.connector_instance.consume_event.wait(10)

        self.assertTrue(self.connector_instance.func_3_ok)

    def test_sync_thread(self):
        self.assertIsInstance(self.connector_instance.sync_thread,
                              RepeatingTimer)

    def test_sync(self):
        real_method = self.connector_instance.publish_message
        mock_method = Mock()
        self.connector_instance.publish_message = mock_method

        self.connector_instance.sync()
        mock_method.assert_called_once()

        self.connector_instance.publish_message = real_method


@pytest.mark.usefixtures("rmq_instance")
class MQConnectorChildAsyncModeTest(MQConnectorChildTest):

    def setUp(self):
        MQConnectorChildTest.setUp(self)
        self.connector_instance.async_consumers_enabled = True


@pytest.mark.usefixtures("rmq_instance")
class TestMQConnectorInit(unittest.TestCase):
    def test_connector_init(self):
        connector = MQConnector(None, "test")
        self.assertEqual(connector.service_name, "test")
        self.assertEqual(connector.consumers, dict())
        self.assertEqual(connector.consumer_properties, dict())

        # Test properties
        self.assertIsInstance(connector.config, dict)
        test_config = {"test": {"username": "test",
                                "password": "test"}}
        connector.config = test_config
        self.assertEqual(connector.config, test_config)
        connector.config = {"MQ": test_config}
        self.assertEqual(connector.config, test_config)

        self.assertIsInstance(connector.service_configurable_properties, dict)
        self.assertIsInstance(connector.service_id, str)

        # Test credentials
        with self.assertRaises(Exception):
            connector.mq_credentials()
        connector.config = {"MQ": {"users": {"test": {"user": "username",
                                                      "password": "test"}}}}
        creds = connector.mq_credentials
        self.assertIsInstance(creds, pika.PlainCredentials)
        self.assertEqual(creds.username, "username")
        self.assertEqual(creds.password, "test")

        # Testing test vars
        self.assertIsInstance(connector.testing_mode, bool)
        self.assertIsInstance(connector.testing_prefix, str)

        # self.assertEqual(connector.vhost, '/')
        test_vhost = "/testing"
        connector.vhost = "testing"
        self.assertEqual(connector.vhost, test_vhost)
        connector.vhost = "/testing"
        self.assertEqual(connector.vhost, test_vhost)

    @patch("neon_mq_connector.utils.connection_utils.get_timeout")
    def test_init_rmq_down(self, get_timeout):
        get_timeout.return_value = 0.01
        test_config = {"server": "127.0.0.1",
                       "port": self.rmq_instance.port,
                       "users": {
                           "test": {
                               "user": "test_user",
                               "password": "test_password"
                           }}}
        test_vhost = "/neon_testing"
        test_queue = "test_queue"
        connector = MQConnector(test_config, "test")
        connector.vhost = test_vhost

        request_data = {"test": True,
                        "data": ["test"]}

        callback_event = threading.Event()
        callback = Mock(side_effect=lambda *args: callback_event.set())
        connector.register_consumer("test_consumer", vhost=test_vhost,
                                    queue=test_queue, callback=callback)

        # Connector fails to start without RMQ
        self.rmq_instance.stop()
        connector.run(run_sync=False, run_observer=False, mq_timeout=1)
        self.assertFalse(connector.started)
        self.assertFalse(connector.check_health())
        for consumer in connector.consumers.values():
            # The consumer is marked as alive at init, until explicitly joined
            # self.assertFalse(consumer.is_consumer_alive)
            self.assertFalse(consumer.is_consuming)
            self.assertFalse(consumer.is_alive())

        # Restart connector after RMQ is started
        self.rmq_instance.start()
        connector.run(run_sync=False, run_observer=False)
        self.assertTrue(connector.started)
        self.assertTrue(connector.check_health())
        connector.send_message(request_data, test_vhost, queue=test_queue)
        callback_event.wait(timeout=5)
        self.assertTrue(callback_event.is_set())
        callback.assert_called_once()
        connector.stop()

    def test_emit_mq_message(self):
        from neon_mq_connector.utils.network_utils import b64_to_dict

        test_config = {"server": "127.0.0.1",
                       "port": self.rmq_instance.port,
                       "users": {
                           "test": {
                               "user": "test_user",
                               "password": "test_password"
                           }}}
        test_vhost = "/neon_testing"
        test_queue = "test_queue"
        connector = MQConnector(test_config, "test")
        connector.vhost = test_vhost

        request_data = {"test": True,
                        "data": ["test"]}

        callback_event = threading.Event()
        callback = Mock(side_effect=lambda *args: callback_event.set())
        connector.register_consumer("test_consumer", vhost=test_vhost,
                                    queue=test_queue, callback=callback)
        connector.run(run_sync=False, run_observer=False)

        open_event = threading.Event()
        close_event = threading.Event()
        on_open = Mock(side_effect=lambda *args: open_event.set())
        on_error = Mock()
        on_close = Mock(side_effect=lambda *args: close_event.set())

        blocking_connection = BlockingConnection(
            parameters=connector.get_connection_params(test_vhost))

        async_connection = SelectConnection(
            parameters=connector.get_connection_params(test_vhost),
            on_open_callback=on_open, on_open_error_callback=on_error,
            on_close_callback=on_close)
        async_thread = threading.Thread(target=async_connection.ioloop.start,
                                        daemon=True)
        async_thread.start()

        # Blocking connection emit
        message_id = connector.emit_mq_message(blocking_connection,
                                               request_data, queue=test_queue)
        self.assertIsInstance(message_id, str)
        callback_event.wait(timeout=5)
        self.assertTrue(callback_event.is_set())
        callback.assert_called_once()
        self.assertEqual(b64_to_dict(callback.call_args.args[3]),
                         {**request_data, "message_id": message_id})
        callback.reset_mock()
        callback_event.clear()

        # Async connection emit
        open_event.wait(timeout=5)
        self.assertTrue(open_event.is_set())
        on_open.assert_called_once()
        message_id_2 = connector.emit_mq_message(async_connection,
                                                 request_data, queue=test_queue)
        self.assertIsInstance(message_id_2, str)
        self.assertNotEqual(message_id, message_id_2)
        callback_event.wait(timeout=5)
        self.assertTrue(callback_event.is_set())
        callback.assert_called_once()
        self.assertEqual(b64_to_dict(callback.call_args.args[3]),
                         {**request_data, "message_id": message_id_2})
        callback.reset_mock()
        callback_event.clear()

        # message_id set to `None`
        message_id_3 = connector.emit_mq_message(async_connection,
                                                 {**request_data,
                                                  "message_id": None},
                                                 queue=test_queue)
        self.assertIsInstance(message_id_3, str)
        self.assertNotEqual("", message_id_3)
        callback_event.wait(timeout=5)
        self.assertTrue(callback_event.is_set())
        callback.assert_called_once()
        self.assertEqual(b64_to_dict(callback.call_args.args[3]),
                         {**request_data, "message_id": message_id_3})
        callback.reset_mock()
        callback_event.clear()

        on_close.assert_not_called()
        connector.stop()

        async_connection.close()
        close_event.wait(timeout=5)
        self.assertTrue(close_event.is_set())
        on_close.assert_called_once()

        async_thread.join(3)
        on_error.assert_not_called()

# TODO: test other methods
