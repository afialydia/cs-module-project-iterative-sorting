def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    start = 0
    stop = len(arr) - 1

    while start <= stop:
        midpoint = start + (stop - start)//2
        midpoint_val = arr[midpoint]
        if midpoint_val == target:
            return midpoint
        elif target <midpoint_val:
            stop = midpoint - 1
        else: 
            start = midpoint + 1

    return -1  # not found

print(binary_search([1,2,4,6], 6))