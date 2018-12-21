import os
import time
import sys
import traceback
import unittest
import subprocess
import threading


def import_all_packages():
    realpath = os.path.realpath(__file__)
    dirname = os.path.dirname(realpath)
    dirname_list = dirname.split('/')
    for index in range(len(dirname_list)):
        module_path = '/'.join(dirname_list[:index])
        try:
            sys.path.append(module_path)
        except:
            pass


import_all_packages()

w3c_logs = [
    "127.0.0.1 - james [09/May/2018:16:00:39 +0000] \"GET /report HTTP/1.0\" 200 123",
    "127.0.0.1 - jill [09/May/2018:16:00:41 +0000] \"GET /api/user HTTP/1.0\" 200 234",
    "127.0.0.1 - frank [09/May/2018:16:00:42 +0000] \"POST /api/user HTTP/1.0\" 200 34",
    "127.0.0.1 - mary [09/May/2018:16:00:42 +0000] \"POST /api/user HTTP/1.0\" 503 12",
    "127.0.0.1 - Joe [09/May/2018:16:00:42 +0000] \"POST /api/user HTTP/1.0\" 301 12",
    "127.0.0.1 - Jack [09/May/2018:16:00:42 +0000] \"PATCH /api/user HTTP/1.0\" 200 12",
    "127.0.0.1 - Fred [09/May/2018:16:00:42 +0000] \"POST /api/user HTTP/1.0\" 503 12",
    "127.0.0.1 - Justin [09/May/2018:16:00:42 +0000] \"PUT /api/user HTTP/1.0\" 503 12",
    "127.0.0.1 - Mark [09/May/2018:16:00:42 +0000] \"DELETE /api/user HTTP/1.0\" 200 12",
    "127.0.0.1 - james [09/May/2018:16:00:39 +0000] \"GET /report HTTP/1.0\" 200 123",
    "127.0.0.1 - jill [09/May/2018:16:00:41 +0000] \"GET /api/user HTTP/1.0\" 200 234",
    "127.0.0.1 - frank [09/May/2018:16:00:42 +0000] \"POST /api/user HTTP/1.0\" 200 34",
    "127.0.0.1 - mary [09/May/2018:16:00:42 +0000] \"POST /api/user HTTP/1.0\" 503 12",
    "127.0.0.1 - Joe [09/May/2018:16:00:42 +0000] \"POST /api/user HTTP/1.0\" 301 12",
    "127.0.0.1 - Jack [09/May/2018:16:00:42 +0000] \"PATCH /api/user HTTP/1.0\" 200 12",
    "127.0.0.1 - Fred [09/May/2018:16:00:42 +0000] \"POST /api/user HTTP/1.0\" 503 12",
    "127.0.0.1 - Justin [09/May/2018:16:00:42 +0000] \"PUT /api/user HTTP/1.0\" 503 12",
    "127.0.0.1 - Mark [09/May/2018:16:00:42 +0000] \"DELETE /api/user HTTP/1.0\" 200 12",
]


class TestHTTPTrafficMonitor(unittest.TestCase):
    w3c_file_name = "/var/log/access.log"

    def setUp(self):
        os.environ["broker_name_key"] = "localhost:9092"

    @staticmethod
    def analyze_w3c_logs():
        print("Starting {}".format(threading.current_thread().getName()))
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            t = threading.currentThread()
        print("Thread {}: Exiting"
              .format(threading.current_thread().getName()))

    @staticmethod
    def write_w3c_logs(*args, **kwargs):
        print("Starting {}".format(threading.current_thread().getName()))
        t = threading.currentThread()
        number_of_messages_per_second = 0
        sleep_time = 0
        for name, value in kwargs.items():
            print("name={},value={}".format(name, value))
            if name == 'number_of_messages_per_second':
                number_of_messages_per_second = value
            elif name == 'sleep_time':
                sleep_time = value
        current_index = 0
        while getattr(t, "do_run", True):
            t = threading.currentThread()
            """
            Write w3c formatted logs into /var/log/access.log
            Example:
            127.0.0.1 - james [09/May/2018:16:00:39 +0000] "GET /report HTTP/1.0" 200 123
            """
            for index in range(number_of_messages_per_second):
                with open(TestHTTPTrafficMonitor.w3c_file_name) as f:
                    f.write(w3c_logs[current_index])
                if current_index == len(w3c_logs) - 1:
                    current_index = 0
                else:
                    current_index += 1
                time.sleep(sleep_time)
        print("Thread {}: Exiting"
              .format(threading.current_thread().getName()))

    def create_w3c_log_producer_thread(self,
                                       number_of_messages_per_second,
                                       sleep_time):
        self.w3c_log_producer_thread = None
        self.w3c_log_producer_thread = threading.Thread(name="w3c_log_producer_thread",
                                                        target=TestHTTPTrafficMonitor.write_w3c_logs,
                                                        args=(),
                                                        kwargs={
                                                            'number_of_messages_per_second': number_of_messages_per_second,
                                                            'sleep_time': sleep_time}
                                                        )
        self.w3c_log_producer_thread.do_run = True
        self.w3c_log_producer_thread.name = "w3c_log_producer_thread"
        self.w3c_log_producer_thread.start()

    def validate_historic_stats(self, raise_alarm=False):
        with open("../historic_stats.txt") as f:
            data = f.read()
            if raise_alarm:
                if 'High traffic generated an alert' not in data:
                    return False
            else:
                if 'Clearing the alert' not in data:
                    return False
        return True

    def validate_current_stats(self):
        with open("../current_stats.txt") as f:
            data = f.read()
            if 'report HTTP' not in data:
                return False
            if 'api' not in data:
                return False
        return True

    def test_run(self):
        print("Starting unit testing of HTTP Traffic monitor.")
        self.create_w3c_log_producer_thread(5, 1)
        for index in range(12):
            self.assertTrue(self.validate_current_stats())
            time.sleep(10)
        time.sleep(10)
        self.assertTrue(self.validate_historic_stats(raise_alarm=True))
        self.w3c_log_producer_thread.do_run = False
        self.w3c_log_producer_thread.join(1.0)
        if self.w3c_log_producer_thread.is_alive():
            print("Unable to join w3c_log_producer_thread.")
            raise BaseException
        time.sleep(120)
        self.assertTrue(self.validate_historic_stats(raise_alarm=False))

    def tearDown(self):
        pass
