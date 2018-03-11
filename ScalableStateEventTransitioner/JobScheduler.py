import threading
import logging
import time
from JobExecutor import JobExecutor
from JobMonitor import JobMonitor
from collections import deque
from collections import defaultdict

class JobScheduler:
    instance = None
    def __new__(cls):  # __new__ always a classmethod
        if not JobScheduler.instance:
            JobScheduler.instance = JobScheduler.__JobScheduler()
        return JobScheduler.instance

    def __getattr__(self, name):
        return getattr(self.instance, name)

    def __setattr__(self, name):
        return setattr(self.instance, name)

    @staticmethod
    def schedule():
        JobScheduler.instance.schedule()

    class __JobScheduler:
        def __init__(self):
            self.job_table = defaultdict(object)
            self.threads = []
            self.conditions = []
            self.all_jobs=None
            self.thread_queues = []
            self.condition_Job_scheduler=None
            self.job_scheduler_thread=threading.Thread(name='scheduler',
                                      target=JobScheduler.schedule)
        def schedule(self):
            for index in range(self.total_number_of_executors):
                queue = deque()
                self.thread_queues.append(queue)

            self.create_threads_and_conditions()
            while JobMonitor.isActive():
                self.process_jobs()
                #time.sleep(10)

            for t in self.threads:
                t.join()

        def set_jobs(self,jobs):
            self.all_jobs = jobs

        def set_executors(self,executors):
            self.total_number_of_executors=executors

        def perform_job_scheduling(self):
            logging.debug("I am Job Scheduler.Total Jobs=%d and total number of executors=%d"
                          % (len(self.all_jobs),
                        self.total_number_of_executors))
            #spawn a job scheduler thread
            self.job_scheduler_thread.start()

        def create_threads_and_conditions(self):
            for index in range(self.total_number_of_executors):
                condition = threading.Condition()
                self.conditions.append(condition)
                thread = threading.Thread(name='executor' + str(index),
                                      target=JobExecutor.execute,
                                      args=(self.thread_queues[index],condition,))
                self.threads.append(thread)
                thread.start()
            self.condition_Job_scheduler=threading.Condition()

        def process_jobs(self):
            running_count = 0
            jobs_per_executor = len(self.all_jobs) // self.total_number_of_executors
            executor=0

            current_count_per_executor = 0

            #split the jobs equally across all the threads.
            while running_count < len(self.all_jobs):
                if current_count_per_executor == jobs_per_executor:
                    executor+=1
                    current_count_per_executor=0
                job=self.all_jobs[running_count]
                if job != None:
                    self.thread_queues[executor].append(job)
                    self.all_jobs[running_count]=None
                    current_count_per_executor += 1
                    if job.get_current_state()==job.get_init_state():
                        JobMonitor().update_total_job_done_count()
                running_count += 1

            #notify the threads to wake up and start working on their respective queues.
            for index in range(self.total_number_of_executors):
                #time.sleep(1)
                condition = self.conditions[index]
                with condition:
                    condition.notifyAll()

            #wait for any one of the threads to notify that the job is done.
            #with self.condition_Job_scheduler:
            #    self.condition_Job_scheduler.wait()

        def notify_job_done(self,job):
            self.all_jobs[job.get_job_index()]=job
            #signal Job scheduler to wake up and start working on its queues.
            #with self.condition_Job_scheduler:
            #    self.condition_Job_scheduler.notifyAll()
            JobMonitor().update_current_thread_job_count(threading.current_thread().name)
            return None

