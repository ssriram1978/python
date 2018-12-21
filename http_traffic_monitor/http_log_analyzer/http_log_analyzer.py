#!/usr/bin/python

import os
import sys
import time
from collections import defaultdict, deque
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

from http_traffic_monitor.http_webserver.http_web_server import HTTPWebServerDumpStats


class HTTPLogAnalyzer:
    TWO_MINUTE_INTERVAL = 120
    HTTP_VERBS = ['GET', 'PUT', 'POST', 'PATCH', 'DELETE']
    # Singleton. Used in fetching the two_minute_hit_counts from a thread.
    __instance = None

    def __new__(cls):
        if not HTTPLogAnalyzer.__instance:
            HTTPLogAnalyzer.__instance = object.__new__(cls)
        return HTTPLogAnalyzer.__instance

    @staticmethod
    def get_two_minute_hit_counts():
        return HTTPLogAnalyzer.__instance.__two_minute_hit_counts

    @staticmethod
    def get_stats_time_interval():
        return HTTPLogAnalyzer.__instance.__stats_time_interval

    @staticmethod
    def get_output_alarms_events_file_name():
        return HTTPLogAnalyzer.__instance.__output_alarms_events_file_name

    def __init__(self):
        self.__log_file_name = "/var/log/access.log"
        self.__output_current_stats_file_name = "../current_stats.txt"
        self.__output_alarms_events_file_name = "../historic_stats.txt"
        self.__stats_time_interval = 10
        self.__threshold = 10
        self.__http_output_webserver_thread = None
        self.__two_minute_event_monitor_thread = None
        self.__cached_stamp = 0
        self.__log_file_size = 0
        self.__last_read_file_position = 0
        self.__section_to_hit_dict = defaultdict(int)
        self.__two_minute_hit_counts = deque()

        self.__read_environment_variables()
        # 1. Create a web server thread to display the output stats.
        self.__create_http_webserver_thread()
        # 2. Create a two minute event alarm generator thread.
        self.__create_two_minute_event_monitor_thread()

    def __read_environment_variables(self):
        pass

    def cleanup(self):
        self.__http_output_webserver_thread.join(1.0)
        if self.__http_output_webserver_thread.is_alive():
            print("Unable to force stop a thread.")
            raise BaseException
        self.__two_minute_event_monitor_thread.join(1.0)
        if self.__two_minute_event_monitor_thread.is_alive():
            print("Unable to force stop a thread.")
            raise BaseException

    @staticmethod
    def write_historic_stats_to_output(event):
        # 1. Open the output file in write mode to overwrite all the content.
        f = open(HTTPLogAnalyzer.get_output_alarms_events_file_name(), 'w+')
        # 2. Prepare a heading that says current resource section to hits.
        f.write("Historic events and alarms of resource_section to Hit count.\n")
        f.write("***********************************************************.\n")
        f.write(event + '\n')
        f.close()

    @staticmethod
    def run_two_minute_event_monitor() -> object:
        print("Starting {}".format(threading.current_thread().getName()))
        t = threading.currentThread()
        is_alarm_raised = False
        while getattr(t, "do_run", True):
            t = threading.currentThread()
            if is_alarm_raised:
                continue
            # compute the sum of all the 10 second hit counts.
            total_hit_counts = sum(HTTPLogAnalyzer.get_two_minute_hit_counts())

            # compute the total max threshold for 2 minutes.
            # total_max_threshold = 10 (default threshold per 10 sec) +
            # (120//10) where 120 is 120 seconds = 2 minutes / 10 (default time interval when stats are computed)
            total_max_threshold = HTTPLogAnalyzer.__instance.__threshold * (
                    HTTPLogAnalyzer.TWO_MINUTE_INTERVAL // HTTPLogAnalyzer.get_stats_time_interval())

            # raise an alarm event if the total_hit_counts exceed total_max_threshold.
            if total_hit_counts >= total_max_threshold:
                print("Raising an alarm as total hit count {} "
                      "is greater than maximum threshold {}"
                      .format(total_hit_counts, total_max_threshold))

                localtime = time.asctime(time.localtime(time.time()))

                HTTPLogAnalyzer.__instance.write_historic_stats_to_output(
                    "High traffic generated an alert - hits = {}, triggered at {} "
                    .format(total_hit_counts, localtime))
                is_alarm_raised = True
            elif is_alarm_raised:
                is_alarm_raised = False
                print(
                    "Clearing the alarm as total hit count {} is "
                    "less than maximum threshold {}"
                    .format(total_hit_counts, total_max_threshold))

                localtime = time.asctime(time.localtime(time.time()))

                HTTPLogAnalyzer.__instance.write_historic_stats_to_output(
                    "Clearing the alert at {} "
                    "as total hit count {} is "
                    "less than maximum threshold {}"
                    .format(localtime,
                            total_hit_counts,
                            total_max_threshold))

        print("Exiting {}".format(threading.current_thread().getName()))

    def __create_two_minute_event_monitor_thread(self):
        self.__two_minute_event_monitor_thread = threading.Thread(name="two_minute_event_monitor_thread",
                                                                  target=HTTPLogAnalyzer.run_two_minute_event_monitor)
        self.__two_minute_event_monitor_thread.do_run = True
        self.__two_minute_event_monitor_thread.name = "http_output_webserver_thread"
        self.__two_minute_event_monitor_thread.start()

    @staticmethod
    def run_webserver() -> object:
        print("Starting {}".format(threading.current_thread().getName()))
        t = threading.currentThread()
        server = HTTPWebServerDumpStats()
        while getattr(t, "do_run", True):
            t = threading.currentThread()
            server.listen_for_connections()
        print("Exiting {}".format(threading.current_thread().getName()))

    def __create_http_webserver_thread(self):
        self.__http_output_webserver_thread = threading.Thread(name="http_output_webserver_thread",
                                                               target=HTTPLogAnalyzer.run_webserver)
        self.__http_output_webserver_thread.do_run = True
        self.__http_output_webserver_thread.name = "http_output_webserver_thread"
        self.__http_output_webserver_thread.start()

    def __compute_aggregate_hit_count(self):
        # 1. Compute the sum of all the 120/10 = 12 samples.
        cumulative_sum_of_hits = sum(self.__section_to_hit_dict.values())
        max_number_of_samples_in_two_min = HTTPLogAnalyzer.TWO_MINUTE_INTERVAL // self.__stats_time_interval
        # 2. Add it to the tail of the hit count list.
        self.__two_minute_hit_counts.append(cumulative_sum_of_hits)
        # 3. Slide the window to the left by one if it is full. (12 values)
        if len(self.__two_minute_hit_counts) >= max_number_of_samples_in_two_min:
            self.__two_minute_hit_counts.popleft()

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
        print("Read {}.".format(log_entry))
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
        f.close()

    def __cleanup_section_to_hit_dict(self):
        del self.__section_to_hit_dict
        self.__section_to_hit_dict = defaultdict(int)

    def analyze_w3c_http_logs(self):
        # 3. If the input file is modified, then consume it.
        if self.__is_file_modified():
            # 4. For each new log entry read from the input file, consume it.
            for log_entry in self.__read_data_from_file():
                self.__consume_and_process_log_entry(log_entry)
            # 5. Compute the aggregate hit counts of all the Resources found.
            self.__compute_aggregate_hit_count()
        # 6. Over write the output file with the latest stats.
        self.__write_the_current_stats_to_output()
        # 7. Clean up the dict of resources to hits.
        self.__cleanup_section_to_hit_dict()
        # 8. Sleep for the stipulated time interval.
        time.sleep(self.__stats_time_interval)


if __name__ == "__main__":
    try:
        web_server = HTTPLogAnalyzer()
        while True:
            web_server.analyze_w3c_http_logs()
    except KeyboardInterrupt:
        print('^C received, shutting down.')
