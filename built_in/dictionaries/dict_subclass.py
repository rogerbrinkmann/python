import re

class MyDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value)

    def __getitem__(self, key):
        return super().__getitem__(key)

    def keys(self):
        return super().keys()

    def values(self):
        return super().values()

    def items(self):
        return super().items()

    def __len__(self):
        return len(self.items())

    def filtered(self, pattern):
        if not isinstance(pattern, str):
            raise IndexError()
        return {k:v for k, v in self.items() if k == pattern}

    def fullmatch(self, pattern):
        if not isinstance(pattern, str):
            raise IndexError()

        comp = re.compile(pattern)
        return {k:v for k, v in self.items() if comp.fullmatch(k)}

result = re.fullmatch(".*Motor_Control", "PDU_Motor_Control")

if result:
    print(result.string)

if __name__ == "__main__":
    d = MyDict()

    d["Toast"]=1
    d["Taste"]=2
    d["Stress"]=3

    print(d.fullmatch(".*st.*"))
