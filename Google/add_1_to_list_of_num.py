"""
Given a list, start from the end of the list.
If plus one results in a carry, then, set the end element to 0 and remember the carry.
Traverse from back to front and always remember to add the carry to the next element and remember the carry as told in step1
Once you walked all the way to the front and this also resulted in a carry, then insert 1 at index 0 into the list.
"""

def add_one_to_number(list_num):
    if list_num == None:
        return
    if list_num[len(list_num)-1] == 9:
        #you will have to carry over to the next digit
        #do this in a for loop until you are all done carrying over the digit.
        carry_over_from_prev_num = True
        index=len(list_num)-1
        while(carry_over_from_prev_num == True and index >=0 ):
            if list_num[index] == 9:
                #set it to 0
                list_num[index]=0
            else:
                #add one to the current number and reset the boolean flag
                list_num[index]+=1
                carry_over_from_prev_num = False
            #make sure to decrement the while loop index
            index-=1
        #if the carry over bool is true, then insert 1 to the front of the list
        if carry_over_from_prev_num == True and index == -1:
            list_num.insert(0,1)
    else:
        #just add +1 to the end of the digit and return it
        list_num[len(list_num)-1]+=1

    return list_num

list=[9,9,9,9]
add_one_to_number(list)
print(list)
