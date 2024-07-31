
class CapitalIterable(str):
    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)


class CapitalIterator(str):
    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __iter__(self):
        return self
        
    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index =self.index+1
        print(self.index)
        return word
        

iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
iterator = iter(iterable)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

#print("Done")

for i in iter(iterator):
    print(i)


