class VendingMachine:
    def __init__(self):
        self.state = IdleState()

    def set_state(self, state):
        self.state = state

    def insert_money(self, money):
        self.state.insert_money(self, money)

    def dispense(self):
        self.state.dispense(self)

class IdleState:
    def insert_money(self, vending_machine, money):
        vending_machine.money += money
        vending_machine.set_state(AcceptingMoneyState())
        print("Money accepted. Current balance: ", vending_machine.money)

    def dispense(self, vending_machine):
        print("No money inserted.")

class AcceptingMoneyState:
    def insert_money(self, vending_machine, money):
        vending_machine.money += money
        print("Money accepted. Current balance: ", vending_machine.money)

    def dispense(self, vending_machine):
        if vending_machine.money >= vending_machine.product_price:
            vending_machine.money -= vending_machine.product_price
            vending_machine.set_state(DispensingState())
            print("Product dispensed. Remaining balance: ", vending_machine.money)
        else:
            print("Insufficient balance.")

class DispensingState:
    def insert_money(self, vending_machine, money):
        print("Cannot accept money. Product is being dispensed.")

    def dispense(self, vending_machine):
        print("Cannot dispense product. Product is being dispensed.")


M=VendingMachine().insert_money(100)