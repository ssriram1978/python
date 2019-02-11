

def quick_sort(list_of_numbers):
    quick_sort_recurse(list_of_numbers,0,len(list_of_numbers)-1)

def quick_sort_recurse(list_of_numbers, starting_index, ending_index):
    start = starting_index
    end = ending_index
    if start < end:
        pivot = start + (end-start)//2
        if pivot == start and list_of_numbers[start] > list_of_numbers[end]:
                list_of_numbers[start], list_of_numbers[end] = list_of_numbers[end], list_of_numbers[start]
                return
        while start < pivot and end > pivot:
            while start < pivot and list_of_numbers[start] < list_of_numbers[pivot]:
                start+=1
            while end > pivot and list_of_numbers[end] > list_of_numbers[pivot]:
                end-=1
            if list_of_numbers[start] > list_of_numbers[pivot] and list_of_numbers[end] < list_of_numbers[pivot]:
                list_of_numbers[start], list_of_numbers[end] = list_of_numbers[end], list_of_numbers[start]
            start+=1
            end-=1
        quick_sort_recurse(list_of_numbers, starting_index, pivot)
        quick_sort_recurse(list_of_numbers, pivot+1,ending_index)
        



list_of_numbers =[x for x in range(10000,-1,-1)]
quick_sort(list_of_numbers)
#print("after sorting, list_of_numbers={}".format(list_of_numbers))
print("after sorting, len(list_of_numbers)={}".format(len(list_of_numbers)))