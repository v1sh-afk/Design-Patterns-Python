from typing import Iterable,Iterator

class Subject:

    def __init__(self,sub_name,sub_code,sub_credit):
        self.sub_name=sub_name
        self.sub_code=sub_code
        self.sub_credit=sub_credit
    
    def __str__(self):
        return f'{self.sub_name}' + " " + f'{self.sub_code}' + " " + f'{self.sub_credit}'
        
   
class Subjectiterable(Iterable[str]):

    def __init__(self,*args):
        self.subjects=[*args]
    
    def __iter__(self):
        return Subjectiterator(self.subjects)

class Subjectiterator(Iterator[str]):

    def __init__(self,subjectiterable):
        self.subjectiterator=[sub for sub in subjectiterable if sub.sub_credit=='3']
        self.index=0
    
    def __next__(self):

        if self.index<len(self.subjectiterator):
            
            sub = self.subjectiterator[self.index]
            self.index=self.index+1
            return sub
        else:
            raise StopIteration

s1=Subject('PDP','10','3')
s2=Subject('DS1','11','2')
s3=Subject('DS2','12','3')


subjectiterable1=Subjectiterable(s1,s2,s3)


for i in subjectiterable1:
    print(i)
    
