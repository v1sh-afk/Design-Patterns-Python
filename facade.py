"""
The Facade pattern is a way to provide a simpler unified interface to
a more complex system. It provides an easier way to access functions
of the underlying system by providing a single entry point.
This pattern can be seen in the Python standard library.



The Facade Design Pattern is a structural pattern that provides a simplified interface to a complex system.
 It hides the underlying complexity of a system and provides a unified and more convenient interface for clients to access the 
 functionality of the system. 
In Python, you can implement the Facade design pattern in the following way:
"""
class CPU:
    def freeze(self):
        print("Freezing processor.")
    def jump(self, position):
        print("Jumping to:", position)
    def execute(self):
        print("Executing.")

class Memory:
    def load(self, position, data):
        print(f"Loading from {position} data: '{data}'.")

class SolidStateDrive:
    def read(self, lba, size):
        return f"Some data from sector {lba} with size {size}"
    
class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()
    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()


computer_facade = ComputerFacade()
computer_facade.start()
