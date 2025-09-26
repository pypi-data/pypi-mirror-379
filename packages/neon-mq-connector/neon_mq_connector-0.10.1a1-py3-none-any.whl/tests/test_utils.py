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
import logging
import os
import time
import unittest
from unittest.mock import Mock

import pytest
import pika

from threading import Thread

from pika.exceptions import ProbableAuthenticationError
from pydantic import BaseModel

from neon_minerva.integration.rabbit_mq import rmq_instance  # noqa: F401

from neon_mq_connector.utils import RepeatingTimer
from neon_mq_connector.utils.connection_utils import get_timeout, retry, \
    wait_for_mq_startup
from neon_mq_connector.utils.client_utils import MQConnector, NeonMQHandler
from neon_mq_connector.utils.network_utils import dict_to_b64, b64_to_dict
from neon_mq_connector.utils.rabbit_utils import create_mq_callback

os.environ["TEST_RMQ_VHOSTS"] = "/neon_testing"

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
TEST_PATH = os.path.join(ROOT_DIR, "tests", "ccl_files")

RANDOM_STR = str(int(time.time()))

INPUT_CHANNEL_A = RANDOM_STR + '_a'
INPUT_CHANNEL_B = RANDOM_STR + '_b'
OUTPUT_CHANNEL = RANDOM_STR + '_output'

TEST_DICT = {b"section 1": {"key1": "val1",
                            "key2": "val2"},
             "section 2": {"key_1": b"val1",
                           "key_2": "val2"}}

TEST_DICT_B64 = b'IntiJ3NlY3Rpb24gMSc6IHsna2V5MSc6ICd2YWwxJywgJ2tleTInOiAndm' \
                b'FsMid9LCAnc2VjdGlvbiAyJzogeydrZXlfMSc6IGIndmFsMScsICdrZXlfM' \
                b'ic6ICd2YWwyJ319Ig=='


def callback_on_failure():
    """Simple callback on failure"""
    return False


class MockRequestModel(BaseModel):
    message_id: str
    test: bool = True


class MqCallbackDecoratorClass:
    from neon_mq_connector.utils.rabbit_utils import create_mq_callback
    class_callback = Mock()

    def __init__(self):
        self.callback = Mock()

    @create_mq_callback
    def default_callback(self, body):
        self.callback(body)

    @create_mq_callback(include_callback_props=())
    def no_kwargs_callback(self, **kwargs):
        self.callback(**kwargs)

    @staticmethod
    @create_mq_callback
    def static_callback(body):
        MqCallbackDecoratorClass.class_callback(body)

    @create_mq_callback(request_model=MockRequestModel)
    def callback_with_pydantic_model(self, **kwargs):
        self.callback(**kwargs)


class SimpleMQConnector(MQConnector):
    def __init__(self, config: dict, service_name: str, vhost: str):
        super().__init__(config, service_name)
        self.vhost = vhost

    @staticmethod
    def respond(channel, method, _, body):
        request = b64_to_dict(body)
        response = dict_to_b64({"message_id": request["message_id"],
                                "success": True,
                                "request_data": request["data"]})
        reply_channel = request.get("routing_key") or OUTPUT_CHANNEL
        channel.queue_declare(queue=reply_channel)
        channel.basic_publish(exchange='',
                              routing_key=reply_channel,
                              body=response,
                              properties=pika.BasicProperties(expiration='1000'))
        channel.basic_ack(delivery_tag=method.delivery_tag)

    @create_mq_callback
    def respond_wrapped(self, body: dict):
        return {
            "message_id": body["message_id"],
            "success": True,
            "request_data": body["data"],
        }



