# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    index_a = 0
    index_b = 0
    for i in range(len(merged_arr)):
        if index_a > len(arrA) - 1:
            merged_arr[i] = arr[index_b]
            index_b += 1
        elif index_b > len(arrB) -1:
            merged_arr[i] = arrA[index_a]
            index_a += 1
        else:
            if arrA[index_a] > arrB[index_b]:
                merged_arr[i] = arrB[index_b]
                index_b += 1
            else:
                merged_arr[i] = arrA[index_a]
                index_a += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    middle = len(arr) // 2
    left_side = arr[:middle]
    right_side = arr[middle:]

    if len(left_side) > 1:
        left_side = merge_sort(left_side)

    if len(right_side) > 1:
        right_side = merge_sort(right_side)

    arr = merge(left_side, right_side)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
