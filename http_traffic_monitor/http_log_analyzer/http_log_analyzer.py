#!/usr/bin/python

import os
import sys
import time
from collections import defaultdict, deque
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
            print(module_path)
            sys.path.append(module_path)
        except:
            pass


import_all_packages()

from http_webserver.http_web_server import HTTPWebServerDumpStats

"""
This is a singleton class.
This class creates two threads.
Thread 1. Instantiates web server on port 8080 for displaying
          a. Current 10 second statistics of the HTTP traffic.
          b. Historic statistics of alarms and events.
Thread 2.  a. Used for computing two minute average of all the 10 second hits.
           The sampling rate is 120//10 = 12 samples.
           b. This thread raises an alarm if it finds that the 2 min average of hits 
           exceeds the threshold limit.
           
"""


class HTTPLogAnalyzer:
    HTTP_VERBS = ['GET', 'PUT', 'POST', 'PATCH', 'DELETE']
    # Singleton. Used in fetching the two_minute_hit_counts from a thread.
    __instance = None

    def __new__(cls):
        if not HTTPLogAnalyzer.__instance:
            HTTPLogAnalyzer.__instance = object.__new__(cls)
        return HTTPLogAnalyzer.__instance

    @staticmethod
    def get_hit_counts():
        return HTTPLogAnalyzer.__instance.__hit_counts

    @staticmethod
    def get_max_number_of_samples():
        return HTTPLogAnalyzer.__instance.__max_number_of_samples

    @staticmethod
    def get_stats_time_interval():
        return HTTPLogAnalyzer.__instance.__stats_time_interval

    @staticmethod
    def get_threshold_limit():
        return HTTPLogAnalyzer.__instance.__threshold

    @staticmethod
    def get_output_alarms_events_file_name():
        return HTTPLogAnalyzer.__instance.__output_alarms_events_file_name

    @staticmethod
    def get_current_output_stats_file_name():
        return HTTPLogAnalyzer.__instance.__output_current_stats_file_name

    @staticmethod
    def get_web_server_listening_port():
        return HTTPLogAnalyzer.__instance.__web_server_port

    def __init__(self):
        self.__log_file_name = "/var/log/access.log"
        self.__output_current_stats_file_name = "current_stats.txt"
        self.__output_alarms_events_file_name = "historic_stats.txt"
        self.__stats_time_interval = 10
        self.__threshold = 10
        self.__event_timer_val = 120
        self.__http_output_webserver_thread = None
        self.__event_monitor_thread = None
        self.__cached_stamp = 0
        self.__log_file_size = 0
        self.__last_read_file_position = 0
        self.__section_to_hit_dict = defaultdict(int)
        self.__hit_counts = deque()
        self.__web_server_port = 8080
        # Read the environment variables.
        self.__read_environment_variables()
        # Default: Max number of samples is 120//10 = 12
        self.__max_number_of_samples = self.__event_timer_val // self.__stats_time_interval

        # 1. Create a web server thread to display the output stats.
        self.__create_http_webserver_thread()
        # 2. Create a two minute event alarm generator thread.
        self.__create_event_monitor_thread()

    def __read_environment_variables(self):
        self.__log_file_name = os.getenv("log_file_name_key",
                                         default="/var/log/access.log")

        self.__output_current_stats_file_name = os.getenv("output_current_stats_file_name_key",
                                                          default="current_stats.txt")

        self.__output_alarms_events_file_name = os.getenv("output_alarms_events_file_name_key",
                                                          default="historic_stats.txt")

        self.__stats_time_interval = int(os.getenv("stats_time_interval_key",
                                                   default="10"))

        self.__threshold = int(os.getenv("threshold_key",
                               default="10"))
        self.__event_timer_val = int(os.getenv("event_timer_val_key",
                                     default="120"))

        self.__web_server_port = int(os.getenv("web_server_port_key",
                                     default="8085"))

    def cleanup(self):
        # Not used. Need to force kill the python3 process.
        completedProcess = subprocess.run(["killall",
                                           "pidof",
                                           "/usr/bin/python3.5"],
                                          stdout=subprocess.PIPE)
        print(completedProcess.stdout)

    @staticmethod
    def write_historic_stats_to_output(event):
        # 1. Open the output file in append mode to append to the existing content.
        f = open(HTTPLogAnalyzer.get_output_alarms_events_file_name(), 'a')
        # 2. Prepare a heading that says current resource section to hits.
        # f.write("Historic events and alarms of resource_section to Hit count.\n")
        # f.write("***********************************************************.\n")
        f.write(event + '\n')
        f.close()

    @staticmethod
    def monitor_threshold_and_raise_alarms(sleep_time):
        is_alarm_raised = False
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            time.sleep(sleep_time)
            t = threading.currentThread()
            # compute the sum of all the 10 second hit counts.
            total_hit_counts = sum(HTTPLogAnalyzer.get_hit_counts())
            average_of_total_hits = total_hit_counts // HTTPLogAnalyzer.get_max_number_of_samples()
            print("Average of total_hits = {}"
                  .format(average_of_total_hits))
            # raise an alarm event if the total_hit_counts exceed total_max_threshold.
            if average_of_total_hits >= HTTPLogAnalyzer.get_threshold_limit():
                # skip redundant alarm generation if there is already an existing alarm.
                if is_alarm_raised:
                    continue
                print("Raising an alarm as average of hit counts {} "
                      "is greater than average threshold {}"
                      .format(average_of_total_hits,
                              HTTPLogAnalyzer.get_threshold_limit()))

                localtime = time.asctime(time.localtime(time.time()))

                HTTPLogAnalyzer.__instance.write_historic_stats_to_output(
                    "High traffic generated an alert - hits = {}, triggered at {} "
                    .format(total_hit_counts, localtime))
                is_alarm_raised = True
            elif is_alarm_raised:
                is_alarm_raised = False
                print(
                    "Clearing the alarm as average hit count {} is "
                    "less than the threshold {}"
                    .format(average_of_total_hits,
                            HTTPLogAnalyzer.get_threshold_limit()))

                localtime = time.asctime(time.localtime(time.time()))

                HTTPLogAnalyzer.__instance.write_historic_stats_to_output(
                    "Clearing the alert at {} "
                    "as average hit count {} is "
                    "less than the threshold {}"
                    .format(localtime,
                            average_of_total_hits,
                            HTTPLogAnalyzer.get_threshold_limit()))

    """
    Thread 2.  a. Used for computing two minute average of all the 10 second hits.
           The sampling rate is 120//10 = 12 samples.
           b. This thread raises an alarm if it finds that the 2 min average of hits 
           exceeds the threshold limit.
    """
    @staticmethod
    def run_event_monitor(*args, **kwargs) -> object:
        print("Starting {}".format(threading.current_thread().getName()))
        # 1. Read the Thread arguments.
        sleep_time = 0
        for name, value in kwargs.items():
            print("name={},value={}".format(name, value))
            if name == 'sleep_time':
                sleep_time = value
        try:
            HTTPLogAnalyzer.monitor_threshold_and_raise_alarms(sleep_time)
        except:
            print("Exception in user code:")
            print("Unhandled exception {}.".format(sys.exc_info()[0]))
            print("-" * 60)
            traceback.print_exc(file=sys.stdout)
            print("-" * 60)

        print("Exiting {}".format(threading.current_thread().getName()))

    def __create_event_monitor_thread(self):
        if self.__event_monitor_thread:
            print("Event monitor thread is already started.")
            return
        self.__event_monitor_thread = threading.Thread(name="two_minute_event_monitor_thread",
                                                       target=HTTPLogAnalyzer.run_event_monitor,
                                                       args=(),
                                                       kwargs={'sleep_time': self.__event_timer_val})
        self.__event_monitor_thread.do_run = True
        self.__event_monitor_thread.name = "http_output_webserver_thread"
        self.__event_monitor_thread.start()
        time.sleep(1)
    """
    Thread 1. Instantiates web server on port 8080 for displaying
          a. Current 10 second statistics of the HTTP traffic.
          b. Historic statistics of alarms and events.
    """
    @staticmethod
    def run_webserver() -> object:
        print("Starting {}".format(threading.current_thread().getName()))
        t = threading.currentThread()
        server = HTTPWebServerDumpStats(HTTPLogAnalyzer.get_current_output_stats_file_name(),
                                        HTTPLogAnalyzer.get_output_alarms_events_file_name(),
                                        HTTPLogAnalyzer.get_web_server_listening_port())
        while getattr(t, "do_run", True):
            t = threading.currentThread()
            server.listen_for_connections()
        print("Exiting {}".format(threading.current_thread().getName()))

    def __create_http_webserver_thread(self):
        if self.__http_output_webserver_thread:
            print("Webserver thread is already started.")
            return

        self.__http_output_webserver_thread = threading.Thread(name="http_output_webserver_thread",
                                                               target=HTTPLogAnalyzer.run_webserver)
        self.__http_output_webserver_thread.do_run = True
        self.__http_output_webserver_thread.name = "http_output_webserver_thread"
        self.__http_output_webserver_thread.start()
        time.sleep(1)

    def __compute_aggregate_hit_count(self):
        # 1. Compute the sum of all the 120/10 = 12 samples.
        cumulative_sum_of_hits = sum(self.__section_to_hit_dict.values())
        # 2. Add it to the tail of the hit count list.
        self.__hit_counts.append(cumulative_sum_of_hits)
        # 3. Slide the window to the left by one if it is full. (12 values)
        if len(self.__hit_counts) > self.__max_number_of_samples:
            self.__hit_counts.popleft()
        #print(self.__hit_counts)

    def __locate_pattern_in_log_entry(self,
                                      log_entry,
                                      search_input,
                                      starting_index=0):
        index_of_search_input = -1

        if type(search_input) is list:
            # 1. For each HTTP verb try to find it in the log_entry and return the index.
            for item in search_input:
                if item in log_entry:
                    index_of_search_input = log_entry.find(item, starting_index)
        elif type(search_input) is str:
            # 2. Try to locate the index of the passed in search_input and return the index.
            index_of_search_input = log_entry.find(search_input, starting_index)
        return index_of_search_input

    def __consume_and_process_log_entry(self, log_entry):
        is_successful = False
        """
        parse the log_entry.
        A section is defined as being what's before the second '/' 
        in the resource section of the log line. 
        For example, the section for "/pages/create" is "/pages"
        """
        # 1. Locate the HTTP verbs in the log entry.
        http_verb_location = self.__locate_pattern_in_log_entry(log_entry,
                                                                HTTPLogAnalyzer.HTTP_VERBS)
        if http_verb_location == -1:
            print("Skipping log {} because because the http verb is not found."
                  .format(log_entry))
            return is_successful

        # 2. Locate the first '/' after HTTP verb.
        first_back_slash_location = self.__locate_pattern_in_log_entry(log_entry,
                                                                     '/',
                                                                       http_verb_location)
        if first_back_slash_location == -1:
            print("Skipping log {} because because '/' is not found after HTTP verb."
                  .format(log_entry))
            return is_successful

        # 3. Locate second '/' after HTTP verb.
        second_back_slash_location = self.__locate_pattern_in_log_entry(log_entry,
                                                                      '/',
                                                                        first_back_slash_location + 1)
        if second_back_slash_location == -1:
            print("Skipping log {} because because second '/' is not found after HTTP verb."
                  .format(log_entry))
            return is_successful

        # 4. Resource section is what is found between the first and second '/'
        resource_section = log_entry[first_back_slash_location + 1:
                                     second_back_slash_location]

        if not len(resource_section):
            print("unable to find a resource in the resource section")
            return is_successful

        # 5. Bump up the hit count.
        self.__section_to_hit_dict[resource_section] += 1

        return is_successful

    def __read_data_from_file(self):
        try:
            # 1. Open the file in read only mode.
            file = open(self.__log_file_name, 'r')
            # 2. Seek the last read position in the file.
            file.seek(self.__last_read_file_position)
            # 3. For every line in the file, return it back to the caller.
            for line in file:
                yield line
            # 4. Record the last read file position so that
            #    you read it from that position after sleeping for stats_time_interval.
            self.__last_read_file_position = file.tell()
            file.close()
        except:
            print("Unhandled exception {}.".format(sys.exc_info()[0]))
            print("Caught an exception while opening file {}."
                  .format(self.__log_file_name))

    def __is_file_modified(self):
        is_modified = False
        # 1. Compute the current time stamp.
        stamp = os.stat(self.__log_file_name).st_mtime
        if stamp != self.__cached_stamp:
            # 2. Someone touched this file.
            self.__cached_stamp = stamp
            # 3. Compute the file size.
            file_size = os.stat(self.__log_file_name).st_size
            if file_size < self.__log_file_size:
                # 4. "Log rotation happened. Reset the last read position to 0."
                self.__last_read_file_position = 0
            # File has changed, so do something...
            self.__log_file_size = file_size
            is_modified = True
        return is_modified

    def __write_the_current_stats_to_output(self):
        # 1. Open the output file in write mode to overwrite all the content.
        f = open(self.__output_current_stats_file_name, 'w')
        # 2. Prepare a heading that says current resource section to hits.
        f.write("{} second aggregate of resource_section to Hit count.\n"
                .format(self.__stats_time_interval))
        f.write("****************************************************.\n")
        f.write("{0:40s} ==> {1:10s}.\n".format("Resource_section", "Hits"))
        f.write("********************************************************.\n")
        for key, value in self.__section_to_hit_dict.items():
            f.write("{0:40s} ==> {1:10d}.\n".format(key, value))
        current_sum_of_hits = sum(self.__section_to_hit_dict.values())
        f.write("Total sum of all the hits = {}."
                .format(current_sum_of_hits))
        if current_sum_of_hits > self.__hit_counts[-1]:
            f.write("There has been a sudden increase of "
                    "web traffic of {} hits in the past {} seconds."
                    .format(current_sum_of_hits-self.__hit_counts[-1],
                            self.__stats_time_interval))
        elif current_sum_of_hits == self.__hit_counts[-1]:
            f.write("There has been a constant flow of "
                    "web traffic of {} hits every {} seconds."
                    .format(current_sum_of_hits,
                            self.__stats_time_interval))
        else:
            f.write("There has been a sudden decrease of "
                    "web traffic of {} hits in the past {} seconds."
                    .format(self.__hit_counts[-1]-current_sum_of_hits,
                            self.__stats_time_interval))
        f.close()

    def __cleanup_section_to_hit_dict(self):
        del self.__section_to_hit_dict
        self.__section_to_hit_dict = defaultdict(int)

    def analyze_w3c_http_logs(self):
        try:
            # 3. If the input file is modified, then consume it.
            if self.__is_file_modified():
                # 4. For each new log entry read from the input file, consume it.
                for log_entry in self.__read_data_from_file():
                    if log_entry is None or log_entry == b'' or len(log_entry) == 0:
                        continue
                    self.__consume_and_process_log_entry(log_entry)
            # 5. Compute the aggregate hit counts of all the Resources found.
            self.__compute_aggregate_hit_count()
            # 6. Over write the output file with the latest stats.
            self.__write_the_current_stats_to_output()
            # 7. Clean up the dict of resources to hits.
            self.__cleanup_section_to_hit_dict()
            # 8. Sleep for the stipulated time interval.
            time.sleep(self.__stats_time_interval)
        except:
            print("Exception in user code:")
            print("Unhandled exception {}.".format(sys.exc_info()[0]))
            print("-" * 60)
            traceback.print_exc(file=sys.stdout)
            print("-" * 60)


if __name__ == "__main__":
    try:
        web_server = HTTPLogAnalyzer()
        while True:
            web_server.analyze_w3c_http_logs()
    except KeyboardInterrupt:
        print('^C received, shutting down.')
    except:
        print("Exception in user code:")
        print("Unhandled exception {}.".format(sys.exc_info()[0]))
        print("-" * 60)
        traceback.print_exc(file=sys.stdout)
        print("-" * 60)

