def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def main():
    # Test case for ascending order
    arr_asc = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr_asc)
    heap_sort(arr_asc)
    print("Sorted array by Heap Sort :", arr_asc)

    # Test case with input provided at runtime
    arr_runtime = list(map(int, input("Enter numbers separated by space: ").split()))
    heap_sort(arr_runtime)
    print("Sorted array by Heap Sort :", arr_runtime)

if __name__ == '__main__':
    main()
