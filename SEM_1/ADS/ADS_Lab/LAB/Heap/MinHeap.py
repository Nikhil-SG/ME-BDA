class MinHeap:
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
        self.heap[0] = self.heap.pop()  
        self._heapify_down(0)           
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
    min_heap = MinHeap()
    min_heap.add(10)
    min_heap.add(20)
    min_heap.add(15)
    min_heap.add(30)
    min_heap.add(45)
    min_heap.add(35)
    min_heap.add(22)
    min_heap.add(18)
    min_heap.add(25)
    min_heap.add(5)
    min_heap.add(5)
    min_heap.add(3)
    min_heap.add(8)
    min_heap.add(1)

    print("Minimum element:", min_heap.get_min()) 
    print("Extracted minimum:", min_heap.extract_min())  
    print("New minimum after extraction:", min_heap.get_min())  
    print("Count of elements:", min_heap.count())  
    print("Is valid heap:", min_heap.is_heap_order())  
