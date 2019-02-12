

def perform_bfs(list_of_items,list_of_item_dependencies):
    pass

def perform_dfs_recurse(key_value_store,item,visited):
    list_of_nodes = []
    if visited[item]:
        return list_of_nodes
    list_of_nodes.append(item)
    visited[item] = True    
    if item in key_value_store:
        for sub_item in key_value_store[item]:
            list_of_nodes += perform_dfs_recurse(key_value_store,sub_item,visited)
    return list_of_nodes

def perform_dfs(list_of_items,list_of_item_dependencies):
    key_value_store ={}
    output = []
    for item in list_of_item_dependencies:
        if item[1] in key_value_store:
            key_value_store[item[1]].append(item[0])
        else:    
            key_value_store[item[1]] = [item[0]]
    visited = [False] * (len(list_of_items))
    for item in list_of_items:
        if item not in key_value_store:
            output.append(item)
    for item in key_value_store.keys():
        if item not in output:
            temp_list = perform_dfs_recurse(key_value_store,item,visited)
        for item in temp_list:
            if item not in output:
                output.append(item)
    return output


list_of_items = [0,1,2,3,4,5]
list_of_item_dependencies = [[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]

print("DFS = {}".format(perform_dfs(list_of_items,list_of_item_dependencies)))
print("BFS = {}".format(perform_bfs(list_of_items,list_of_item_dependencies)))
