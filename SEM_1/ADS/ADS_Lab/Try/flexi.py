class flexi:
    default_size = 2

    def __init__(self):
        self.data = [None] * flexi.default_size
        self.count = 0
        self.front = 0

    def isempty(self):
        return self.count == 0

    def size(self):
        return self.count

    def first(self):
        if self.isempty():
            raise IndexError("Queue is empty")
        return self.data[self.front]
    
    def enqueue(self, ele):
        if self.count == len(self.data):
            self.resize(len(self.data) * 2)

        idx = (self.front + self.count) % len(self.data)
        self.data[idx] = ele
        self.count += 1
    
    def dequeue(self):
        if not self.isempty():
            ele = self.data[self.front]
            self.data[self.front] = None
            self.count -= 1
            self.front = (self.front + 1) % len(self.data)
            return ele
        else:
            raise IndexError("Queue is empty")
        
    def resize(self, new_size):
        old_data = self.data
        old_size = len(old_data)
        self.data = [None] * new_size
        walk = self.front
        for i in range(self.count):
            self.data[i] = old_data[walk]
            walk = (walk + 1) % old_size
        self.front = 0

def main():
        # Enqueue elements
    queue = flexi()
  
    queue.enqueue(1)
 
    queue.enqueue(2)
  
    queue.enqueue(3)

    queue.enqueue(4)

    queue.enqueue(5)

    queue.enqueue(6)
  
    queue.enqueue(7)

    queue.enqueue(8)

    queue.enqueue(9)

    queue.enqueue(10)

    queue.enqueue(11)
   

    # Dequeue elements
    print("\nDequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())
    print("Dequeued:", queue.dequeue())

    # Enqueue more elements
    queue.enqueue(12)
    queue.enqueue(13)
    queue.enqueue(14)
    queue.enqueue(15)
    
    print("\nCurrent queue state:")
    print(f"First element: {queue.first()}")
    print(f"Queue size: {queue.size()}")
    print(f"Is queue empty: {queue.isempty()}")

if __name__ == '__main__':
    main()
