# TO-DO: Complete the selection_sort() function below 

####### Steps to sort
        ## 1 Check first index
        ## 2 in the array and find the lowest value
        ## 3 change (swap) the index of the lowest value to the current index
        ## 4 Increase the current index ++ and repeat while len(arr) == true

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(1, len(arr)):
        ##?why are they setting the [i] value twice?
        ## 1 Check first index
        temp = arr[i]
        j = i
        while j > 0 and temp < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    print(arr)
    return arr

# selection_sort([1,5,3,4,2])
# TO-DO:  implement the Bubble Sort function below

## Bubble Sort:
## 1) grab the first 2 indices (current and current + 1)
## 2) compare the 2 indicies if the index on the right 
##    is less than the left swap the 2
## 3) perform the swaps until a pass with no swaps
def bubble_sort( arr ):
    for i in range(0, len(arr)-1):
        x = arr[i] #first index value to compare
        y = arr[i+1] #second index value to compare 

        # if first index is great than second swap them           
        if(x > y):
            arr[i+1] = x
            arr[i] = y
            
    print(arr)
    return arr

bubble_sort([2,1,5,3,4])
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr