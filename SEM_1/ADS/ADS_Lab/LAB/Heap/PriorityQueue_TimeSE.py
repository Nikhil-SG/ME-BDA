class Task:
    def __init__(self, task_id, priority, execution_time, deadline):
        self.task_id = task_id
        self.priority = priority
        self.execution_time = execution_time
        self.deadline = deadline

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

def schedule_tasks(start_time, end_time, tasks):
    pq = PriorityQueue()

    for task in tasks:
        pq.push(task)

    current_time = start_time
    results = []

    while not pq.is_empty():
        task = pq.pop()

        if current_time + task.execution_time <= end_time:
            waiting_time = current_time
            turnaround_time = waiting_time + task.execution_time
            current_time += task.execution_time

            results.append({
                'task_id': task.task_id,
                'priority': task.priority,
                'execution_time': task.execution_time,
                'deadline': task.deadline,
                'waiting_time': waiting_time,
                'turnaround_time': turnaround_time,
                'is_missed': turnaround_time > task.deadline
            })
        else:
            # If we can't execute the task within the allowed time, still add it to results
            results.append({
                'task_id': task.task_id,
                'priority': task.priority,
                'execution_time': task.execution_time,
                'deadline': task.deadline,
                'waiting_time': current_time,
                'turnaround_time': current_time + task.execution_time,
                'is_missed': (current_time + task.execution_time) > task.deadline
            })
        
    return results

if __name__ == "__main__":
    tasks = [
        Task("T1", 5, 3, 10),
        Task("T2", 10, 1, 2),
        Task("T3", 7, 2, 5),
        Task("T4", 3, 4, 12)
    ]

    start_time = 0  
    end_time = 5

    results = schedule_tasks(start_time, end_time, tasks)

    for result in results:
        print(f"Task ID: {result['task_id']}, "
              f"Waiting Time: {result['waiting_time']}, "
              f"Turnaround Time: {result['turnaround_time']}, "
              f"Deadline: {result['deadline']}, "
              f"Missed Deadline: {'Yes' if result['is_missed'] else 'No'}")
