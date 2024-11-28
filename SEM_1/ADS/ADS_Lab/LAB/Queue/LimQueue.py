class LimitedQueue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def is_full(self):
        return len(self.queue) >= self.max_size
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        self.queue.append(item)
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
    def __str__(self):
        if self.is_empty():
            return "Queue is empty."
        return str(self.queue)
