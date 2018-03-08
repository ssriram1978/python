from Job import Job

class Client:
    def __init__(self,events,states):
        print("client is getting created.")
        self.events=events
        self.states=states

    def execute(self,job_info):
        print("Executing this Job=" + str(job_info.get_job_param())
              + " in current state=" + str(job_info.get_current_state())
              + "and current event=" + str(job_info.get_current_event()))
        index=self.states.index(job_info.get_current_state())
        if index == len(self.states)-1:
            index=-1
        return self.states[index+1]


