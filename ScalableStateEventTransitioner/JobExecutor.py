class JobExecutor:
    def __init__(self,jobs):
        print("Job Executor")
        for job in jobs:
            job.job_work(jobs)

