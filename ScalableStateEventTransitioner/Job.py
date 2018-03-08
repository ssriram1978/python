class Job:
    def __init__(self,job_id):
        self.job_id=job_id
        self.current_state=-1
        self.current_event=-1
        self.job_param=None
        self.job_work=None
    def set_current_state(self,current_state):
        self.current_state=current_state
    def set_current_event(self,current_event):
        self.current_event=current_event
    def get_current_state(self):
        return self.current_state
    def get_current_event(self):
        return self.current_event
    def get_job_param(self):
        return self.job_param
    def set_job_param(self,job_param):
        self.job_param=job_param
    def set_job_work(self,work):
        self.job_work=work