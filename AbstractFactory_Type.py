from abc import ABC, abstractstaticmethod


#Student Factory
class Invalidexception(Exception):
    print('Hi')


class Student(ABC):

    @abstractstaticmethod
    def id():
        ...

class FirstyearStudent(Student):
    def __init__(self):
        self.name = "First year"
        
    def admission(self):
        pass
    
    def id(self):
        print("I study in first year")

class SecondyearStudent(Student):
    def __init__(self):
        self.name = "Second year"

    def internships(self):
        pass
    
    def id(self):
        print("I study in second year")

class ThirdyearStudent(Student):
    def __init__(self):
        self.name = "Third year"

    def placements(self):
        pass
    
    def id(self):
        print("I study in third year")

class StudentFactory:

    @staticmethod
    def id(choice):
        if choice=="first year":
            return FirstyearStudent()
        if choice=="second year":
            return SecondyearStudent()
        if choice== "third year":
            return ThirdyearStudent()
        else:
            raise Invalidexception()

#Teacher Factory
        
class Teacher(ABC):

    @abstractstaticmethod
    def id():
        ...

class FirstyearTeacher(Teacher):
    def __init__(self):
        self.name = "First year"
        #pass
    
    def common_faculty(self):
        pass
    
    def id(self):
        print("I teach for first year")

class SecondyearTeacher(Teacher):
    def __init__(self):
        self.name = "Second year"

    def dept_faculty(self):
        pass
    
    def id(self):
        print("I teach for second year")

class ThirdyearTeacher(Teacher):
    def __init__(self):
        self.name = "Third year"

    def industry_faculty(self):
        pass
    
    def id(self):
        print("I teach for third year")

class TeacherFactory:
    
    @staticmethod
    def id(choice):
        if choice=="first year":
            return FirstyearTeacher()
        if choice=="second year":
            return SecondyearTeacher()
        if choice== "third year":
            return ThirdyearTeacher()
        else:
            raise Invalidexception()

class Academics(ABC):
    def id():
        ...

class AcademicFactory(Academics):
    @staticmethod
    def id(choice):
        if choice in ["first year student"]:
            return StudentFactory.id("first year")
        if choice in ["second year student"]:
            return StudentFactory.id("second year")
        if choice in ["third year student"]:
            return StudentFactory.id("third year")
        if choice in ["first year teacher"]:
            return TeacherFactory.id("first year")
        if choice in ["second year teacher"]:
            return TeacherFactory.id("second year")
        if choice in ["third year teacher"]:
            return TeacherFactory.id("third year")
        else:
            return -1
    
choice=input("ID of\n") 
object1=AcademicFactory.id(choice)
print(f'{object1.__class__}')
object1.id()

'''GPT
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are usually
    able to collaborate among themselves. A family of products may have several
    variants, but the products of one variant are incompatible with products of
    another.
    """

    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract product,
    while inside the method a concrete product is instantiated.
    """

    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(ABC):
    """
    Each distinct product of a product family should have a base interface. All
    variants of the product must implement this interface.
    """

    @abstractmethod
    def useful_function_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    """
    Concrete Products are created by corresponding Concrete Factories.
    """

    def useful_function_a(self):
        return "The result of the product A1."


class ConcreteProductA2(AbstractProductA):
    """
    Each Concrete Product belongs to a single variant of the product.
    """

    def useful_function_a(self):
        return "The result of the product A2."


class AbstractProductB(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between products of
    the same concrete variant.
    """

    @abstractmethod
    def useful_function_b(self):
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractProductA):
        pass


class ConcreteProductB1(AbstractProductB):
    def useful_function_b(self):
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(self, collaborator: AbstractProductA
'''