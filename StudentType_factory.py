from abc import ABC, abstractstaticmethod

class Student(ABC):

    @abstractstaticmethod
    def id():
        ...

class Student_firstyear(Student):
    def __init__(self):
        self.name = "First year"
        #pass
    
    def admission(self):
        pass
    
    def id(self):
        print("I study in first year")

class Student_secondyear(Student):
    def __init__(self):
        self.name = "Second year"

    def internships(self):
        pass
    
    def id(self):
        print("I study in second year")

class Student_thirdyear(Student):
    def __init__(self):
        self.name = "Third year"

    def placements(self):
        pass
    
    def id(self):
        print("I study in third year")


class StudentFactory:

    @staticmethod
    def build_student(type):
        if type=="first year":
            return Student_firstyear()
        if type=="second year":
            return Student_secondyear()
        if type== "third year":
            return Student_thirdyear()
        else:
            raise Invalidexception()


s1=Student_firstyear()
s1.id()
s1.admission()
s2=Student_secondyear()
s2.id()
s2.internships()
s3=Student_thirdyear()
s3.id()
s3.placements()


choice = input("Type of the student\n")
student_details=StudentFactory.build_student(choice)
student_details.id()
