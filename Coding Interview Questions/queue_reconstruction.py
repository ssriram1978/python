"""
Suppose you have a random list of people standing in a queue.
Each person is described by a pair of integers (h, k), where h is the height of the person and
k is the number of people in front of this person who have a height greater than or equal to h.
Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""

"""
Sort the array based on height in descending order and save it in a sorted stack.
Create an output stack with all zeros of length sizeof array.
For every element in the sorted stack:
    Extract the location (second sub-element) from the element.
    If there are no items in the output stack at the desired location:
        Just replace 0 with this current element
    Else
        Insert this current element into the output stack at the desired location.
        This would result in a right shift of the sorted stack so do a pop() to get rid off the item which is 0.
Return the output stack.
"""
#[7,0],[7,1]
#[7,0],[6,1],[7,1]
#[5,0],[7,0],[5,2],[6,1],[7,1]
#[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]
from collections import deque
input=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
sort_based_on_height=sorted(input,key=lambda x: x[0],reverse=True)
print(sort_based_on_height)
stack_of_people=[0]*len(sort_based_on_height)
for index in range(len(sort_based_on_height)):
    people=sort_based_on_height[index]
    #if there are no persons at the specified location, then, make the person stand at the specified location.
    if stack_of_people[people[1]]==0:
        stack_of_people[people[1]]=people
    else:
        #insert this person at the specified location which is the total number of persons standing before him.
        stack_of_people.insert(people[1],people)
        #make sure to remove the trailing zero in the stack because you already inserted an element which
        #caused the zeros to right shift in the list.
        stack_of_people.pop()
    print(stack_of_people)

print(stack_of_people)
