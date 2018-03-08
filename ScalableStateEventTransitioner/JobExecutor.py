class JobExecutor:
    def __init__(self):
        print("Job Executor")
        for count in range(10):
            next_state = state_event_transition.execute(job)
            job.set_next_state(next_state)
