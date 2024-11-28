class LimitedQueue:
    def __init__(self, max_size):
        """Initialize a queue with a maximum size."""
        self.queue = []
        self.max_size = max_size
    
    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0
    
    def is_full(self):
        """Check if the queue is full."""
        return len(self.queue) >= self.max_size
    
    def enqueue(self, item):
        """Add an item to the end of the queue if not full."""
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        self.queue.append(item)
    
    def dequeue(self):
        """Remove and return an item from the front of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        return self.queue.pop(0)
    
    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        return self.queue[0]
    
    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)
    
    def __str__(self):
        """Return a string representation of the queue."""
        if self.is_empty():
            return "Queue is empty."
        return str(self.queue)
