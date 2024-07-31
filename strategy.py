'''The strategy pattern is a design pattern that allows for the encapsulation of different algorithms or behaviors in separate classes, and allows for the selection of the appropriate algorithm or behavior at runtime.

Here is an example scenario where the strategy pattern can be used:

Let's say you are building a game that has different difficulty levels, and each difficulty level uses a different AI for the game's enemies. The AI for the easy difficulty level should be simple and not very aggressive, while the AI for the hard difficulty level should be more complex and aggressive.

Here's an example code that illustrates how the strategy pattern can be used to implement this scenario:

'''
class Enemy:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def move(self):
        self.strategy.move()

class EasyAI:
    def move(self):
        print("Easy AI: Moving slowly")

class HardAI:
    def move(self):
        print("Hard AI: Moving quickly and aggressively")

# creating objects
easy_ai = EasyAI()
hard_ai = HardAI()

# creating enemy
enemy = Enemy(easy_ai)

# enemy using easy AI
enemy.move()
# Output: Easy AI: Moving slowly

# changing the strategy
enemy.set_strategy(hard_ai)

# enemy using hard AI
enemy.move()
# Output: Hard AI: Moving quickly and aggressively
''' 
In this example, the Enemy class has a strategy attribute that can be set to different instances of the EasyAI and HardAI classes. The move method of the Enemy class simply calls the move method of the current strategy. This allows the behavior of the Enemy class to change depending on the strategy that is currently set. This way we can change the behavior of the Enemy class without changing the code of the class.
'''


