# TO-DO: complete the helpe function below to merge 2 sorted arrays

###Objective: (split then merge)
    # 1) Split all lists into smaller lists until 1 or 0 remains (recursively)

    # 2) take all the single split numbers and put them back together

    # Step 2) hints: 
    #    when putting back together write an algorithem check 2 arrays at a time 
    #    and (sort / merge to less arrays)
    #    merge the lists into one list and return
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    ## Take both arrays as merged array and loop over both
    for i in arrA, arrB:
        
        print(i)
        ## Take both values of the current lowest index
        
        ## Compare both values of the current index 
        ## and place the lower in current index
        ## Increase value not chosen by 1 and compare



    # TO-DO
    print(merged_arr)
    return merged_arr

merge([2,3,5],[1,4,7])
# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    return arr


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
