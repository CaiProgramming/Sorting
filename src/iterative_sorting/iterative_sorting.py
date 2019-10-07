# TO-DO: Complete the selection_sort() function below
def selection_sort( arr ):
    # loop through n-1 elements
    for low in range(0, len(arr)):
        min_dex = low
        for i in range(low+ 1, len(arr)):
            if(arr[min_dex] > arr[i]):
                min_dex = i

        arr[low], arr[min_dex] = arr[min_dex], arr[low]
    return arr


print(selection_sort([9,8,7,6,5,4,3,2,1]))
# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swap = 1
    while swap:
        swap = 0
        for i in range(0, len(arr) - 1):
            if(arr[i] > arr[i+1]):
                print(arr)
                print(i)
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = 1
    return arr
# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
