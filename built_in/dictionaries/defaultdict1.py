"""
Sample usage of defaultdict
"""
from collections import defaultdict


def makedict():
    """
    recursively provide levels of nested dictionary as needed 
    """
    return lambda: defaultdict(makedict())


d1 = defaultdict(makedict())

d1["a"]["b"]["c"] = 123
d1["c"]["d"] = 23

print(d1["a"]["b"]["c"])
print(d1["c"]["d"])

d2 = defaultdict(list)

d2["a"].extend([1, 2])
d2["a"].extend([3, 4])
print(d2["a"])

d3 = defaultdict(int)

d3["a"] = 1
print(d3["a"])
