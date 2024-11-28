from SimQueue import SimpleQueue
from LimQueue import LimitedQueue
from FlexiQueue import FlexiQueue

def main():
    # Test SimpleQueue
    print("Testing SimpleQueue:")
    queue = SimpleQueue()
    
    print("Initial queue:", queue)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueues:", queue)
    print("Front item:", queue.peek())
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())
    print("Queue after dequeues:", queue)
    print("Is the queue empty?", queue.is_empty())
    print("Queue size:", queue.size())
    print()

    # Test LimitedQueue
    print("Testing LimitedQueue:")
    max_size = 3
    queue = LimitedQueue(max_size)
    print("Initial queue:", queue)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueues:", queue)
    queue.enqueue(40)  
    print("Front item:", queue.peek())
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())
    print("Queue after dequeues:", queue)
    queue.enqueue(50)
    queue.enqueue(60)
    print("Queue after additional enqueues:", queue)
    print("Is the queue empty?", queue.is_empty())
    print("Is the queue full?", queue.is_full())
    print("Queue size:", queue.size())
    print()

    # Test FlexiQueue
    print("Testing FlexiQueue:")
    queue = FlexiQueue()
    print("Initial queue:", queue)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print("Queue after enqueues:", queue)
    print("Front item:", queue.peek())
    print("Dequeued item:", queue.dequeue())
    print("Dequeued item:", queue.dequeue())
    print("Queue after dequeues:", queue)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)
    print("Queue after additional enqueues:", queue)
    print("Is the queue empty?", queue.is_empty())
    print("Queue size:", queue.queue_size())

if __name__ == "__main__":
    main()
