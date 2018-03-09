import threading
from Job import Job
import logging

class Client_param:
    def __init__(self,local_port,remote_port,local_ip,remote_ip,socket_fd):
        self.local_port=0
        self.remote_port=0
        self.local_ip=0
        self.remote_ip=0
        self.socket_fd=0

class Client:
    def __init__(self):
        print("client is getting created.")
        self.events = ["timeout", "error", "success response", "failure response"]
        self.states = ["initialize", "bind", "connect", "request", "read", "close"]


    def execute(self,job_info):
        logging.debug("Executing this Job ID=" + str(job_info.get_job_id())
              + " in current state=" + str(job_info.get_current_state())
              + " and current event=" + str(job_info.get_current_event()))
        index=self.states.index(job_info.get_current_state())
        if index == len(self.states)-1:
            index=-1
        #move to next state
        job_info.set_current_state(self.states[index+1])

    def getJobs(self):
        Jobs=[]
        for count in range(100):
            jobid="Job"+str(count)
            job = Job(jobid)
            job.set_current_state(self.states[0])
            job.set_current_event(self.events[0])
            client_param=Client_param(count,count,count,count,count)
            job.set_job_param(client_param)
            Jobs.append(job)
            job.set_job_work(self)
        return Jobs

logging.basicConfig(
level=logging.DEBUG,
format='[%(levelname)s] %(asctime)s (%(threadName)-10s) %(message)s',
)

