#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)  # should print True
print(add.__annotations__)  # should print {'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}

