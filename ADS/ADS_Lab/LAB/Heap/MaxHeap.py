class MaxHeap:
    def __init__(self):
        self.heap = []

    def add(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def get_max(self):
        if not self.heap:
            raise IndexError("Heap is empty.")
        return self.heap[0]

    def extract_max(self):
        if not self.heap:
            raise IndexError("Heap is empty.")
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return max_value

    def count(self):
        return len(self.heap)

    def is_heap_ordered(self):
        for i in range(len(self.heap)):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < len(self.heap) and self.heap[i] < self.heap[left]:
                return False
            if right < len(self.heap) and self.heap[i] < self.heap[right]:
                return False
        return True

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

if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.add(10)
    max_heap.add(20)
    max_heap.add(15)
    max_heap.add(30)
    max_heap.add(25)
    max_heap.add(5)
    max_heap.add(12)
    max_heap.add(8)
    max_heap.add(18)
    max_heap.add(22)
    max_heap.add(17)
    max_heap.add(28)
    max_heap.add(23)
    max_heap.add(35)
    max_heap.add(5)

    print("Max element:", max_heap.get_max())  
    print("Extracted max:", max_heap.extract_max())  
    print("Count of elements:", max_heap.count())  
    print("Is heap ordered?", max_heap.is_heap_ordered()) 