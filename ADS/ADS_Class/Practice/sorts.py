def Mergesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def Selectionsort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j] > arr[min]:
                min = j
        arr[i] , arr[min] = arr[min], arr[i]

def Insertionsort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        MergeSort(left)
        MergeSort(right)
        
        i = j = k =0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(arr):
            arr[k] = right[j]
            j += 1
            k += 1

def QuickSort(arr):
    start = 0
    end = len(arr) - 1
    quick(arr,start,end)
        
def quick(arr,start,end):
    if start < end:
        mid = partition(arr,start,end)
        quick(arr,start,mid-1)
        quick(arr,mid+1,end)

def partition(arr,start,end):
    up = start
    down = end
    pivot = arr[up]
    while up <= down:
        while up<= down and arr[up] < pivot:
            up += 1
        while up <= down and arr[down] > pivot:
            down -= 1
        if up <= down:
            arr[up], arr[down] = arr[down], arr[up]
        
    arr[start], arr[down] = arr[down], arr[start]
    return down
