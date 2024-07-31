from abc import ABC, abstractmethod 

class Baking_Cake(ABC):
    @abstractmethod
    def get_ingredients(self):
        pass

    @abstractmethod
    def mix_all(self):
        pass

    @abstractmethod
    def baking(self):
        pass

    def process_cake_making(self):
        print("Preparing a Cake")
        self.get_ingredients()
        self.mix_all()
        self.baking()
        print("Serve the Cake")


class FruitCake(Baking_Cake):

    def get_ingredients(self):
        print("Collect nuts, dry fruits, egg, refined flour, butter, sugar")

    def mix_all(self):
        print("Add one item at a time. Egg should be added in the last")

    def baking(self):
        print("Bake at 325 F")


class Eggless_BlackForest(Baking_Cake):

    def get_ingredients(self):
        print("Collect cocoa powder, baking soda, milk, refined flour, butter, sugar")

    def mix_all(self):
        print("Add all items at the same time")

    def baking(self):
        print("Bake at 475 F")

choice = input("What type of cake you want? ")

if choice == 'fruit':
    cake=FruitCake()
    cake.process_cake_making()
elif choice == 'eggless':
    cake=Eggless_BlackForest()
    cake.process_cake_making()
else:
    print("No cake")
    
'''
GPT
The template design pattern is a behavioral design pattern that defines the skeleton of an algorithm in a method, 
deferring some steps to subclasses. 
It allows subclasses to redefine certain steps of an algorithm without changing the algorithm's structure.

Here is an example of the template design pattern in Python:
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def primitive_operation_1(self):
        pass

    @abstractmethod
    def primitive_operation_2(self):
        pass

    def template_method(self):
        print("Defining the algorithm. Operation 1 follows operation 2.")
        self.primitive_operation_1()
        self.primitive_operation_2()

class ConcreteClass(AbstractClass):
    def primitive_operation_1(self):
        print("Operation 1 called on ConcreteClass")

    def primitive_operation_2(self):
        print("Operation 2 called on ConcreteClass")

c = ConcreteClass()
c.template_method()
In this example, the AbstractClass defines the template method that contains the algorithm, 
as well as two abstract methods, primitive_operation_1 and primitive_operation_2, 
that are left to be implemented by concrete subclasses. 
The ConcreteClass is a subclass of AbstractClass and provides concrete implementations for the two abstract methods.
 When the template method is called on an instance of ConcreteClass, 
 it executes the algorithm defined in the template method, using the concrete implementations of the abstract methods provided by the subclass.'''