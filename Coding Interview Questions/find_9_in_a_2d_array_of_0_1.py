

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
                [0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 1, 1, 1, 9, 0, 1, 1, 1]]

"""
Starting from the left most corner of the puzzle, 
traverse up, down, left or right in such a way that you can step on only 1's and not on 0's.
Count the number of 1's that lead to the final destination 9.
"""

def destination_found(row, column, number_of_1s, input_puzzle, already_visited_nodes):
    if row >= len(input_puzzle) or row < 0 or column >= len(input_puzzle[0]) or column < 0:
        return False
    already_visited_nodes[row][column] = 1
    if input_puzzle[row][column] == 9:
        print("Found 9")
        number_of_1s.append(1)
        return True
    if input_puzzle[row][column] == 0:
        return False
    if input_puzzle[row][column] == 1:
        print("Found 1")
        if column+1 < len(input_puzzle[0]) and not already_visited_nodes[row][column+1]:
            print("Recursing on {} {}".format(row,column+1))
            is_destination_found = destination_found(row, column + 1, number_of_1s, input_puzzle, already_visited_nodes)
            if is_destination_found:
                number_of_1s.append(1)
                return is_destination_found
        if row +1 < len(input_puzzle) and not already_visited_nodes[row+1][column]:
            print("Recursing on {} {}".format(row+1, column))
            is_destination_found = destination_found(row+1, column, number_of_1s, input_puzzle, already_visited_nodes)
            if is_destination_found:
                number_of_1s.append(1)
                return is_destination_found
        if column-1 >= 0 and not already_visited_nodes[row][column-1]:
            print("Recursing on {} {}".format(row, column - 1))
            is_destination_found = destination_found(row, column - 1, number_of_1s, input_puzzle, already_visited_nodes)
            if is_destination_found:
                number_of_1s.append(1)
                return is_destination_found
    return False

def steps_to_reach_destination(input_puzzle):
    rows = len(input_puzzle)
    columns = len(input_puzzle[0])
    total_number_of_steps = -1
    already_visited_nodes = [[0 for x in range(columns)] for y in range(rows)]
    for index in range(columns):
        number_of_1s = []
        if destination_found(0, index, number_of_1s, input_puzzle, already_visited_nodes):
            total_number_of_steps = len(number_of_1s)
            break

    return total_number_of_steps


if __name__ == "__main__":
        print("steps_to_reach_destination={}".format(steps_to_reach_destination(input_puzzle)))