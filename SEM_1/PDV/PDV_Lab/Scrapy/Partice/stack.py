class unlimtedstack:
        def __init__(self):
            self.data = []
            self.count = 0

        def isempty(self):
            return self.count == 0
        
        def count(self):
            return self.count
        
        def push(self,ele):
            self.data.append(ele)
            self.count+=1

        def peek(self):
            if not self.isempty():
                return self.data[-1]
            else:
                return None
            
        def pop(self):
            if not self.isempyt():
                self.count-=1
                self.data.pop()
            else:
                return None
        
        def __str__(self):
            return str(self.data)

if __name__ == 'main':
    stk = unlimtedstack()
    stk.push(1)
    print(stk)

