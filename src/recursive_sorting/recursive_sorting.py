# TO-DO: complete the helpe function below to merge 2 sorted arrays

def merge( arrA, arrB ):
    print(arrA, arrB)
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    ## Take both arrays as merged array and loop over both
    for i in range(0, elements):
        if len(arrB) == 0:
            merged_arr[i] = arrA[0]
            del arrA[0]
        elif len(arrA) == 0:
            merged_arr[i] = arrB[0]
            del arrB[0]
        else:
            if arrA[0] < arrB[0]:
                merged_arr[i] = arrA[0]
                del arrA[0]
            elif arrB[0] < arrA[0]:
                merged_arr[i] = arrB[0]
                del arrB[0]

    # TO-DO
    print('here',merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
###Objective: (split then merge)
    # 1) Split all lists into smaller lists until 1 or 0 remains (recursively)

    # 2) take all the single split numbers and put them back together

    # Step 2) hints: 
    #    when putting back together write an algorithem check 2 arrays at a time 
    #    and (sort / merge to less arrays)
    #    merge the lists into one list and return
def merge_sort( arr ):
    # TO-DO
    print('should be an array...',arr)
    if len(arr) > 1:
        half = int(len(arr)/2)
        arrA = merge_sort(arr[0:half])
        arrB = merge_sort(arr[half:len(arr)])
        print('should be TWO array...',arrA, arrB)
        return merge(arrA, arrB)

    return arr

merge_sort([1, 5, 8, 4, 2, 9, 6, 3])
# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
