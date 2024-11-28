class SimpleQueue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
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
