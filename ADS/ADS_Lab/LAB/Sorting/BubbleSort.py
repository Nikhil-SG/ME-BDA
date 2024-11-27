def bubble_sort_ascending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
               
def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]<arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    arr_asc = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr_asc)

    bubble_sort_ascending(arr_asc)
    print("Sorted array in Ascending order by Bubble Sort :", arr_asc)

    bubble_sort_descending(arr_asc)
    print("Sorted array in Descending order by Bubble Sort :", arr_asc)

    arr_runtime = list(map(int, input("Enter numbers separated by space : ").split()))

    bubble_sort_ascending(arr_runtime)
    print("Sorted array in Ascending order by Bubble Sort :", arr_runtime)

    bubble_sort_descending(arr_runtime)
    print("Sorted array in Descending order by Bubble Sort :", arr_runtime)

if __name__ == '__main__':
    main()
