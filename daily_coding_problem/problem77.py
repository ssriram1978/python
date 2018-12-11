"""
his problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

"""
from operator import itemgetter


def check_overlap(last_item, item):
    is_overlap = False
    if item[0] >= last_item[0] and item[0] <= last_item[1]:
        is_overlap = True
    elif item[1] >= last_item[0] and item[1] <= last_item[1]:
        is_overlap = True
    return is_overlap


def merge_overlap(last_item, item):
    merged_start = 0
    merged_end = 0
    if last_item[0] <= item[0]:
        merged_start = last_item[0]
    else:
        merged_start = item[0]

    if last_item[1] >= item[1]:
        merged_end = last_item[1]
    else:
        merged_end = item[1]
    return merged_start, merged_end


def merge(list_of_intervals):
    list_of_intervals = sorted(list_of_intervals, key=itemgetter(0))
    print(list_of_intervals)
    output_list = []
    for item in list_of_intervals:
        if not len(output_list):
            output_list.append(item)
        else:
            if check_overlap(output_list[-1], item):
                output_list[-1] = merge_overlap(output_list[-1], item)
            else:
                output_list.append(item)
    return output_list


unmerged_list = [(1, 3), (5, 8), (4, 10), (20, 25)]
merged_list = merge(unmerged_list)
print(merged_list)


"""
Solution
We can do this by sorting all the intervals by their start time. This way, when looking at the current interval, if it overlaps with the previous one we can just combine them.

def merge(intervals):
    result = []
    for start, end in sorted(intervals, key=lambda i: i[0]):
        # If current interval overlaps with the previous one, combine them
        if result and start <= result[-1][1]:
            prev_start, prev_end = result[-1]
            result[-1] = (prev_start, max(end, prev_end))
        else:
            result.append((start, end))
    return result
    
Since we have to sort the intervals, this runs in O(N log N) time.
"""