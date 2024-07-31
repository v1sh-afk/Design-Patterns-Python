from abc import ABC,abstractmethod

class Component(ABC):

    @abstractmethod
    def size(self):
        ...

class File(Component):

    def __init__(self,fname,fsize):
        self.fname=fname
        self.fsize=fsize
    
    def size(self):
        return self.fsize
    
class Folder(Component):

    def __init__(self,name,components):
        self.name=name
        self.components=components
    
    def size(self):
        total=0
        for component in self.components:
            total=total+component.size()
        return total

    def add(self,component):
        self.components.append(component)

file1=File('file1',100)
file2=File('file2',200)
Folder1=Folder('Folder1',[file1,file2])
print(file1.size())
print(Folder1.size())