import os
import time
import sys
import unittest
import threading
import subprocess
import traceback

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

from http_traffic_monitor.http_log_analyzer.http_log_analyzer import HTTPLogAnalyzer

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
        os.environ["log_file_name_key"] = "/var/log/access.log"
        os.environ["output_current_stats_file_name_key"] = "../current_stats.txt"
        os.environ["output_alarms_events_file_name_key"] = "../historic_stats.txt"
        os.environ["stats_time_interval_key"] = "10"
        os.environ["threshold_key"] = "10"
        os.environ["event_timer_val_key"] = "120"
        os.environ["web_server_port_key"] = "8085"
        self.w3c_log_producer_thread = None
        self.w3c_analyzer_thread = None

    @staticmethod
    def analyze_w3c_logs():
        print("Starting {}".format(threading.current_thread().getName()))
        try:
            t = threading.currentThread()
            web_server = HTTPLogAnalyzer()
            time.sleep(1)
            while getattr(t, "do_run", True):
                t = threading.currentThread()
                web_server.analyze_w3c_http_logs()
        except KeyboardInterrupt:
            print('^C received, shutting down.')
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
                f = open(TestHTTPTrafficMonitor.w3c_file_name, 'a')
                f.write(w3c_logs[current_index]+'\n')
                if current_index == len(w3c_logs) - 1:
                    current_index = 0
                else:
                    current_index += 1
                f.close()
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

    def create_w3c_analyzer_thread(self):
        self.w3c_analyzer_thread = None
        self.w3c_analyzer_thread = threading.Thread(name="w3c_analyzer_thread",
                                                    target=TestHTTPTrafficMonitor.analyze_w3c_logs,
                                                    )
        self.w3c_analyzer_thread.do_run = True
        self.w3c_analyzer_thread.name = "w3c_analyzer_thread"
        self.w3c_analyzer_thread.start()

    def validate_historic_stats(self, raise_alarm=False):
        try:
            with open("../historic_stats.txt") as f:
                data = f.read()
                if raise_alarm:
                    if 'High traffic generated an alert' not in data:
                        return False
                else:
                    if 'Clearing the alert' not in data:
                        return False
            return True
        except FileNotFoundError:
            return True
        except:
            print("Exception in user code:")
            print("Unhandled exception {}.".format(sys.exc_info()[0]))
            print("-" * 60)
            traceback.print_exc(file=sys.stdout)
            print("-" * 60)
            return False

    def validate_current_stats(self):
        try:
            with open("../current_stats.txt") as f:
                data = f.read()
                if 'report HTTP' not in data:
                    return False
                if 'api' not in data:
                    return False
            return True
        except FileNotFoundError:
            return True
        except:
            print("Exception in user code:")
            print("Unhandled exception {}.".format(sys.exc_info()[0]))
            print("-" * 60)
            traceback.print_exc(file=sys.stdout)
            print("-" * 60)
            return False

    def test_run(self):
        print("Starting unit testing of HTTP Traffic monitor.")
        self.create_w3c_log_producer_thread(10, 10)
        self.create_w3c_analyzer_thread()
        time.sleep(1)
        for index in range(12):
            self.assertTrue(self.validate_current_stats())
            time.sleep(10)
        self.assertTrue(self.validate_historic_stats(raise_alarm=True))
        self.w3c_log_producer_thread.do_run = False
        self.w3c_log_producer_thread.join(1.0)
        time.sleep(10)
        if self.w3c_log_producer_thread.is_alive():
            print("Unable to join w3c_log_producer_thread.")
            raise BaseException
        time.sleep(150)
        self.assertTrue(self.validate_historic_stats(raise_alarm=False))

    def tearDown(self):
        completedProcess = subprocess.run(["rm",
                                           "-f",
                                           "../current_stats.txt"],
                                          stdout=subprocess.PIPE)
        print(completedProcess.stdout)
        completedProcess = subprocess.run(["rm",
                                           "-f",
                                           "../historic_stats.txt"],
                                          stdout=subprocess.PIPE)
        print(completedProcess.stdout)

        completedProcess = subprocess.run(["killall",
                                           "pidof",
                                           "/usr/bin/python3.5"],
                                          stdout=subprocess.PIPE)
        print(completedProcess.stdout)


if __name__ == "__main__":
    try:
        unittest.main()
    except:
        print("Exception in user code:")
        print("-" * 60)
        traceback.print_exc(file=sys.stdout)
        print("-" * 60)
