from collections import defaultdict
from Job import Job

class StateEventTransitioner:
    def __init__(self):
        print("State Event Transitioner")
        self.table=defaultdict(object)

    def setStates(self,states):
        assert(states != type(list))
        self.states=states

    def setEvents(self,events):
        assert (events != type(list))
        self.events=events

    """
    keys= 1.Current state.
          2.Current event.
    values= 1.Object to execute.
    """
    def setTransitionTable(self,table):
        assert(table != type(dict))
        self.table.update(table)

    def execute(self,job_info):
        assert(job_info != type(Job))
        key=job_info.get_current_state()+job_info.get_current_event()
        value=self.table[key]
        next_state=-1
        if value==[]:
            print("No object found for key="+str(key))
        else:
            print("Trying to execute the job with key="+str(key))
            next_state=value.execute(job_info)
        return next_state


