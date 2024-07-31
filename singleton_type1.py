class Singleton1:

  __instance = None
  

  def __init__(self):
    if Singleton1.__instance != None:
       raise Exception("Singleton object already created!")
    else:
       Singleton1.__instance = self


  @staticmethod 
  def getInstance():
    if Singleton1.__instance == None:
      Singleton1()
    return Singleton1.__instance

  

s1 = Singleton1.getInstance()
print(s1)
s2 = Singleton1.getInstance()
print(s2)

s1.x = 5
print(s1.x)
s2.x = 10
print(s2.x)
print(s1.x)

#s3=Singleton1()

'''GPT
The singleton design pattern is a design pattern that ensures that a class has only one instance, and provides a global point of access to it. 
This is useful when you need to ensure that only one object of a particular class is created, 
because the object represents a resource that is shared by the entire system.

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2) # True
In this example, the Singleton class has a class variable _instance that is set to None. The __new__ method is overridden to check if an instance of the Singleton class has already been created. If not, it creates a new instance and assigns it to the _instance variable. If an instance already exists, it returns the existing instance. This ensures that only one instance of the Singleton class is created.

You can also use the __init__ method to initialize the instance, but it is called only once, when the instance is first created.
 The __new__ method is called every time an instance is created, so it is a better place to implement the singleton pattern.
'''

