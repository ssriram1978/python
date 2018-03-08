from Job import Job
from client import Client
from JobScheduler import JobScheduler
from JobMonitor import JobMonitor

if __name__ == "__main__":
    import sys
    #define unit test cases here.

    #initialize state event transitioner.
    #initialize client.
    client=Client()

    #initialize job scheduler with client jobs.
    number_of_executors=1
    jobScheduler=JobScheduler(client.getJobs(),number_of_executors)

    #initialize job monitor
    jobMonitor=JobMonitor()