@pytest.mark.usefixtures("rmq_instance")
class TestClientUtils(unittest.TestCase):
    test_connector = None

    def setUp(self) -> None:
        if self.test_connector is None:
            self.test_conf = {
                "server": "localhost",
                "port": self.rmq_instance.port,
                "users": {"mq_handler": {"user": "test_user",
                                         "password": "test_password"}}}
            import neon_mq_connector.utils.client_utils
            neon_mq_connector.utils.client_utils._default_mq_config = self.test_conf
            vhost = "/neon_testing"
            self.test_connector = SimpleMQConnector(config=self.test_conf,
                                                    service_name="mq_handler",
                                                    vhost=vhost)
            self.test_connector.register_consumer("neon_utils_test",
                                                  vhost,
                                                  INPUT_CHANNEL_A,
                                                  self.test_connector.respond,
                                                  auto_ack=False)
            self.test_connector.register_consumer("neon_utils_test_wrapped",
                                                  vhost,
                                                  INPUT_CHANNEL_B,
                                                  self.test_connector.respond_wrapped,
                                                  auto_ack=False)
            self.test_connector.run_consumers()

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.test_connector is not None:
            cls.test_connector.stop()

    def test_send_mq_request_valid(self):
        from neon_mq_connector.utils.client_utils import send_mq_request
        request = {"data": time.time()}
        response = send_mq_request("/neon_testing", request, INPUT_CHANNEL_A)
        self.assertIsInstance(response, dict)
        self.assertTrue(response["success"])
        self.assertEqual(response["request_data"], request["data"])

    def test_send_mq_request_spec_output_channel_valid(self):
        from neon_mq_connector.utils.client_utils import send_mq_request
        request = {"data": time.time()}
        response = send_mq_request("/neon_testing", request,
                                   INPUT_CHANNEL_A, OUTPUT_CHANNEL)
        self.assertIsInstance(response, dict)
        self.assertTrue(response["success"])
        self.assertEqual(response["request_data"], request["data"])

    def test_send_mq_request_response_emit_handled_by_create_mq_request_decorator(self):
        from neon_mq_connector.utils.client_utils import send_mq_request

        request = {"data": time.time()}
        response = send_mq_request("/neon_testing", request, INPUT_CHANNEL_B)
        self.assertIsInstance(response, dict)
        self.assertTrue(response["success"])
        self.assertEqual(response["request_data"], request["data"])

    def test_multiple_mq_requests(self):
        from neon_mq_connector.utils.client_utils import send_mq_request
        responses = dict()
        processes = []

        def check_response(name: str):
            request = {"data": time.time()}
            response = send_mq_request("/neon_testing", request, INPUT_CHANNEL_A)
            self.assertIsInstance(response, dict)
            if not isinstance(response, dict):
                responses[name] = {'success': False,
                                   'reason': 'Response is not a dict',
                                   'response': response}
                return
            if not response.get("success"):
                responses[name] = {'success': False,
                                   'reason': 'Response success flag not true',
                                   'response': response}
                return
            if response.get("request_data") != request["data"]:
                responses[name] = {'success': False,
                                   'reason': "Response data doesn't match request",
                                   'response': response}
                return
            responses[name] = {'success': True}

        for i in range(8):
            p = Thread(target=check_response, args=(str(i),))
            p.start()
            processes.append(p)

        for p in processes:
            p.join(60)

        self.assertEqual(len(processes), len(responses),
                         f"len(responses)={len(responses)}")
        for resp in responses.values():
            self.assertTrue(resp['success'], resp.get('reason'))

    def test_send_mq_request_invalid_vhost(self):
        from neon_mq_connector.utils.client_utils import send_mq_request
        with self.assertRaises(ValueError):
            send_mq_request("invalid_endpoint", {}, "test", "test", timeout=5)

    def test_connector_shutdown(self):
        connector = NeonMQHandler(config=self.test_conf,
                                  service_name="mq_handler",
                                  vhost="/neon_testing")
        self.assertTrue(connector.connection.is_open)
        connector.shutdown()
        self.assertTrue(connector.connection.is_closed)


