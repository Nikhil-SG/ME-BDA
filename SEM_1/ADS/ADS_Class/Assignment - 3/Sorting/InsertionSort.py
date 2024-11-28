def insertion_sort_ascending(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i -1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -=1
        arr[j +1] = key

def insertion_sort_descending(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i- 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j-= 1
        arr[j+ 1] = key

def main():
    arr_asc = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr_asc)

    insertion_sort_ascending(arr_asc)
    print("Sorted array in Ascending order by Insertion Sort :", arr_asc)

    insertion_sort_descending(arr_asc)
    print("Sorted array in Descending order by Insertion Sort :", arr_asc)

    arr_runtime = list(map(int, input("Enter numbers separated by space : ").split()))

    insertion_sort_ascending(arr_runtime)
    print("Sorted array in Ascending order by Insertion Sort :", arr_runtime)

    insertion_sort_descending(arr_runtime)
    print("Sorted array in Descending order by Insertion Sort :", arr_runtime)

if __name__ == '__main__':
    main()
