class StackQueueList:
    def __init__(self):
        # The single underlying list to store elements
        self._data = []

    # --- Stack Operations (LIFO - Last-In, First-Out) ---

    def push(self, item):
        """Adds an item to the top of the stack (right end of the list). O(1)"""
        self._data.append(item)
        print(f"Stack Push: Added {item}")

    def pop(self):
        """Removes and returns the item from the top of the stack (right end). O(1)"""
        if not self._data:
            raise IndexError("pop from empty stack")
        item = self._data.pop()
        print(f"Stack Pop: Removed {item}")
        return item

    # --- Queue Operations (FIFO - First-In, First-Out) ---

    def enqueue(self, item):
        """Adds an item to the back of the queue (right end of the list). O(1)"""
        # We reuse the list's append for efficiency
        self._data.append(item)
        print(f"Queue Enqueue: Added {item}")

    def dequeue(self):
        """Removes and returns the item from the front of the queue (left end). O(n)"""
        if not self._data:
            raise IndexError("dequeue from empty queue")
        # Removing from the start (index 0) is O(n) for Python lists
        item = self._data.pop(0)
        print(f"Queue Dequeue: Removed {item}")
        return item

    # --- Common Operation ---

    def peek(self):
        """Returns the next item to be popped (top of stack) or dequeued (front of queue)."""
        if not self._data:
            return None
        
        # We can define 'peek' to look at either the stack top or queue front.
        # It's conventional to show the element *about to be removed* by either operation.
        
        # If the user is operating as a Stack, they expect the rightmost element.
        # If the user is operating as a Queue, they expect the leftmost element.
        
        # For simplicity, we can default to showing the element that would be removed by a 'dequeue' (the queue front).
        # You could also offer a choice (peek_stack, peek_queue).
        
        return self._data[0] # Returns the queue front (element at index 0)
    
    # --- Utility ---
    
    def is_empty(self):
        """Checks if the structure is empty."""
        return len(self._data) == 0

    def __len__(self):
        """Returns the number of elements."""
        return len(self._data)