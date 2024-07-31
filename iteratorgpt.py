import unittest

class IntegerIterable:
    def __init__(self,value):
        self.value=value
    def __iter__(self):
        return IntegerIterator(self.value)

class IntegerIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

iterator = IntegerIterable([1, 2, 3, 4, 5])
for number in iterator:
    print(number)  # Output: 1 2 3 4 5

class Test(unittest.TestCase):
    def check(self):
        self.assertTrue(isinstance(iterator,IntegerIterable))


if __name__=='__main__':
    unittest.main()

'''The Iterator design pattern is a behavioral design pattern that allows you to 
traverse a container of objects in a sequential manner without exposing the underlying representation of the container. 
This allows you to access elements in the container one at a time, rather than having to deal with the entire container at once.

In Python, the Iterator pattern is implemented using two methods: __iter__ and __next__.
 The __iter__ method returns an iterator object, and the __next__ method returns the next value in the iteration.'''