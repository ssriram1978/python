from collections import defaultdict


class Node:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, another):
        return hasattr(another, 'value') and self.value == another.value

        # def __str__(self):
        #   return str(self.value)


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.node_object = defaultdict(list)

    def create_graph(self, origin, dest):
        key = self.node_object[origin] = Node(origin)
        value = self.node_object[dest] = Node(dest)

        self.graph[key].append(value)
        # print("value=%s" % (key))
        # print("graph=")
        # print(self.graph[key])

    def BFS_walk(self, origination):
        if self.graph == None or origination == None or self.node_object[origination] == None:
            return

        # initialize a list of the nodes to be traversed.
        list_of_nodes_to_be_traversed = []

        # initialize all the nodes in the graph with traversed flag set to 0
        print("Total number of nodes=%d" % (len(self.node_object)))
        node_traversed = [False] * len(self.node_object)

        # append the origination node to the list
        list_of_nodes_to_be_traversed.append(self.node_object[origination])

        # set the current node as traversed.
        node_traversed[self.node_object[origination].value] = True

        # start BFS until the list is empty
        while (list_of_nodes_to_be_traversed):
            # pop from left
            current_node = list_of_nodes_to_be_traversed.pop(0)
            print("BFS:Traversed node with value=%d" % (current_node.value))

            # start checking for all nodes from the current node.
            for node in self.graph[current_node]:
                # print("node.value=%d" %(node.value))
                if node_traversed[node.value] == False:
                    # print("Adding node=%d to the list."%(node.value))
                    list_of_nodes_to_be_traversed.append(node)
                    node_traversed[node.value] = True

    def DFS_walk(self, current_node,list=None):
        if list==None:
            list=[False]*len(self.node_object)
        if current_node == None:
            return

        curr_node_obj=self.node_object[current_node]

        print("DFS:Traversed node with value=%d" %(curr_node_obj.value))
        list[curr_node_obj.value]=True

        for node in self.graph[curr_node_obj]:
            #print("node.value=%d" %(node.value))
            if list[node.value]==False:
                self.DFS_walk(node.value,list)
graph = Graph()
graph.create_graph(0, 1)
graph.create_graph(0, 2)
graph.create_graph(0, 3)
graph.create_graph(1, 2)
graph.create_graph(2, 3)
graph.create_graph(2, 4)
graph.create_graph(3, 4)
graph.create_graph(3, 5)
graph.create_graph(5, 6)
graph.create_graph(4, 9)
graph.create_graph(6, 7)
graph.create_graph(9, 10)
graph.create_graph(7, 8)

graph.BFS_walk(0)
graph.DFS_walk(0)





