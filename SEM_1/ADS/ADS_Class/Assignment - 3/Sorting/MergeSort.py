def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def main():
    arr_asc = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr_asc)

    merge_sort(arr_asc)
    print("Sorted array by Merge Sort :", arr_asc)

    arr_runtime = list(map(int, input("Enter numbers separated by space : ").split()))

    merge_sort(arr_runtime)
    print("Sorted array by Merge Sort :", arr_runtime)

if __name__ == '__main__':
    main()
