class ReverseIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = len(self.data) - 1   # start from last index
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration     # signals end of iteration
        
        value = self.data[self.index]
        self.index -= 1
        return value
nums = ReverseIterable([10, 20, 30, 40])

for n in nums:
    print(n)
