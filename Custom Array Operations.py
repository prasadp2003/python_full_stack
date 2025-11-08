class IntList:
    def __init__(self):
        self.data = []

    def append(self, value):
        """Add an integer to the list"""
        if isinstance(value, int):
            self.data.append(value)
        else:
            raise TypeError("Only integers are allowed")

    def remove(self, value):
        """Remove first occurrence of an integer"""
        if value in self.data:
            self.data.remove(value)
        else:
            raise ValueError(f"{value} not found in list")

    def pop(self, index=-1):
        """Remove and return element at given index (default last)"""
        if len(self.data) == 0:
            raise IndexError("pop from empty list")
        return self.data.pop(index)

    def slice(self, start=None, end=None):
        """Return a new IntList containing a slice"""
        sliced = self.data[start:end]
        new_list = IntList()
        new_list.data_

# Example usage:
nums = IntList()
nums.append(10)
nums.append(20)
nums.append(30)
print(nums)          # IntList([10, 20, 30])

nums.remove(20)
print(nums)          # IntList([10, 30])

popped = nums.pop()
print(popped)        # 30
print(nums)          # IntList([10])

nums.append(40)
nums.append(50)
print(nums.slice(0, 2))  # IntList([10, 40])












