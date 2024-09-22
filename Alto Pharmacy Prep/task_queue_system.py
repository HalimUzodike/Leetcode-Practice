# Task Queue System

"""
This implementation provides a basic task queue system with the following features:

Task Creation: Tasks are created with a function and its arguments.
Task Queueing: Tasks are added to a queue for processing.
Asynchronous Processing: Multiple worker threads process tasks concurrently.
Status Tracking: Each task has a status (PENDING, RUNNING, COMPLETED, FAILED).
Result Retrieval: Completed task results can be retrieved.
"""

import time
import uuid
from enum import Enum
from collections import deque
from threading import Thread, Event
from typing import Callable, Dict, Any

class TaskStatus(Enum):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class Task:
    def __init__(self, func: Callable, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.status = TaskStatus.PENDING
        self.result = None
        self.error = None

class TaskQueue:
    def __init__(self, num_workers: int = 2):
        self.queue = deque()
        self.tasks: Dict[str, Task] = {}
        self.num_workers = num_workers
        self.workers = []
        self.stop_event = Event()

    def enqueue(self, func: Callable, *args, **kwargs) -> str:
        task = Task(func, *args, **kwargs)
        self.queue.append(task)
        self.tasks[task.id] = task
        return task.id

    def get_task_status(self, task_id: str) -> TaskStatus:
        return self.tasks[task_id].status if task_id in self.tasks else None

    def get_task_result(self, task_id: str) -> Any:
        task = self.tasks.get(task_id)
        if task and task.status == TaskStatus.COMPLETED:
            return task.result
        return None

    def start(self):
        for _ in range(self.num_workers):
            worker = Thread(target=self._worker)
            worker.start()
            self.workers.append(worker)

    def stop(self):
        self.stop_event.set()
        for worker in self.workers:
            worker.join()

    def _worker(self):
        while not self.stop_event.is_set():
            try:
                task = self.queue.popleft()
            except IndexError:
                # Queue is empty, wait a bit and try again
                time.sleep(0.1)
                continue

            task.status = TaskStatus.RUNNING
            try:
                task.result = task.func(*task.args, **task.kwargs)
                task.status = TaskStatus.COMPLETED
            except Exception as e:
                task.error = str(e)
                task.status = TaskStatus.FAILED

# Example usage
def example_task(x: int, y: int) -> int:
    time.sleep(2)  # Simulate a time-consuming task
    return x + y

if __name__ == "__main__":
    task_queue = TaskQueue(num_workers=2)
    task_queue.start()

    # Enqueue tasks
    task_ids = [
        task_queue.enqueue(example_task, 1, 2),
        task_queue.enqueue(example_task, 3, 4),
        task_queue.enqueue(example_task, 5, 6),
    ]

    # Check task status and results
    for task_id in task_ids:
        while task_queue.get_task_status(task_id) != TaskStatus.COMPLETED:
            print(f"Task {task_id} status: {task_queue.get_task_status(task_id)}")
            time.sleep(0.5)

        result = task_queue.get_task_result(task_id)
        print(f"Task {task_id} completed with result: {result}")

    task_queue.stop()


"""
Potential Improvements:

This implementation is a good starting point for a task queue system.
Depending on your specific requirements, you might want to consider the following enhancements:


Persistence: Store tasks and their status in a database for durability.
Distributed processing: Extend the system to work across multiple machines.
Priority queues: Add support for task priorities.
Task dependencies: Allow tasks to depend on other tasks' completion.
Retry mechanism: Automatically retry failed tasks.
Monitoring and logging: Add more comprehensive logging and monitoring capabilities.
Web interface: Create a web-based dashboard for managing and monitoring tasks



One thing to note is that while deque operations are atomic,
there's a small chance of race conditions when checking if the queue is empty and then trying to pop from it.
In a more robust implementation, you might want to add a lock around these operations if absolute thread-safety is required.
"""