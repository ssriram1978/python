from Job import Job
from JobScheduler import JobScheduler
from JobMonitor import JobMonitor
import os
import importlib.util
import sys


def load_from_file(module_name, class_name):
    class_inst = None

    spec = importlib.util.find_spec(module_name)
    if spec is None:
        print("can't find the module %s"%(module_name))
    else:
        # If you chose to perform the actual import ...
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # Adding the module to sys.modules is optional.
        sys.modules[module_name] = module
        class_inst = getattr(module, class_name)()
        #print(type(class_inst))
        #print(dir(class_inst))

    return class_inst

if __name__ == "__main__":
    import sys

    # define unit test cases here.

    number_of_executors=int(input("Enter the number of threads:").strip())

    filename=input("Enter the module name that contains the work to be executed:").strip()
    classname=input("Enter the class name in module %s that needs to be invoked for getting the work done:"%(filename)).strip()
    # initialize the object to execute.
    object = load_from_file(filename,classname)
    object.assign_state_event_actions()
    object.print_state_event_dict()
    # initialize job scheduler with client jobs.
    jobScheduler = JobScheduler()
    jobScheduler.set_jobs(object.getJobs())
    jobScheduler.set_executors(number_of_executors)
    jobScheduler.perform_job_scheduling()

    # initialize job monitor
    jobMonitor = JobMonitor()
    jobMonitor.monitor()
