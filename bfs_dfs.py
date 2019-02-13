from collections import deque

def perform_bfs(list_of_jobs,
                list_of_job_dependencies,
                starting_job,
                ending_job):
    key_value_store ={}
    output = []

    #validate input parameters.
    if starting_job not in list_of_jobs \
    or ending_job not in list_of_jobs:
       return output
 
    #prepare a key,value store of the job[1] 
    #and it's pre-requisite job[0]
    for job in list_of_job_dependencies:
        if job[1] in key_value_store:
            key_value_store[job[1]].append(job[0])
        else:    
            key_value_store[job[1]] = [job[0]]

    #maintain a boolean list of visited nodes to avoid infinite loop.
    visited = [False] * (len(list_of_jobs))
       
    #maintain a queue with the starting job
    queue = deque()
    queue.append(starting_job)
    path_found = False
    while not path_found and len(queue):
        #dequeue an item from the queue.
        current_item = queue.popleft()
        #check if the current item is not visited to avoid infinite loops.
        if not visited[current_item]:
            #append the item to the output.
            output.append(current_item)
            #mark the visited item index to be True.
            visited[current_item] = True
            if current_item == ending_job:
                path_found = True
                break
            #check if the current_item is in the dict of jobs and dependencies.
            if current_item in list_of_job_dependencies[current_item]:
                for dependency in list_of_job_dependencies[current_item]:
                    #append the dependency to the queue.
                    if not visited[dependency]:
                        queue.append(dependency)
    if not path_found:
        output = []
    return output

def perform_dfs_recurse(key_value_store,job,visited):
    list_of_nodes = []
    #skip the current job if it is already traversed.
    if visited[job]:
        return list_of_nodes
    visited[job] = True
    #recurse on all the dependencies or pre-requisites of the current job.
    if job in key_value_store:
        for sub_job in key_value_store[job]:
            list_of_nodes += perform_dfs_recurse(key_value_store,sub_job,visited)
    #append the current job to the list.
    list_of_nodes.append(job)
    return list_of_nodes

def perform_dfs(list_of_jobs,list_of_job_dependencies):
    key_value_store ={}
    output = []
    #prepare a key,value pair. key = job, value = dependencies [list of jobs].
    for job in list_of_job_dependencies:
        if job[1] in key_value_store:
            key_value_store[job[1]].append(job[0])
        else:    
            key_value_store[job[1]] = [job[0]]

    #prepare a visited list initialized with False to avoid infinite loop.
    visited = [False] * (len(list_of_jobs))

    # for every job in the list of jobs, check if there is a dependency.
    for job in list_of_jobs:
        if job not in key_value_store:
            #there is no dependency of the the current job.
            #just add it to the output.
            output.append(job)
    #iterate over all the keys in the dictionary and append the dependencies
    #first before adding the current job.
    for job in key_value_store.keys():
        #do not add duplicates.
        if job not in output:
            #recurse over the dependencies of the current job.
            temp_list = perform_dfs_recurse(key_value_store,job,visited)
        for job in temp_list:
            #do not add duplicates.
            if job not in output:
                output.append(job)
    return output


def find_all_jobs_with_dependencies():
    list_of_jobs = [0,1,2,3,4,5]
    #index 0 of every job is the pre-requisite.
    #index 1 of every job is the current job.
    list_of_job_dependencies = [[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]
    #example; job in index 0 is 2 with a pre-requisite of job 5.
    print("DFS = {}".format(perform_dfs(list_of_jobs,list_of_job_dependencies)))
    list_of_job_dependencies = [[5,2],[5,0],[4,0],[4,1],[2,3],[3,2]]
    print("DFS = {}".format(perform_dfs(list_of_jobs,list_of_job_dependencies)))
    list_of_job_dependencies = [[5,1],[4,1],[3,1],[2,1]]
    print("DFS = {}".format(perform_dfs(list_of_jobs,list_of_job_dependencies)))


def find_a_path_between_the_given_jobs():
    list_of_jobs = [0,1,2,3,4,5]
    #index 0 of every job is the pre-requisite.
    #index 1 of every job is the current job.
    list_of_job_dependencies = [[1,0],[2,1],[3,2],[4,3],[5,4],[5,0]]
    #example; job in index 0 is 2 with a pre-requisite of job 5.
    print("BFS = {}".format(perform_bfs(list_of_jobs,
                                        list_of_job_dependencies,
                                        0,
                                        5)))
    print("BFS = {}".format(perform_bfs(list_of_jobs,
                                        list_of_job_dependencies,
                                        5,
                                        2)))
find_all_jobs_with_dependencies()
find_a_path_between_the_given_jobs()