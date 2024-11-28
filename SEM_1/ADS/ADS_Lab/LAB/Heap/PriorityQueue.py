class Task:
    def __init__(self, task_id, priority, execution_time):
        self.task_id = task_id
        self.priority = priority  
        self.execution_time = execution_time

class PriorityQueue:
    def __init__(self):
        self.tasks = []
        
    def push(self, task):
        self.tasks.append(task)
        self.tasks.sort(key=lambda x: x.priority, reverse=True)
        
    def pop(self):
        return self.tasks.pop(0) if self.tasks else None
    
    def is_empty(self):
        return len(self.tasks) == 0

def schedule_tasks(tasks):
    pq = PriorityQueue()

    for task in tasks:
        pq.push(task)

    current_time = 0
    results = []

    while not pq.is_empty():
        task = pq.pop()
        
        waiting_time = current_time
        turnaround_time = waiting_time + task.execution_time
        current_time += task.execution_time

        results.append({
            'task_id': task.task_id,
            'priority': task.priority,
            'execution_time': task.execution_time,
            'waiting_time': waiting_time,
            'turnaround_time': turnaround_time
        })
        
    return results

if __name__ == "__main__":
    tasks = [
        Task("T1", 5, 3),
        Task("T2", 10, 1),
        Task("T3", 7, 2),
        Task("T4", 3, 4)
    ]

    results = schedule_tasks(tasks)

    for result in results:
        print(f"Task ID: {result['task_id']}, "
              f"Waiting Time: {result['waiting_time']}, "
              f"Turnaround Time: {result['turnaround_time']}")
