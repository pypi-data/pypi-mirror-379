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

import uuid

from threading import Event
from pika.channel import Channel
from pika.spec import Basic, BasicProperties
from pika.exceptions import ProbableAccessDeniedError, StreamLostError
from neon_mq_connector.connector import MQConnector
from ovos_config.config import Configuration
from ovos_utils.log import LOG

from neon_mq_connector.utils.connection_utils import SuppressPikaLogging
from neon_mq_connector.utils.network_utils import b64_to_dict

_default_mq_config = {
    "server": "mq.neonaiservices.com",
    "port": 5672,
    "users": {
        "mq_handler": {
            "user": 'neon_api_utils',
            "password": 'Klatchat2021'
        }
    }
}


class NeonMQHandler(MQConnector):
    """
    This class is intended for use with `send_mq_request` for simple,
    transactional reqeusts. Applications needing a persistent connection to
    MQ services should implement `MQConnector` directly.
    """

    async_consumers_enabled = False

    def __init__(self, config: dict, service_name: str, vhost: str):
        super().__init__(config, service_name)
        self.vhost = vhost
        import pika
        self.connection = pika.BlockingConnection(
            parameters=self.get_connection_params(vhost))

    def shutdown(self):
        MQConnector.stop(self)
        with SuppressPikaLogging():
            self.connection.close()
        if not self.connection.is_closed:
            raise RuntimeError(f"Connection is still open: {self.connection}")


def send_mq_request(vhost: str, request_data: dict, target_queue: str,
                    response_queue: str = None, timeout: int = 30,
                    expect_response: bool = True) -> dict:
    """
    Sends a request to the MQ server and returns the response.
    :param vhost: vhost to target
    :param request_data: data to post to target_queue
    :param target_queue: queue to post request to
    :param response_queue: optional queue to monitor for a response.
        Generally should be blank
    :param timeout: time in seconds to wait for a response before timing out
    :param expect_response: boolean indicating whether a response is expected
    :return: response to request
    """
    response_queue = response_queue or uuid.uuid4().hex

    response_event = Event()
    message_id = None
    response_data = dict()
    config = dict()

    def on_error(thread, error):
        """
        Override default error handler to suppress certain logged errors.
        """
        if isinstance(error, StreamLostError):
            return
        LOG.error(f"{thread} raised {error}")

    def handle_mq_response(channel: Channel, method: Basic.Deliver,
                           _: BasicProperties, body: bytes):
        """
        Method that handles Neon API output.
        In case received output message with the desired id, event stops
        """
        api_output = b64_to_dict(body)

        # The Messagebus connector generates a unique `message_id` for each
        # response message. Check context for the original one; otherwise,
        # check in output directly as some APIs emit responses without a unique
        # message_id
        api_output_msg_id = \
            api_output.get('context',
                           api_output).get('mq', api_output).get('message_id')
        # TODO: One of these specs should be deprecated
        if api_output_msg_id != api_output.get('message_id'):
            LOG.debug(f"Handling message_id from response context")
        if api_output_msg_id == message_id:
            LOG.debug(f'MQ output: {api_output}')
            channel.basic_ack(delivery_tag=method.delivery_tag)
            channel.queue_delete(response_queue)
            channel.close()
            response_data.update(api_output)
            response_event.set()
        else:
            channel.basic_nack(delivery_tag=method.delivery_tag)
            LOG.debug(f"Ignoring {api_output_msg_id} waiting for {message_id}")

    neon_api_mq_handler = None
    try:
        config = Configuration().get('MQ') or _default_mq_config
        if not config['users'].get('mq_handler'):
            LOG.warning("mq_handler not configured, using default credentials")
            config['users']['mq_handler'] = \
                _default_mq_config['users']['mq_handler']
        neon_api_mq_handler = NeonMQHandler(config=config,
                                            service_name='mq_handler',
                                            vhost=vhost)
        if not neon_api_mq_handler.connection.is_open:
            raise ConnectionError("MQ Connection not established.")

        if expect_response:
            neon_api_mq_handler.register_consumer(
                'neon_output_handler', neon_api_mq_handler.vhost,
                response_queue, handle_mq_response, on_error, auto_ack=False)
            neon_api_mq_handler.run_consumers()
            request_data['routing_key'] = response_queue

        message_id = neon_api_mq_handler.emit_mq_message(
            connection=neon_api_mq_handler.connection, queue=target_queue,
            request_data=request_data, exchange='')
        LOG.debug(f'Sent request with keys: {request_data.keys()}')

        if expect_response:
            response_event.wait(timeout)
            if not response_event.is_set():
                LOG.error(f"Timeout waiting for response to: {message_id} on "
                          f"{response_queue}")
            with SuppressPikaLogging():
                neon_api_mq_handler.stop_consumers()
    except ProbableAccessDeniedError:
        raise ValueError(f"{vhost} is not a valid endpoint for "
                         f"{config.get('users').get('mq_handler').get('user')}")
    except Exception as ex:
        LOG.exception(f'Exception occurred while resolving Neon API: {ex}')
    finally:
        # Ensure this object is always cleaned up
        if neon_api_mq_handler:
            neon_api_mq_handler.shutdown()
    return response_data
