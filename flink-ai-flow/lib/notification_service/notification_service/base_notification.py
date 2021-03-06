#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#
import abc
import time

from typing import List

UNDEFINED_EVENT_TYPE = "UNDEFINED"


class BaseEvent(object):
    def __init__(self, key: str, value: str, event_type: str = UNDEFINED_EVENT_TYPE,
                 version: int = None, create_time: int = None, id: int = None):
        self.key = key
        self.value = value
        self.event_type = event_type
        self.version = version
        self.create_time = create_time
        self.id = id

    def __str__(self) -> str:
        return 'key:{0}, value:{1}, type:{2}, version:{3}, create_time:{4}, id: {5}' \
            .format(self.key, self.value, self.event_type, self.version, self.create_time, self.id)


class EventWatcher(metaclass=abc.ABCMeta):
    """
    SignalWatcher is used to represent a standard event handler, which defines the
    logic related to signal notifications.
    """

    @abc.abstractmethod
    def process(self, events: List[BaseEvent]):
        pass


class BaseNotification(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def send_event(self, event: BaseEvent) -> BaseEvent:
        """
        Send event to Notification
        :param event: the event updated.
        :return: A single object of Event created in Notification.
        """
        pass

    @abc.abstractmethod
    def list_events(self, key: str, version: int = None) -> list:
        """
        List specific `key` or `version` of events in Notification Service.
        :param key: Key of the event for listening.
        :param version: (Optional) Version of the signal for listening.
        :return: Specific `key` or `version` event notification list.
        """
        pass

    @abc.abstractmethod
    def start_listen_event(self, key: str, watcher: EventWatcher, version: int = None):
        """
        Start listen specific `key` or `version` notifications in Notification Service.

        :param key: Key of notification for listening.
        :param watcher: Watcher instance for listening notification.
        :param version: (Optional) Version of notification for listening.
        """
        pass

    @abc.abstractmethod
    def stop_listen_event(self, key: str = None):
        """
        Stop listen specific `key` notifications in Notification Service.

        :param key: Key of notification for listening.
        """
        pass

    @abc.abstractmethod
    def list_all_events(self, start_time: int):
        """
        List specific `key` or `version` of events in Notification Service.
        :param start_time: the event after this time.
        :return:
        """
        pass

    @abc.abstractmethod
    def start_listen_events(self, watcher: EventWatcher, start_time=time.time_ns()):
        """
        start listen all events.
        :param watcher: process event.
        :param start_time: the earliest event time.
        :return:
        """
        pass

    @abc.abstractmethod
    def stop_listen_events(self):
        """
        stop listen the events
        :return:
        """
        pass
