class MyDict(dict):
    def __setitem__(self, key, value):
        print("__setitem__() called")
        super().__setitem__(key, value)

    def __getitem__(self, key):
        print("__getitem__() called")
        return super().__getitem__(key)

    def keys(self):
        print("keys() called")
        return super().keys()

    def values(self):
        print("values() called")
        return super().values()

    def items(self):
        print("items() called")
        return super().items()

    def __len__(self):
        print("len() called")
        return len(self.items())

    def filtered(self, pattern):
        if not isinstance(pattern, str):
            raise IndexError()
        return {k:v for k, v in self.items() if k == pattern}

if __name__ == "__main__":
    adict = dict()
    mydict = MyDict()

    adict["a"] = 1
    adict["b"] = 2
    adict["c"] = 3

    mydict["a"] = 1
    mydict["b"] = 2
    mydict["c"] = 3

    # print(adict.keys())
    # print(mydict.keys())
    
    # print(adict.values())
    # print(mydict.values())
    
    # print(adict.items())
    # print(mydict.items())

    # print(len(adict))
    # print(len(mydict))

    print(mydict.filtered("d"))
