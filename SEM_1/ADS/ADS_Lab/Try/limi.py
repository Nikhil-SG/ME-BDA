class LimStack:
    def __init__(self, max_size):
        self.data = []
        self.max_size = max_size

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def is_full(self):
        return len(self.data) >= self.max_size

    def push(self, ele):
        if not self.is_full():
            self.data.append(ele)
        else:
            print("Stack is full. Cannot push.")

    def pop(self):
        if not self.is_empty():
            return self.data.pop()
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            return self.data[-1]
        else:
            print("Stack is empty. Nothing to peek.")

    def __str__(self):
        return f"Stack: {self.data}, Max size: {self.max_size}, Current size: {self.size()}"

def main():
    stk = LimStack(max_size=5)
    stk.push(1)
    stk.push(2)
    stk.push(3)
    stk.push(4)
    stk.push(5)
    stk.push(6) 
    print(stk) 
    assert stk.peek() == 5 
    assert stk.size() == 4  
    popped_element = stk.pop()
    assert popped_element == 5 
    assert stk.size() == 4 
    print(stk)  

if __name__ == '__main__':
    main()
