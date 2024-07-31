#non-list comprehension

str_list1 = ["2", "4", "6"]
converted_list1=[]
for num in str_list1:
    converted_list1.append(int(num))
print(converted_list1)


#list comprehension

converted_list2=[int(num) for num in str_list1]
print(converted_list2)


#list comprehension with conditions

converted_list2=[int(num) for num in str_list1 if len(num)>0]
print(converted_list2)

#Dictionary comprehensions
'''Like dictionaries, they contain keys that are hashed to a particular value.
But on contrary, it supports both access from key-value and iteration,
the functionality that dictionaries lack'''

from typing import NamedTuple
class Book(NamedTuple):
    author:str
    genre: str

books=[Book("Book1","fantasy"), Book("Book2","fiction")]

authors={b.author for b in books if b.genre=='fiction'}
print(authors)
