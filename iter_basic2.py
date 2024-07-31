my_list = [4, 7, 0, 3]

my_iter = iter(my_list)

while True:
    try:
        element = next(my_iter)
        print(element)
        
    except StopIteration:
        break


