# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    index_length =  range(0, len(arr) - 1)

    # loop through n-1 elements
    for i in index_length:
        cur_index = i

        for j in range( i + 1 , len(arr)):
            if arr[j] < arr[cur_index]:
                cur_index = j

        if cur_index != i:
            arr[cur_index], arr[i] = arr[i], arr[cur_index]

        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

    return arr


print(selection_sort([2,34,8,1]))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    index_length = len(arr) -1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, index_length):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

print(bubble_sort([2,34,8,1]))
'''
STRETCH: implement the Counting Sort function below

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
