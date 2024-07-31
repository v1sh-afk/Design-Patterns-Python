from abc import ABC, abstractstaticmethod

class Student(ABC):

    @abstractstaticmethod
    def id():
        ...

class FirstYear(Student):
    def __init__(self):
        self.name="first year"
    def id(self):
        print('I study in first year')

class SecondYear(Student):
    def __init__(self):
        self.name='second year'

    def id(self):
        print('I study in second year')
    
class StudentFactory:

    @staticmethod
    def id(choice):
        if choice=='first year':
            return FirstYear()
        else:
            return SecondYear()
class Teacher(ABC):

    @abstractstaticmethod
    def id():
        ...

class FirstYearTeacher(Teacher):
    def __init__(self):
        self.name="First year"
    def id(self):
        print('I teach for first year')

class SecondYearTeacher(Teacher):
    def __init__(self):
        self.name='Second year'
    def id(self):
        print('I teach for the second year')
    
class TeacherFactory:
    @staticmethod
    def id(choice):
        if choice=='first year':
            return FirstYearTeacher()
        else:
            return SecondYear()

class Academics(ABC):
    def id():
        ...

class AcademicFactory(Academics):
    @staticmethod
    def id(choice):
        if choice in ['first year student']:
            return StudentFactory.id('first year')
        elif choice in ['second year student']:
            return StudentFactory.id('second year')
        elif choice in ['first year teacher']:
            return TeacherFactory.id('first year')
        else:
            return TeacherFactory.id('second year')

choice=input('enter choice')
object1=AcademicFactory.id(choice)
print(f'{object1.__class__}')
object1.id()

'''
class AbstractFactory:
    def create_product_a(self):
        pass
    def create_product_b(self):
        pass
    
class ConcreteFactoryA(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()
    def create_product_b(self):
        return ConcreteProductB1()

class ConcreteFactoryB(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()
    def create_product_b(self):
        return ConcreteProductB2()

class AbstractProductA:
    def operation(self):
        pass

class AbstractProductB:
    def operation(self):
        pass

class ConcreteProductA1(AbstractProductA):
    def operation(self):
        return "ConcreteProductA1"

class ConcreteProductA2(AbstractProductA):
    def operation(self):
        return "ConcreteProductA2"

class ConcreteProductB1(AbstractProductB):
    def operation(self):
        return "ConcreteProductB1"

class ConcreteProductB2(AbstractProductB):
    def operation(self):
        return "ConcreteProductB2"
'''