from UnlimitedStack import UnlimitedStack

class QueueUsingStacks:
    def __init__(self):
        self.stack_in = UnlimitedStack()
        self.stack_out = UnlimitedStack()
    
    def enqueue(self, item):
        self.stack_in.stackPush(item)
    
    def dequeue(self):
        if self.stack_out.isEmpty():
            while not self.stack_in.isEmpty():
                self.stack_out.stackPush(self.stack_in.stackPop())
        
        if self.stack_out.isEmpty():
            print("Queue is empty. Cannot dequeue.")
            return None
        
        return self.stack_out.stackPop()
    
    def peek(self):
        if self.stack_out.isEmpty():
            while not self.stack_in.isEmpty():
                self.stack_out.stackPush(self.stack_in.stackPop())
        
        if self.stack_out.isEmpty():
            print("Queue is empty. Cannot peek.")
            return None
        
        return self.stack_out.stackPeek()
    
    def is_empty(self):
        return self.stack_in.isEmpty() and self.stack_out.isEmpty()
    
    def __str__(self):
        if not self.stack_out.isEmpty():
            return str(self.stack_out.data[::-1] + self.stack_in.data)
        return str(self.stack_in.data[::-1])


if __name__ == "__main__":
    queue = QueueUsingStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    print("Queue peek:", queue.peek())    
    print("Queue dequeue:", queue.dequeue())    
    print("Queue is empty:", queue.is_empty())  
    print("Queue state:", queue)  
