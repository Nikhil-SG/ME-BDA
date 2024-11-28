class MaxHeapAsc:
    def __init__(self):
        self.heap = []

    def add(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap is empty.")
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_value

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def heap_sort(self):
        sorted_list = []
        original_size = len(self.heap)

        for _ in range(original_size):
            sorted_list.append(self.extract_max())

        return sorted_list[::-1]  

if __name__ == "__main__":
    max_heap = MaxHeapAsc()
    elements_to_add = [10, 20, 5, 30, 15, 25, 35, 40]
    
    for element in elements_to_add:
        max_heap.add(element)
    sorted_elements = max_heap.heap_sort()
    print("Sorted elements in ascending order:", sorted_elements)
