#List comprehension and dictionary comprehension are concise ways to create new lists and dictionaries, respectively. 
# They are a more efficient and simpler way of performing the same tasks as a for loop.

#Here is an example of list comprehension:


numbers = [1, 2, 3, 4]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)  # Output: [2, 4, 6, 8]
#This is equivalent to the following for loop:


numbers = [1, 2, 3, 4]
doubled_numbers = []
for num in numbers:
  doubled_numbers.append(num * 2)
print(doubled_numbers)  # Output: [2, 4, 6, 8]
#Here is an example of dictionary comprehension:


numbers = [1, 2, 3, 4]
squared_numbers = {num: num ** 2 for num in numbers}
print(squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16}
#This is equivalent to the following for loop:


numbers = [1, 2, 3, 4]
squared_numbers = {}
for num in numbers:
  squared_numbers[num] = num ** 2
print(squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16}
#List and dictionary comprehensions can also include conditional statements to create more complex lists and dictionaries. For example:

#Copy code
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {num: num ** 2 for num in numbers if num % 2 == 0}
print(even_squares)  # Output: {2: 4, 4: 16, 6: 36}
#This is equivalent to the following for loop:

#Copy code
numbers = [1, 2, 3, 4, 5, 6]
even_squares = {}
for num in numbers:
  if num % 2 == 0:
    even_squares[num] = num ** 2
print(even_squares)  # Output: {2: 4, 4: 16, 6: 36}