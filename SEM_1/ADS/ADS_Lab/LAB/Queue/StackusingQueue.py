from SimQueue import SimpleQueue
from UnlimitedStack import UnlimitedStack

class StackUsingSimpleQueue:
    def __init__(self):
        self.queue1 = SimpleQueue()
        self.queue2 = SimpleQueue()
    
    def push(self, x):
        self.queue1.enqueue(x)
    
    def pop(self):
        if self.queue1.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        
        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())
        
        popped_element = self.queue1.dequeue()
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return popped_element
    
    def top(self):
        if self.queue1.is_empty():
            print("Stack is empty. Cannot top.")
            return None
        
        while self.queue1.size() > 1:
            self.queue2.enqueue(self.queue1.dequeue())
        top_element = self.queue1.dequeue()
        self.queue2.enqueue(top_element)
        
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return top_element
    
    def empty(self):
        # Stack is empty if queue1 is empty
        return self.queue1.is_empty()

    def __str__(self):
        return str(self.queue1)

# Example usage
if __name__ == "__main__":
    # Using UnlimitedStack
    unlimited_stack = UnlimitedStack()
    unlimited_stack.stackPush(1)
    unlimited_stack.stackPush(2)
    print("UnlimitedStack top:", unlimited_stack.stackPeek())  
    print("UnlimitedStack pop:", unlimited_stack.stackPop())    
    print("UnlimitedStack empty:", unlimited_stack.isEmpty())    

    # Using StackUsingSimpleQueue
    stack = StackUsingSimpleQueue()
    stack.push(1)
    stack.push(2)
    print("StackUsingSimpleQueue top:", stack.top())    # Should print 2
    print("StackUsingSimpleQueue pop:", stack.pop())    # Should print 2
    print("StackUsingSimpleQueue empty:", stack.empty())  # Should print False
