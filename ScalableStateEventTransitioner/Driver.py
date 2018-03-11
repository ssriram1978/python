from Job import Job
from client import Client
from JobScheduler import JobScheduler
from JobMonitor import JobMonitor

if __name__ == "__main__":
    import sys

    # define unit test cases here.

    # initialize state event transitioner.
    # initialize client.
    client = Client()

    # initialize job scheduler with client jobs.
    number_of_executors = 5
    jobScheduler = JobScheduler()
    jobScheduler.set_jobs(client.getJobs())
    jobScheduler.set_executors(number_of_executors)
    jobScheduler.perform_job_scheduling()

    # initialize job monitor
    jobMonitor = JobMonitor()
    jobMonitor.monitor()
