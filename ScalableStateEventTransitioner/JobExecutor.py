
from Job import Job
import threading
from JobMonitor import JobMonitor
from JobMonitor import JobMonitor

class JobExecutor:
    def __init__(self):
        print("Job Executor")

    @staticmethod
    def execute(jobs,cond):
        while JobMonitor.isActive() == True:
            with cond:
                cond.wait()
                while len(jobs) > 0:
                    job=jobs.popleft()
                    work=job.get_job_work()
                    work.execute(job)