@pytest.mark.usefixtures("rmq_instance")
class TestMQConnectionUtils(unittest.TestCase):
    test_conf = None
    counter = 0

    def setUp(self) -> None:
        self.counter = 0

        if self.test_conf is None:
            self.test_conf = {
                "server": "localhost",
                "port": self.rmq_instance.port,
                "users": {"mq_handler": {"user": "test_user",
                                         "password": "test_password"}}}
            import neon_mq_connector.utils.client_utils
            neon_mq_connector.utils.client_utils._default_mq_config = self.test_conf

    def repeating_method(self):
        """Simple method incrementing counter by one"""
        self.counter += 1

    @retry(num_retries=3, backoff_factor=0.1,
           callback_on_exceeded=callback_on_failure, use_self=True)
    def method_passing_on_nth_attempt(self, num_attempts: int = 3) -> bool:
        """
            Simple method that is passing check only after n-th attempt
            :param num_attempts: number of attempts before passing
        """
        if self.counter < num_attempts - 1:
            self.repeating_method()
            raise AssertionError(f'Awaiting counter equal to {num_attempts}')
        return True

    def test_get_timeout(self):
        """Tests of getting timeout with backoff factor applied"""
        __backoff_factor, __number_of_retries = 0.1, 1
        timeout = get_timeout(__backoff_factor, __number_of_retries)
        self.assertEqual(timeout, 0.1)
        __number_of_retries += 1
        timeout = get_timeout(__backoff_factor, __number_of_retries)
        self.assertEqual(timeout, 0.2)
        __number_of_retries += 1
        timeout = get_timeout(__backoff_factor, __number_of_retries)
        self.assertEqual(timeout, 0.4)

    def test_retry(self):
        # Retry with successful outcome
        outcome = self.method_passing_on_nth_attempt(num_attempts=3)
        self.assertTrue(outcome)
        self.assertEqual(2, self.counter)

        # Retry with failing outcome
        self.counter = 0
        outcome = self.method_passing_on_nth_attempt(num_attempts=4)
        self.assertFalse(outcome)
        self.assertEqual(3, self.counter)

        # Retry raises exception
        @retry(num_retries=1)
        def _retry_fails():
            raise Exception("This method is supposed to fail")

        with self.assertRaises(Exception) as e:
            _retry_fails()
        self.assertIsInstance(e.exception, RuntimeError)
        self.assertIn("_retry_fails", repr(e.exception))

    def test_wait_for_mq_startup(self):
        self.assertTrue(wait_for_mq_startup("mq.neonaiservices.com", 5672))
        self.assertFalse(wait_for_mq_startup("www.neon.ai", 5672, 1))

    def test_check_rmq_is_available(self):
        from neon_mq_connector.utils.connection_utils import check_rmq_is_available
        from pika.exceptions import ProbableAccessDeniedError
        from pika.credentials import PlainCredentials
        from pika.connection import ConnectionParameters

        valid_vhost = "/neon_testing"
        invalid_vhost = "/mock_vhost"
        base_connection_kwargs = {"host": self.test_conf['server'],
                                  "port": self.test_conf['port']}

        valid_creds = PlainCredentials("test_user",
                                       "test_password")
        invalid_creds = PlainCredentials("test_user",
                                         "invalid_password")

        valid_connection = ConnectionParameters(**base_connection_kwargs,
                                                virtual_host=valid_vhost,
                                                credentials=valid_creds)
        self.assertTrue(check_rmq_is_available(valid_connection))

        invalid_bad_vhost = ConnectionParameters(**base_connection_kwargs,
                                                 virtual_host=invalid_vhost,
                                                 credentials=valid_creds)
        with self.assertRaises(ProbableAccessDeniedError):
            self.assertFalse(check_rmq_is_available(invalid_bad_vhost))

        invalid_bad_creds = ConnectionParameters(**base_connection_kwargs,
                                                 virtual_host=valid_vhost,
                                                 credentials=invalid_creds)
        with self.assertRaises(ProbableAuthenticationError):
            self.assertFalse(check_rmq_is_available(invalid_bad_creds))

        # If the calling service doesn't specify a `vhost`, allow it to start
        # anyway (i.e. klat-observer)
        invalid_default_vhost = ConnectionParameters(**base_connection_kwargs,
                                                     virtual_host='/',
                                                     credentials=valid_creds)
        self.assertTrue(check_rmq_is_available(invalid_default_vhost))

    def test_supress_pika_logging(self):
        from neon_mq_connector.utils.connection_utils import SuppressPikaLogging
        pika_logger = logging.getLogger("pika")
        pika_logger.setLevel(logging.DEBUG)
        self.assertEqual(pika_logger.level, logging.DEBUG)

        # Normal Behavior
        with SuppressPikaLogging():
            self.assertEqual(pika_logger.level, logging.CRITICAL)
        self.assertEqual(pika_logger.level, logging.DEBUG)

        # With Exception
        try:
            with SuppressPikaLogging():
                self.assertEqual(pika_logger.level, logging.CRITICAL)
                raise RuntimeError("This is an exception")
        except RuntimeError:
            self.assertEqual(pika_logger.level, logging.DEBUG)

        # With extra changes
        with SuppressPikaLogging():
            self.assertEqual(pika_logger.level, logging.CRITICAL)
            pika_logger.setLevel(logging.INFO)
            self.assertEqual(pika_logger.level, logging.INFO)
        self.assertEqual(pika_logger.level, logging.DEBUG)


