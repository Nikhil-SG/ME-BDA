from SimQueue import SimpleQueue

# Extend the SimpleQueue class to include the findMax method
def add_findMax_method():
    def findMax(self):
        if self.is_empty():
            print("Queue is empty. No maximum value.")
            return None
        
        temp_list = []
        max_value = float('-inf')

        while not self.is_empty():
            item = self.dequeue()
            temp_list.append(item)
            if item > max_value:
                max_value = item

        while temp_list:
            self.enqueue(temp_list.pop(0))
        
        return max_value
    
    SimpleQueue.findMax = findMax

# Add the findMax method to the SimpleQueue class
add_findMax_method()

def main():
    queue = SimpleQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(15)
    queue.enqueue(5)

    print("Original Queue:", queue) 
    
    max_value = queue.findMax()
    print("Maximum Value:", max_value) 

if __name__ == "__main__":
    main()
