import threading
import logging
import time

class JobScheduler:
    def __init__(self,jobs,executors):
        print("I am Job Scheduler %d" %(input))
        self.jobs=jobs
        self.executors=executors

        threads=[]
        for count in range(executors):
            thread=threading.Thread(name="",target=)
            thread.start()
            threads.append(thread)


