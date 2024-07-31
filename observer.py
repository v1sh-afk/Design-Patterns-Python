from abc import ABC, abstractmethod

class Observable(ABC):
    @abstractmethod
    def notify(self):
        ...
    def remove(self):
        ...
    
class Observer(ABC):
    @abstractmethod
    def update(self):
        ...
    
class InterestedPeople(Observer):
    def __init__(self,name):
        self.name=name
    def update(self,home):
        print(f'Hi {self.name} you can buy our homes {home} now')

class Home(Observable):
    def __init__(self,society):
        self.society=society
        self.Intersterpeople=[]
        self.home=[]

    def addhome(self,home):
        self.home.append(home)
        self.notify(home)
    def addpeople(self,people):
        self.Intersterpeople.append(people)
    def notify(self,home):
        for Interested in self.Intersterpeople:
            Interested.update(home)
    def __str__(self):
        return self.Intersterpeople,self.home

Society=Home('Society Straight Edge')

Interested1 = InterestedPeople('Vishal')
Interested2 = InterestedPeople('Viccky')

Society.addpeople(Interested1)
Society.addpeople(Interested2)

Society.addhome('APC')

