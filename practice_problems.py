"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    """
    Using a set is ideal here because sets store only unique values and provide O(1) average‑time
    lookup and insertion. As we iterate through the list, we check whether an element is already
    in the set; if so, we’ve found a duplicate. This approach runs in O(n) time and uses O(n)
    additional space.
    """
    seen = set()
    for pid in product_ids:
        if pid in seen:
            return True
        seen.add(pid)
    return False



"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

from collections import deque

class TaskQueue:
    """
    A queue is the correct data structure because tasks must be processed in FIFO order.
    Python’s deque provides O(1) insertion at the back and O(1) removal from the front,
    making it more efficient than a list for queue operations.
    """
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)  # O(1)

    def remove_oldest_task(self):
        if self.queue:
            return self.queue.popleft()  # O(1)
        return None



"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    """
    A set is the best choice because it automatically enforces uniqueness and supports O(1)
    average‑time insertion and membership checks. Each call to add() inserts into the set,
    and get_unique_count() simply returns the size of the set in O(1) time.
    """
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)  # O(1)

    def get_unique_count(self):
        return len(self.values)  # O(1)
