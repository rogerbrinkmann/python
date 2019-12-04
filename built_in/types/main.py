mytype = type("CustomType", (object,), {'attr1':1, 'attr2':'some value'})

print(type(mytype))
# <class 'type'>

print(vars(mytype))
# {'attr1': 1, 'attr2': 'some value', '__module__': '__main__', '__dict__': <attribute '__dict__' of 'CustomType' objects>, '__weakref__': <attribute '__weakref__' of 'CustomType' objects>, '__doc__': None}

print(dir(mytype))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attr1', 'attr2']

print(mytype.attr1)
print(mytype.attr2)
