from Job import Job
from client import Client
from StateEventTransitioner import StateEventTransitioner

if __name__ == "__main__":
    import sys
    #define unit test cases here.
    job=Job("Test")
    job.set_next_state("initialize")
    job.set_current_event("timeout")

    events = ["timeout", "error", "success response", "failure response"]
    states = ["initialize", "bind", "connect", "request", "read", "close"]

    state_event_transition=StateEventTransitioner()
    state_event_transition.setEvents(events)
    state_event_transition.setStates(states)

    hash_table={}
    client=Client(events,states)
    for state in states:
        for event in events:
            hash_table[state+event]=client

    state_event_transition.setTransitionTable(hash_table)

    for count in range(10):
        next_state=state_event_transition.execute(job)
        job.set_next_state(next_state)
