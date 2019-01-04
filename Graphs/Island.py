"""
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island.
For example, the below matrix contains 5 islands

Example:

Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1}
Output : 5


"""

def mark_neighbors_visited(graph,
                           visited_graph,
                           current_row,
                           current_column):
    if current_row < 0 or current_row >= len(graph):
        return
    if current_column < 0 or current_column >= len(graph[current_row]):
        return
    if visited_graph[current_row][current_column] == 1:
        return
    if graph[current_row][current_column] == 0:
        return
    if graph[current_row][current_column] == 1:
        visited_graph[current_row][current_column] = 1
        #right
        mark_neighbors_visited(graph,
                               visited_graph,
                               current_row,
                               current_column+1)
        #left
        mark_neighbors_visited(graph,
                               visited_graph,
                               current_row,
                               current_column - 1)
        #bottom
        mark_neighbors_visited(graph,
                               visited_graph,
                               current_row+1,
                               current_column)
        #top
        mark_neighbors_visited(graph,
                               visited_graph,
                               current_row-1,
                               current_column)
        #right top
        mark_neighbors_visited(graph,
                               visited_graph,
                               current_row+1,
                               current_column+1)
        #left top
        mark_neighbors_visited(graph,
                               visited_graph,
                               current_row+1,
                               current_column - 1)
        #bottom left
        mark_neighbors_visited(graph,
                               visited_graph,
                               current_row+1,
                               current_column-1)
        #bottom right
        mark_neighbors_visited(graph,
                               visited_graph,
                               current_row+1,
                               current_column+1)

def count_islands(graph):
    count=0
    rows = len(graph)
    columns = len(graph[0])
    visited_graph = [[0 for y in range(columns)] for x in range(rows)]
    for index1 in range(rows):
        for index2 in range(columns):
            if not visited_graph[index1][index2]:
                if graph[index1][index2] == 0:
                    continue
                elif graph[index1][index2] == 1:
                    count+=1
                    mark_neighbors_visited(graph,visited_graph,index1,index2)
    return count


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]
print("Total number of islands = {}".format(count_islands(graph)))
