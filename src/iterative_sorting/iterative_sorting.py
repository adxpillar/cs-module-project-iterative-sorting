# TO-DO: Complete the selection_sort() function below
# insertion sort or selection sort 
# Find the list[0] as first sorted and create boundry
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        boundry_index = i
        smallest_index = boundary_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
          # (hint, can do in 3 loc)
        # Your code here
        # iterate through the unsorted portion of the array 
        # finding the index of the smallest element in the unsorted portion

        for unsorted_index in range(boundary_index, len(arr)):
             # if we find a value < smallest_index element,
            # update our smallest_index variable 
            if arr[unsorted_index] < arr[smallest_index]:
                smallest_index = unsorted_index

        # TO-DO: swap
        # Your code here
        # we've found the smallest element in the unsorted portion 
        # swap it with the element right next to the boundary 

        arr[smallest_index],arr[boundary_index] = arr[boundary_index],arr[smallest_index]

    return arr



# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    # traverse the array
    # loop until no more swaps occur 
    swaps_occurred = True

    while swaps_occurred:
        swaps_occurred = False 

        for i in range(0, len(arr)-1):
            # compare two elements 
            if arr[i] > arr[i+1]:
                # swaps them if the two elements aren't in order 
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps_occurred = True
    return arr

# bubble sort solution without bool
def bubble_sort_two(arr):
    end_index= len(arr)-1
    while end_index > 0:
        for i in range(0, end_index):
            cur_index= i
            next_index= i+1
            if arr[cur_index] > arr[next_index]:
                swap= arr[cur_index]
                arr[cur_index]= arr[next_index]
                arr[next_index]= swap
        end_index-= 1


# recursive solution for bubble sort 

def bubble_sort(arr, unsorted_length):
    # find the unsorted_length 
    # iterate through the arr
    # figure out, starting from the right side, how many elements 
    # of the array are sorted 
    
    # recursive implementation of bubble sort 
    # base case 
    # what's the length of the unsorted portion of our array? 
    # once we get to an empty unsorted portion, then everything is sorted 
    # how are we moving closer to our base case? 
    for i in range(0, unsorted_length - 1):
        # compare two elements 
        if arr[i] > arr[i+1]:
            # swaps them if the two elements aren't in order 
            arr[i], arr[i+1] = arr[i+1], arr[i]

    # we've done one iteration of the swapping, check to see 
    # if there's more sorting to do 
    if unsorted_length > 0:
        bubble_sort(arr, unsorted_length - 1)


'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
