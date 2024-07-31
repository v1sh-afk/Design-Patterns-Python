import unittest

class MyClass:
    def __init__(self, value):
        self.value = value

class MyClassTests(unittest.TestCase):
    def test_my_class(self):
        my_obj = MyClass(5)
        self.assertIsInstance(my_obj, MyClass)

if __name__ == '__main__':
    unittest.main()

