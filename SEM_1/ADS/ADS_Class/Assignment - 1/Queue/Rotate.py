from SimQueue import SimpleQueue

def rotate(queue):
    if queue.is_empty() or queue.size() == 1:
        return
    
    temp_list = []
    
    while not queue.is_empty():
        temp_list.append(queue.dequeue())
    
    while temp_list:
        queue.enqueue(temp_list.pop())

if __name__ == "__main__":
    queue = SimpleQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    
    print("Original Queue:", queue)  
    rotate(queue)
    print("Rotated Queue:", queue)  
