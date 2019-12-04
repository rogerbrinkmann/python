from collections import defaultdict

def nesteddict():
    return defaultdict(nesteddict)

nd = nesteddict()


nd["a"]["b"]["c"] = 10

print(nd["a"]["b"]["c"])

