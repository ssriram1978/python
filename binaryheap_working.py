# Python program for implementation of heap Sort

# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        print("Before swapping")
        print(arr)
        print("\nheapify:swapping %d" % (arr[i]) + "and %d" % (arr[largest]))
        temp=arr[i]
        arr[i]=arr[largest]
        arr[largest]=temp
        # Heapify the root.
        heapify(arr, n, largest)
    print(arr)


# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
    half=n//2
    # Build a maxheap.
    for i in range(half, -1, -1):
        heapify(arr, half, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        print("Before swapping")
        print(arr)
        print("\nswapping %d"%(arr[i])+"and %d"%(arr[0]))
        temp=arr[i]
        arr[i]=arr[0]
        arr[0]=temp
        heapify(arr, i, 0)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i])