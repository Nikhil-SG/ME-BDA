class LimitedStack:
    def __init__(self, maxSize):
        self.data = []
        self.maxSize = maxSize

    def isEmpty(self):
        return len(self.data) == 0
    
    def isFull(self):
        return len(self.data) >= self.maxSize
    
    def stackCount(self):
        return len(self.data)
    
    def stackPush(self,ele):
        if not self.isFull():
            self.data.append(ele)
        else:
            raise OverflowError("Push to a full stack")

    def stackPop(self):
        if not self.isEmpty():
            return self.data.pop()
        else:
            raise IndexError("Pop from an empty stack")
    
    def stackPeek(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            raise IndexError("Peek from an empty stack")
        
    def __str__(self):
        return str(self.data)
    
