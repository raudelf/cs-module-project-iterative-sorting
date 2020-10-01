def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    min = 0
    max = len(arr) - 1

    while min <= max:
        middle = (min+max)//2
        
        if target < arr[middle]:
            max = middle - 1

        elif target > arr[middle]:
            min = middle + 1

        else:
            return middle 

    return -1  # not found
