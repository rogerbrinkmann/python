"""
Example of an iteratior class
"""


class MyRange:
    """
    custom range
    """

    def __init__(self, start, end, step=1):
        self.value = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += self.step
        return current

    def __repr__(self):
        return "MyRange"


nums = MyRange(1, 10, 2)

print(next(nums))
print(next(nums))
print()
for num in nums:
    print(num)

