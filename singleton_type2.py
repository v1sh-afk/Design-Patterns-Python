class Singleton2:

  __instance = None 

  def __new__(cls):

    if (cls.__instance is None):

      cls.__instance = super(Singleton2,cls).__new__(cls)
    
    return cls.__instance 

s1 = Singleton2()
print(s1)
s2 = Singleton2()
print(s2)

s1.x = 5
print(s2.x)

'''
import unittest

class MyClass:
    def __init__(self, value):
        self.value = value

class MyClassTests(unittest.TestCase):
    def test_my_class(self):
        my_obj = Singleton2()
        self.assertIsInstance(my_obj, Singleton2())

if __name__ == '__main__':
    unittest.main()
'''