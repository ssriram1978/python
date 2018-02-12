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
from collections import deque

input=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]

sort_based_on_height=sorted(input,key=lambda x: x[0],reverse=True)
"""
sort the array based on height and save it in a sorted stack.
create a dummy stack with all zeros of size input.
in a loop that runs until there are no elements in the sorted stack
    pop all element which have the same height from the sorted stack
    let h be the location of the element popped from the stack.
    if item in dummy stack is 0, then, replace it with the element popped from the stack.
    if item in dummy stack is non zero, then, insert the popped element at this location.
"""
#[7,0],[7,1]
#[7,0],[6,1],[7,1]
#[5,0],[7,0],[5,2],[6,1],[7,1]
#[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]
print(sort_based_on_height)
stack_of_people=[0]*len(sort_based_on_height)
for index in range(len(sort_based_on_height)):
    people=sort_based_on_height[index]
    if stack_of_people[people[1]]==0:
        stack_of_people[people[1]]=people
    else:
        stack_of_people.insert(people[1],people)
        stack_of_people.pop()
    print(stack_of_people)

print(stack_of_people)
