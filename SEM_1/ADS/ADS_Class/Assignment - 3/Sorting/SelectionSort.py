def selection_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def selection_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i], arr[max_index] = arr[max_index], arr[i]

def main():
    arr_asc = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr_asc)

    selection_sort_ascending(arr_asc)
    print("Sorted array in Ascending order by Selection Sort :", arr_asc)
    
    selection_sort_descending(arr_asc)
    print("Sorted array in Descending order by Selection Sort :", arr_asc)

    arr_runtime = list(map(int, input("Enter numbers separated by space : ").split()))

    selection_sort_ascending(arr_runtime)
    print("Sorted array in Ascending order by Selection Sort :", arr_runtime)

    selection_sort_descending(arr_runtime)
    print("Sorted array in Descending order by Selection Sort :", arr_runtime)

if __name__ == '__main__':
    main()
