def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

def main():
    # Test case for ascending order
    arr_asc = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr_asc)

    arr_asc_sorted = quick_sort(arr_asc)
    print("Sorted array by Quick Sort :", arr_asc_sorted)

    # Test case with input provided at runtime
    arr_runtime = list(map(int, input("Enter numbers separated by space: ").split()))

    arr_runtime_sorted_asc = quick_sort(arr_runtime)
    print("Sorted array by Quick Sort :", arr_runtime_sorted_asc)

if __name__ == '__main__':
    main()
