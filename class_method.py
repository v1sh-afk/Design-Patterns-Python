class Subject():

    sub_name = 'PDP' # class attribute

    def __init__(self):
        self.code = 12345  # instance attribute

    @classmethod
    def display(cls):
        print('Subject Name is:',cls.sub_name)


sub=Subject()
sub.display()
print(sub.code)

