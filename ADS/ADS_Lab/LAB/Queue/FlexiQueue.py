class FlexiQueue:
    def __init__(self, initial_capacity=10, shrink_threshold=0.25, expand_threshold=0.75):
        self.queue = [None] * initial_capacity
        self.front = 0
        self.size = 0
        self.capacity = initial_capacity
        self.shrink_threshold = shrink_threshold
        self.expand_threshold = expand_threshold

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            self._resize(self.capacity * 2)
        end = (self.front + self.size) % self.capacity
        self.queue[end] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear reference
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        
        # Shrink the queue if it's too empty
        if self.size > 0 and self.size < self.capacity * self.shrink_threshold:
            self._resize(max(self.capacity // 2, 10))
        
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.queue[self.front]

    def queue_size(self):
        return self.size

    def _resize(self, new_capacity):
        new_queue = [None] * new_capacity
        for i in range(self.size):
            new_queue[i] = self.queue[(self.front + i) % self.capacity]
        self.queue = new_queue
        self.front = 0
        self.capacity = new_capacity

    def __str__(self):
        if self.is_empty():
            return "Queue is empty."
        items = []
        for i in range(self.size):
            items.append(self.queue[(self.front + i) % self.capacity])
        return str(items)
