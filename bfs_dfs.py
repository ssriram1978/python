from queue import deque
from collections import defaultdict

class Node:
    def __init__(self,value):
        #set the value of the node
        self.value=str(value)
        self.neighbors=[]

    def add_adjacent(self,node):
        if node != None:
            #keep adding neighbors to the queue
            self.neighbors.append(node)

class bfs:
        def find_route(self,start,end):
            self.list_of_route = []
            self.dict_of_routes = defaultdict(list)
            if start == None or end == None:
                return self.list_of_route
            #declare a temporary nodelist which is a queue
            nodelist=deque()
            #append start to the nodelist
            nodelist.append(start)
            #declare a boolean isFound to to be false
            isFound=False
            while len(nodelist):
                #pop an item from the node list
                node=nodelist.popleft()
                if node:
                    #check if the node is already visited. Use dict to search in o(1)
                    #print(self.dict_of_routes[node.value])
                    if self.dict_of_routes[node.value] != []:
                        #you already have traversed this node.
                        #skip it
                        #print("you already have traversed this node %s,skip it." %(node.value))
                        continue
                    else:
                        #add this element to the self.list
                        self.list_of_route.append(node.value)
                        #add this node to the dictionary
                        self.dict_of_routes[node.value].append(node)
                        #print("adding node %s to the list of route and to dictionary"%(node.value))
                        if node.value == end.value:
                            #you found a route to the end
                            #print("Found %s"%(node.value))
                            isFound=True
                            break
                        #add the neighboring nodes to the queue
                        for neighbors in node.neighbors:
                            if self.dict_of_routes[neighbors.value] == []:
                                #append the neighbor to the nodelist
                                #print("Appending %s to the traversal list"%(neighbors.value))
                                nodelist.append(neighbors)
                            #else:
                            #    print("skipping %s because we already traversed it."%(neighbors.value))
            if isFound == True:
                #print("Returning"+str(self.list_of_route))
                return self.list_of_route
                """
                # try to find the shortest route
                for index in range(len(self.list_of_route)):
                    for index2 in range(len(self.list_of_route)-1,index,-1):
                        list_of_nodes=self.dict_of_routes[self.list_of_route[index]].pop()
                        if list_of_nodes:
                            for neighbors in list_of_nodes:
                                if neighbors.value == self.list_of_route[index2]:
                                    #found a direct route
                """

            else:
                #print("Returning None")
                return None

class dfs:
    def __init__(self):
        #define an empty route that needs to be reset everytime
        self.route=[]
        #define a dict to search for already traversed nodes in o(1)
        self.route_path=defaultdict(str)

    def find_route(self,start,end):
        # define an empty route that needs to be reset everytime
        self.route = []
        # define a dict to search for already traversed nodes in o(1)
        self.route_path = defaultdict(str)
        return self.find_route_dfs(start,end)

    def find_route_dfs(self,start,end):
        #base case
        # declare route_found to be false
        route_found=False

        if start == None or end == None:
            return None

        #add the current node to the dictionary and the route list if it is not there
        if self.route_path[start.value] == "":
            #not found, add it to the list and dict.
            self.route_path[start.value]=start.value
            self.route.append(start.value)
        else:
            #node is already in the dict and list
            #just return
            return None

        #return the route list if you found a path
        if start.value == end.value:
            #print("Match found %s" %(start.value))
            route_found=True
        else:
            #search recursively for nodes via the neighbors
            for node in start.neighbors:
                list_of_routes = self.find_route_dfs(node,end)
                if list_of_routes != None:
                    #break from the for loop
                    route_found=True
                    break

        if route_found==True:
            return self.route
        else:
            return None

total_nodes =8
nodes = [0] * total_nodes
for index in range(8):
    nodes[index] = Node(index)

nodes[0].add_adjacent(nodes[1])
nodes[0].add_adjacent(nodes[2])
nodes[0].add_adjacent(nodes[3])
nodes[1].add_adjacent(nodes[0])
nodes[1].add_adjacent(nodes[2])
nodes[1].add_adjacent(nodes[3])
nodes[2].add_adjacent(nodes[0])
nodes[2].add_adjacent(nodes[1])
nodes[2].add_adjacent(nodes[3])
nodes[2].add_adjacent(nodes[4])
nodes[2].add_adjacent(nodes[5])
nodes[3].add_adjacent(nodes[1])
nodes[3].add_adjacent(nodes[2])
nodes[3].add_adjacent(nodes[4])
nodes[3].add_adjacent(nodes[5])
nodes[4].add_adjacent(nodes[2])
nodes[4].add_adjacent(nodes[3])
nodes[4].add_adjacent(nodes[5])
nodes[4].add_adjacent(nodes[6])
nodes[4].add_adjacent(nodes[7])
nodes[5].add_adjacent(nodes[2])
nodes[5].add_adjacent(nodes[3])
nodes[5].add_adjacent(nodes[4])
nodes[5].add_adjacent(nodes[6])
nodes[5].add_adjacent(nodes[7])
nodes[6].add_adjacent(nodes[4])
nodes[6].add_adjacent(nodes[5])
nodes[6].add_adjacent(nodes[7])
nodes[7].add_adjacent(nodes[4])
nodes[7].add_adjacent(nodes[5])
nodes[7].add_adjacent(nodes[6])
print("BFS")
bfs_search = bfs()
print(bfs_search.find_route(nodes[0],nodes[7]))
print(bfs_search.find_route(nodes[1],nodes[7]))
print(bfs_search.find_route(nodes[2],nodes[7]))
print(bfs_search.find_route(nodes[3],nodes[7]))
print(bfs_search.find_route(nodes[4],nodes[7]))
print(bfs_search.find_route(nodes[5],nodes[7]))
print(bfs_search.find_route(nodes[6],nodes[7]))
print(bfs_search.find_route(nodes[7],nodes[7]))
print("DFS")
dfs_search=dfs()
print(dfs_search.find_route(nodes[0],nodes[7]))
print(dfs_search.find_route(nodes[1],nodes[7]))
print(dfs_search.find_route(nodes[2],nodes[7]))
print(dfs_search.find_route(nodes[3],nodes[7]))
print(dfs_search.find_route(nodes[4],nodes[7]))
print(dfs_search.find_route(nodes[5],nodes[7]))
print(dfs_search.find_route(nodes[6],nodes[7]))
print(dfs_search.find_route(nodes[7],nodes[7]))