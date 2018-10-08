"""
Given an input list of x and y coordinates of a bunch of points:
    1. Group the coordinates based upon the distance between the coordinates.
Given an input number of the number of trucks available,
    2. Prepare an output list which contains the list of groups totalling to the
        available number of trucks.
"""
from  operator import itemgetter
from math import sqrt
from collections import deque
from collections import defaultdict

gps_locations = [[2,3], [2,4], [2,10], [3,11], [4,12], [3,1], [2,2], [1,1], [5,12]]

def compute_distance_between_two_locations(location1, location2):
    distance = sqrt((location1[0]-location2[0])**2 + (location1[1]-location2[1])**2)
    distance = int(round(distance))
    return distance

def find_and_update_list_that_already_has_this_location(distance_to_locations_dict,
                                                        distance,
                                                        location1,
                                                        location2):
    list_of_locations = distance_to_locations_dict[distance]
    found_a_sub_list = False
    for index in range(len(list_of_locations)):
        sub_list = list_of_locations[index]
        if location1 in sub_list:
            sub_list.append(location2)
            list_of_locations[index] = sub_list
            found_a_sub_list = True
            break
        elif location2 in sub_list:
            sub_list.append(location1)
            list_of_locations[index] = sub_list
            found_a_sub_list = True
            break
    if not found_a_sub_list:
        list_of_locations.append([location1, location2])
    distance_to_locations_dict[distance] = list_of_locations

def prepare_dispatch_list(distance_to_locations_dict):
    dispatch_list = []
    locations_in_dispatch_list = []
    for key, list_of_destinations in distance_to_locations_dict.items():
        print("Distance = {}, list = {}".format(key,list_of_destinations))
        for destinations_group in list_of_destinations:
            dispatch=[]
            for location in destinations_group:
                if location not in locations_in_dispatch_list:
                    dispatch.append(location)
            if len(dispatch):
                dispatch_list.append(dispatch)
                locations_in_dispatch_list += dispatch
    return dispatch_list

def assign_dispatch_list_to_trucks(dispatch_list, trucks):
    dispatch_list_output = []
    if len(dispatch_list) >= trucks:
        for index in range(len(trucks)):
            dispatch_list_output.append(dispatch_list[index])
    else:
        running_count = 0
        current_dispatch_list_index = 0
        while running_count < trucks and \
                current_dispatch_list_index < len(dispatch_list):
            current_list = dispatch_list[current_dispatch_list_index]
            if len(current_list) > 4:
                dispatch_list_output.append(current_list[:4])
                dispatch_list_output.append(current_list[4:])
                running_count += 2
            else:
                dispatch_list_output.append(current_list)
                running_count += 1
            current_dispatch_list_index += 1
    return dispatch_list_output

def dispatch_trucks_to_destinations(gps_locations, truck_count):
    dispatch_list = []

    if truck_count <= 0 or len(gps_locations) == 0:
        return dispatch_list

    sorted_locations = deque(sorted(gps_locations))
    distance_to_locations_dict = defaultdict(list)
    print("sorted_locations={}".format(sorted_locations))
    for index in range(len(sorted_locations)):
        for index2 in range(index+1,len(sorted_locations)):
            distance = compute_distance_between_two_locations(sorted_locations[index],
                                                              sorted_locations[index2])
            locations_list = distance_to_locations_dict[distance]
            if not len(locations_list):
                distance_to_locations_dict[distance].append([sorted_locations[index],
                                      sorted_locations[index2]])
            else:
                find_and_update_list_that_already_has_this_location(distance_to_locations_dict,
                                                                    distance,
                                                                    sorted_locations[index],
                                                                    sorted_locations[index2])
    dispatch_list = prepare_dispatch_list(distance_to_locations_dict)
    dispatch_list_final = assign_dispatch_list_to_trucks(dispatch_list, truck_count)
    return dispatch_list_final

if __name__ == "__main__":
    dispatch_trucks = dispatch_trucks_to_destinations(gps_locations,5)
    print("dispatch_trucks={}".format(dispatch_trucks))