from abc import ABC,abstractmethod

class Elevator:
    def __init__(self,state):
        self.setstate(state)
    def setstate(self,state):
        self.state=state
        self.state.elevator=self
    def goup(self):
        self.state.goup()
    def godown(self):
        self.state.godown()
    def curstate(self):
        print(type(self.state).__name__)
class FirstFloor:
    def goup(self):
        print('Going to second floor')
        print(self.elevator)
        self.elevator.setstate(SecondFloor())
    
    def godown(self):
        print('Cannot go')

class SecondFloor:
    def goup(self):
        print('Cannot go')
    
    def godown(self):
        self.elevator.setstate(FirstFloor())
E=Elevator(FirstFloor())
E.godown()
E.goup()
E.curstate()

import unittest

class Testing(unittest.TestCase):
    def Testcheck(self,E):
        self.assertIsNone(E)

if __name__=='__main__':
    unittest.main()