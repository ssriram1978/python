"""
Topological Sorting
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering
of vertices such that for every directed edge uv, vertex u comes before v in the ordering.
Topological Sorting for a graph is not possible if the graph is not a DAG.

 In topological sorting, we use a temporary stack.
 We don’t print the vertex immediately, we first recursively call topological sorting
 for all its adjacent vertices, then push it to a stack.
 Finally, print contents of stack. Note that a vertex is pushed to stack only when
 all of its adjacent vertices (and their adjacent vertices and so on) are already in stack.


 Find the ordering of tasks from given dependencies:
 ---------------------------------------------------
There are a total of n tasks you have to pick, labeled from 0 to n-1.
Some tasks may have prerequisites tasks,
for example to pick task 0 you have to first finish tasks 1, which is expressed as a pair: [0, 1]

Given the total number of tasks and a list of prerequisite pairs,
return the ordering of tasks you should pick to finish all tasks.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all tasks, return an empty array.

Input: 2, [[1, 0]]
Output: [0, 1]
Explanation: There are a total of 2 tasks to pick.
To pick task 1 you should have finished task 0. So the correct task order is [0, 1] .


Input: 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
Output: [0, 1, 2, 3] or [0, 2, 1, 3]
Explanation: There are a total of 4 tasks to pick.
To pick task 3 you should have finished both tasks 1 and 2.
Both tasks 1 and 2 should be pick after you finished task 0.
So one correct task order is [0, 1, 2, 3].
Another correct ordering is [0, 2, 1, 3].

"""

# Python program to print topological sorting of a DAG
from collections import defaultdict


# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # A recursive function used by topologicalSort

    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

                # Push current vertex to stack which stores result
        stack.insert(0, v)

        # The function to do Topological Sort. It uses recursive
        # topologicalSortUtil()

    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of the stack
        return stack


def ordering_of_tasks(total_number_of_tasks, dependency_list):
    graph = Graph(total_number_of_tasks)
    for dependency in dependency_list:
        graph.addEdge(dependency[0],dependency[1])
    return graph.topologicalSort()


print("ordering of tasks {} list {} is {}."
      .format(4,[[1, 0], [2, 0], [3, 1], [3, 2]],
              ordering_of_tasks(4,[[1, 0], [2, 0], [3, 1], [3, 2]])))