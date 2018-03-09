import threading
import logging
import time
from JobExecutor import JobExecutor
from JobMonitor import JobMonitor
from collections import deque

class JobScheduler:

    def create_threads_and_conditions(self):

        for index in range(self.total_number_of_executors):
            condition = threading.Condition()
            self.conditions.append(condition)
            thread = threading.Thread(name='executor' + str(index),
                                      target=JobExecutor.execute,
                                      args=(self.thread_queues[index],condition,))
            self.threads.append(thread)
            thread.start()

    def process_jobs(self):
        running_count = 0
        jobs_per_executor = len(self.all_jobs) // self.total_number_of_executors
        executor=0

        while running_count < len(self.all_jobs):
            current_count = 0
            while current_count < jobs_per_executor:
                self.thread_queues[executor].append(self.all_jobs[running_count])
                current_count += 1
                running_count += 1
            executor+=1

        for index in range(self.total_number_of_executors):
            time.sleep(1)
            condition = self.conditions[index]
            with condition:
                condition.notifyAll()

    def __init__(self,all_jobs,executors):
        print("I am Job Scheduler.Total Jobs=%d and total number of executors=%d"%(len(all_jobs),executors))
        self.threads=[]
        self.conditions=[]
        self.all_jobs=all_jobs
        self.total_number_of_executors=executors

        self.thread_queues=[]

        for index in range(self.total_number_of_executors):
            queue=deque()
            self.thread_queues.append(queue)

        self.create_threads_and_conditions()
        print(self.thread_queues)
        while JobMonitor.isActive():
            self.process_jobs()
            time.sleep(10)

        for t in self.threads:
            t.join()




