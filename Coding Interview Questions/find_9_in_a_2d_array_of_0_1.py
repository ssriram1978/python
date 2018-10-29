

input_puzzle = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 1, 1, 9, 1, 1, 1, 1]]

"""
Starting from the left most corner of the puzzle, 
traverse up, down, left or right in such a way that you can step on only 1's and not on 0's.
Count the number of 1's that lead to the final destination 9.
"""
def compute_min_length(row,
                       column,
                       input_puzzle,
                       already_visited_nodes,
                       min_distance_computed_nodes):
    min_computed_length = 0

    if row >= len(input_puzzle) or row < 0 or column >= len(input_puzzle[0]) or column < 0:
        return min_computed_length

    if input_puzzle[row][column]:
        if min_distance_computed_nodes[row][column] == -1 or \
                min_distance_computed_nodes[row][column] > 0:
            min_computed_length = min_distance_computed_nodes[row][column]
        else:
            temp_number_of_1s = []
            if destination_found(row,
                                column,
                                temp_number_of_1s,
                                input_puzzle,
                                already_visited_nodes,
                                 min_distance_computed_nodes):
                min_computed_length = len(temp_number_of_1s)
    return min_computed_length

def destination_found(row,
                      column,
                      number_of_1s,
                      input_puzzle,
                      already_visited_nodes,
                      min_distance_computed_nodes):
    if row >= len(input_puzzle) or row < 0 or column >= len(input_puzzle[0]) or column < 0:
        return False
    if input_puzzle[row][column] == 9:
        print("Found 9")
        number_of_1s.append(1)
        return True
    if input_puzzle[row][column] == 0:
        return False
    if already_visited_nodes[row][column]:
        return False
    if input_puzzle[row][column] == 1:
        #print("Found 1")
        already_visited_nodes[row][column] = 1
        min_length_array = []
        length = compute_min_length(row,
                                    column-1,
                                    input_puzzle,
                                    already_visited_nodes,
                                    min_distance_computed_nodes)
        if length != 0 and length != -1:
            min_length_array.append(length)

        length = compute_min_length(row,
                                    column+1,
                                    input_puzzle,
                                    already_visited_nodes,
                                    min_distance_computed_nodes)

        if length != 0 and length != -1:
            min_length_array.append(length)

        length = compute_min_length(row+1,
                                    column,
                                    input_puzzle,
                                    already_visited_nodes,
                                    min_distance_computed_nodes)

        if length != 0 and length != -1:
            min_length_array.append(length)

        if len(min_length_array):
            #print(min_length_array)
            min_val = min(min_length_array)+1
            for index in range(min_val):
                number_of_1s.append(1)
            min_distance_computed_nodes[row][column] = min_val
            return True
        else:
            min_distance_computed_nodes[row][column] = -1
            return False

def steps_to_reach_destination(input_puzzle):
    rows = len(input_puzzle)
    columns = len(input_puzzle[0])
    number_of_1s = []
    already_visited_nodes = [[0 for x in range(columns)] for y in range(rows)]
    min_distance_computed_nodes = [[0 for x in range(columns)] for y in range(rows)]
    if destination_found(0, 0, number_of_1s, input_puzzle, already_visited_nodes, min_distance_computed_nodes):
        print("min_distance_computed_nodes={}".format(min_distance_computed_nodes))
        print("already_visited_nodes={}".format(already_visited_nodes))
        return len(number_of_1s)

if __name__ == "__main__":
        print("steps_to_reach_destination={}".format(steps_to_reach_destination(input_puzzle)))