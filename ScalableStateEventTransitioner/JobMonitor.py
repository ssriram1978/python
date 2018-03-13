import logging
from threading import Timer
from collections import defaultdict

class JobMonitor:

    stop = False

    instance=None

    def __new__(cls):  # __new__ always a classmethod
        if not JobMonitor.instance:
            JobMonitor.instance = JobMonitor.__JobMonitor()
        return JobMonitor.instance

    @staticmethod
    def isActive():
        if JobMonitor.stop==False:
            return True
        else:
            return False

    @staticmethod
    def compute_rate():
        return JobMonitor().compute_rate()

    class __JobMonitor:
        def __init__(self):
            print("Job Monitor")
            self.current_job_count = 0
            self.prev_job_count = 0
            self.current_job_done_rate = 0
            Timer(1, JobMonitor.compute_rate).start()
            self.current_thread_job_count=defaultdict(int)
            self.previous_thread_job_count=defaultdict(int)
            self.thread_job_completion_rate=defaultdict(int)

        def update_total_job_done_count(self):
            self.current_job_count+=1

        def compute_rate(self):
            self.current_job_done_rate = self.current_job_count - self.prev_job_count
            self.prev_job_count = self.current_job_count

            for name, value in self.current_thread_job_count.items():
                self.thread_job_completion_rate[name]=self.current_thread_job_count[name]-self.previous_thread_job_count[name]
                self.previous_thread_job_count[name] = value


            Timer(1, JobMonitor.compute_rate).start()

        def update_current_thread_job_count(self,thread_id):
            self.current_thread_job_count[thread_id]+=1

        def monitor(self):
            while True:
                character = input("Enter your choice: q-quit, r-display rate:").strip()
                if character == 'q':
                    JobMonitor.stop=True
                    break
                elif character == 'r':
                    print("Total number of Jobs completed=%d,Current Rate=%d"
                          % (self.current_job_count,self.current_job_done_rate))
                    for name,value in self.thread_job_completion_rate.items():
                        print("Name of the thread=%s,Rate=%d"%(name,value))