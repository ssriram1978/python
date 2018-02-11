#here is the array that is all jumbled up
array=[4,6,2,7,1,8,9,3,5]
#find the length of the array
length=len(array)
print("length=" + str(length))
for index in range(length):
    print(str(index) + " element in array is "+  str(array[index]))
print("Before bubble sort")
print(array)
#i am starting a for loop to iterate all the the elenents
for i in range(length-1):
    #i am starting an inner loop to iterate all the elements upto the last but one for the outer loop.
    for j in range(length-i-1):
        #check if the content of array at index j is greater than the content of array at index j+1
        if array[j] > array[j+1]:
            #swap the elements array[j] and array[j+1]
            # i take a back up copy of array[j] in a temp variable
            temp=array[j]
            # i overwrite array at index j with the content of j+1
            array[j]=array[j+1]
            # i overwrite array at index j+1 with the content of temp variable
            array[j+1]=temp
print("After bubble sort")
print(array)