class TestConsumerUtils(unittest.TestCase):
    def test_default_error_handler(self):
        from neon_mq_connector.utils.consumer_utils import default_error_handler
        with self.assertRaises(Exception):
            default_error_handler()

        with self.assertRaises(Exception) as e:
            default_error_handler("error message")
            self.assertEqual(str(e.exception), "error message")


class TestNetworkUtils(unittest.TestCase):
    def test_dict_to_b64(self):
        b64_str = dict_to_b64(TEST_DICT)
        self.assertIsInstance(b64_str, bytes)
        self.assertTrue(len(b64_str) > 0)
        self.assertEqual(b64_str, TEST_DICT_B64)

    def test_b64_to_dict(self):
        result_dict = b64_to_dict(TEST_DICT_B64)
        self.assertIsInstance(result_dict, dict)
        self.assertTrue(len(list(result_dict)) > 0)
        self.assertEqual(result_dict, TEST_DICT)

    def test_check_port_is_open(self):
        from neon_mq_connector.utils.network_utils import check_port_is_open
        self.assertTrue(check_port_is_open("mq.neonaiservices.com", 5672))
        self.assertFalse(check_port_is_open("www.neon.ai", 5672))


class TestRabbitUtils(unittest.TestCase):

    @staticmethod
    def create_mock_request(body):
        return {
            "channel": Mock(),
            "method": Mock(),
            "properties": Mock(),
            "body": dict_to_b64(body)
        }

    def test_create_mq_callback(self):
        from neon_mq_connector.utils.rabbit_utils import create_mq_callback
        callback = Mock()
        test_body = {"test": True}
        valid_request = self.create_mock_request(body=test_body)
        mock_model = MockRequestModel(message_id="test_id")

        @create_mq_callback
        def default_handler_body(body: dict):
            callback(body)

        @create_mq_callback
        def default_handler_kwargs(**kwargs):
            callback(**kwargs)

        @create_mq_callback(include_callback_props=('body', 'method'))
        def extra_kwargs_handler(**kwargs):
            callback(**kwargs)

        @create_mq_callback(include_callback_props=())
        def no_kwargs_handler(**kwargs):
            callback(**kwargs)

        # Default handler
        default_handler_body(*valid_request.values())
        callback.assert_called_once_with(test_body)

        # Handler accepts kwargs
        default_handler_kwargs(*valid_request.values())
        callback.assert_called_with(body=test_body)

        # Handler accepts multiple kwargs
        extra_kwargs_handler(*valid_request.values())
        callback.assert_called_with(body=test_body,
                                    method=valid_request['method'])

        # Handler accepts no kwargs
        no_kwargs_handler(*valid_request.values())
        callback.assert_called_with()

        test_handlers = MqCallbackDecoratorClass()
        # Class handler with default args
        test_handlers.default_callback(*valid_request.values())
        test_handlers.callback.assert_called_once_with(test_body)

        # Class handler with no kwargs
        test_handlers.no_kwargs_callback(*valid_request.values())
        test_handlers.callback.assert_called_with()

        # Class staticmethod handler
        test_handlers.static_callback(*valid_request.values())
        test_handlers.class_callback.assert_called_once_with(test_body)

        # Pydantic model handler
        valid_model_request = self.create_mock_request(body=mock_model.model_dump())
        test_handlers.callback_with_pydantic_model(*valid_model_request.values())
        test_handlers.callback.assert_called_with(body=mock_model)

class TestThreadUtils(unittest.TestCase):
    counter = 0

    def setUp(self) -> None:
        self.counter = 0

    def repeating_method(self):
        """Simple method incrementing counter by one"""
        self.counter += 1

    def test_repeating_timer(self):
        """Testing repeating timer thread"""
        interval_timeout = 3
        timer_thread = RepeatingTimer(interval=0.9,
                                      function=self.repeating_method)
        timer_thread.start()
        time.sleep(interval_timeout)
        timer_thread.cancel()
        self.assertEqual(self.counter, 3)
