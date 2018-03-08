import threading
import logging
import time
from JobExecutor import JobExecutor

class JobScheduler:
    def __init__(self,jobs,executors):
        print("I am Job Scheduler %d" %(input))
        self.jobs=jobs
        self.executors=executors
        job_executor=JobExecutor()
        threads=[]

        jobs_per_executor=len(jobs)//executors

        running_count = 0
        for count in range(executors):
            name="executor"+str(count)
            thread_queue=[]
            current_count=0
            while current_count < jobs_per_executor:
                thread_queue+=jobs[running_count]
                current_count+=1
                running_count+=1

            thread=threading.Thread(name=name,target=job_executor.execute(),args=thread_queue)
            threads.append(thread)
            thread.start()



