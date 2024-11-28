class MinHeapDesc:
    def __init__(self):
        self.heap = []

    def add(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def get_min(self):
        if not self.heap:
            raise IndexError("Heap is empty.")
        return self.heap[0]

    def extract_min(self):
        if not self.heap:
            raise IndexError("Heap is empty.")
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        self._heapify_down(0)           # Restore heap property
        return min_value

    def count(self):
        return len(self.heap)

    def is_heap_order(self):
        n = len(self.heap)
        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and self.heap[i] > self.heap[left]:
                return False
            if right < n and self.heap[i] > self.heap[right]:
                return False
        return True

    def sort_descending(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.extract_min())
        return sorted_list[::-1]  # Reverse to get descending order

    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def _heapify_down(self, index):
        n = len(self.heap)
        while index < n:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            
            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

if __name__ == "__main__":
    min_heap = MinHeapDesc()
    elements_to_add = [10, 20, 5, 30, 15, 25, 35, 40]
    
    for element in elements_to_add:
        min_heap.add(element)
            
    print("Count of elements:", min_heap.count())  
    print("Sorted in descending order:", min_heap.sort_descending())  

