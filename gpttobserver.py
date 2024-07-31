import abc
import datetime

class Observer(abc.ABC):
    """The Observer interface"""
    @abc.abstractmethod
    def update(self, medicine: "Medicine"):
        pass

class Medicine:
    def __init__(self, name: str, stock: int, expiry_date: datetime.datetime):
        self.name = name
        self.stock = stock
        self.expiry_date = expiry_date
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def update_stock(self, new_stock: int):
        self.stock = new_stock
        self.notify()


class ExpiryAlert(Observer):
    def update(self, medicine: Medicine):
        if medicine.expiry_date <= datetime.datetime.now():
            print(f"Medicine {medicine.name} is expired")


class StockAlert(Observer):
    def update(self, medicine: Medicine):
        if medicine.stock <= 10:
            print(f"Medicine {medicine.name} is running low in stock")

# Usage
medicine = Medicine("Paracetamol", 15, datetime.datetime(2022, 12, 31))

expiry_alert = ExpiryAlert()
medicine.attach(expiry_alert)

stock_alert = StockAlert()
medicine.attach(stock_alert)

medicine.update_stock(5)
