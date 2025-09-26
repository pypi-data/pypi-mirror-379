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
import inspect
import logging
import time

from threading import Event
from typing import Union, Callable, Optional
from ovos_utils.log import LOG
from pika.adapters.blocking_connection import BlockingConnection
from pika.connection import ConnectionParameters
from pika.exceptions import IncompatibleProtocolError, ProbableAccessDeniedError

from neon_mq_connector.utils.network_utils import check_port_is_open


def get_timeout(backoff_factor: float, number_of_retries: int) -> float:
    """
        Gets timeout based on backoff_factor

        :param backoff_factor: value of backoff factor
        :param number_of_retries: current number of retries made

        Examples:
            >>> __backoff_factor, __number_of_retries = 0.1, 1
            >>> timeout = get_timeout(__backoff_factor, __number_of_retries)
            >>> assert timeout == 0.1
            >>>
            >>> __backoff_factor, __number_of_retries = 0.1, 2
            >>> timeout = get_timeout(__backoff_factor, __number_of_retries)
            >>> assert timeout == 0.2
    """
    return backoff_factor * (2 ** (number_of_retries - 1))


def retry(callback_on_exceeded: Union[str, Callable] = None,
          callback_on_attempt_failure: Union[str, Callable] = None,
          num_retries: int = 3, backoff_factor: float = 5,
          use_self: bool = False,
          callback_on_attempt_failure_args: list = None,
          callback_on_exceeded_args: list = None):
    """
        Decorator for generic retrying function execution

        :param use_self: to call a function from current class instance
            (defaults to False)
        :param num_retries: num of retries for function execution
        :param callback_on_exceeded: function to call when all attempts fail
        :param callback_on_exceeded_args: args for :param callback_on_exceeded
        :param callback_on_attempt_failure: function to call when a single
            attempt fails
        :param callback_on_attempt_failure_args: args for
            callback_on_attempt_failure
        :param backoff_factor: value of backoff factor for setting delay between
            function execution retry, refer to "get_timeout()" for details
    """
    # TODO: given function shows non-thread-safe behaviour for Consumer Thread,
    #       need to fix this before using
    if not callback_on_attempt_failure_args:
        callback_on_attempt_failure_args = []
    if not callback_on_exceeded_args:
        callback_on_exceeded_args = []

    def decorator(function):
        def wrapper(*args, **kwargs):
            signature = inspect.signature(function).parameters
            self = args[0] if 'self' in signature else None
            if self:
                args = args[1:]
            with_self = use_self and self
            num_attempts = 1
            error_body = f"{function.__name__}(args={args}, kwargs={kwargs})"
            if with_self:
                error_body = f'{self.__class__.__name__}.{error_body}'
            while num_attempts <= num_retries:
                if num_attempts > 1:
                    LOG.debug(f'Retrying {error_body} execution. '
                              f'Attempt #{num_attempts}')
                try:
                    if with_self:
                        return_value = function(self, *args, **kwargs)
                    else:
                        return_value = function(*args, **kwargs)
                    if num_attempts > 1:
                        call_frame = inspect.currentframe().f_back.f_back
                        info = inspect.getframeinfo(call_frame)
                        LOG.info(
                            f"{error_body} succeeded on try #{num_attempts}\n"
                            f"{info.filename}:{info.function}:{info.lineno}")
                    return return_value
                except Exception as e:
                    for i in range(len(callback_on_attempt_failure_args)):
                        if callback_on_attempt_failure_args[i] == 'e':
                            callback_on_attempt_failure_args[i] = e
                        elif callback_on_attempt_failure_args[i] == 'self':
                            callback_on_attempt_failure_args[i] = self
                    try:
                        if callback_on_attempt_failure:
                            if with_self and \
                                    isinstance(callback_on_attempt_failure,
                                               str):
                                getattr(self, callback_on_attempt_failure)(
                                    *callback_on_attempt_failure_args)

                            elif isinstance(callback_on_attempt_failure,
                                            Callable):
                                callback_on_attempt_failure(
                                    *callback_on_attempt_failure_args)
                    except Exception as ex:
                        LOG.error(f'Failed to execute '
                                  f'callback_on_attempt_failure function '
                                  f'{callback_on_attempt_failure.__name__}('
                                  f'{callback_on_attempt_failure_args}) - {ex}')
                    sleep_timeout = get_timeout(backoff_factor=backoff_factor,
                                                number_of_retries=num_attempts)
                    LOG.warning(f'{error_body}: {e}.')
                    LOG.debug(f'Timeout for {sleep_timeout} secs')
                    num_attempts += 1
                    time.sleep(sleep_timeout)
            LOG.error(f'Failed to execute after {num_retries} attempts')
            if callback_on_exceeded:
                if with_self and isinstance(callback_on_exceeded, str):
                    return getattr(self, callback_on_exceeded)(
                        *callback_on_exceeded_args)
                elif isinstance(callback_on_exceeded, Callable):
                    return callback_on_exceeded(*callback_on_exceeded_args)
            else:
                raise RuntimeError(f"Ran out of retries for {function}")

        return wrapper
    return decorator


def wait_for_mq_startup(addr: str, port: int, timeout: int = 60,
                        connection_params: Optional[ConnectionParameters] = None
                        ) -> bool:
    """
    Wait up to `timeout` seconds for the MQ connection at `addr`:`port`
    to come online.
    :param addr: URL or IP address to monitor
    :param port: MQ port to query
    :param timeout: Max seconds to wait for connection to come online
    """
    stop_time = time.time() + timeout
    LOG.debug(f"Waiting for MQ server at {addr}:{port} to come online")
    while not check_port_is_open(addr, port):
        if time.time() > stop_time:
            LOG.warning(f"Timed out waiting for port to open after {timeout}s")
            return False
    LOG.info("Waiting for RMQ broker to load")
    if connection_params:
        waiter = Event()
        rmq_ready = True
        while not check_rmq_is_available(connection_params):
            rmq_ready = False
            if time.time() > stop_time:
                LOG.warning(f"Timed out waiting for RMQ after {timeout}s")
                return False
            waiter.wait(5)
        if not rmq_ready:
            LOG.info("MQ just started. Wait some time for queues, etc. to load")
            waiter.wait(15)
    LOG.info("MQ Server Started")
    return True


def check_rmq_is_available(
        connection_params: Optional[ConnectionParameters]) -> bool:
    """
    Check if an RMQ broker is accessible at the specified Connection
    :param connection_params: ConnectionParameters object to try and connect to
    :return: True if the requested connection is successful, else False
    """
    with SuppressPikaLogging():
        success = False
        try:
            connection = BlockingConnection(connection_params)
            connection.close()
            success = True
        except IncompatibleProtocolError as e:
            LOG.debug(f"RMQ is likely still starting up (e={e})")
        except ProbableAccessDeniedError as e:
            if connection_params.virtual_host == '/':
                LOG.warning(f"Access was denied to default vhost='/'. Assuming RMQ "
                            f"broker is online.")
                success = True
            else:
                raise e
    return success


class SuppressPikaLogging:
    """
    Helper to temporarily suppress pika logging
    """
    _pika_log = logging.getLogger("pika")

    def __init__(self):
        self._pika_level = self._pika_log.getEffectiveLevel()

    def __enter__(self):
        self._pika_log.setLevel(logging.CRITICAL)

    def __exit__(self, *_):
        self._pika_log.setLevel(self._pika_level)
