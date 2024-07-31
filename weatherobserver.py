import abc

class WeatherData:
    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify_observers()

class Observer(abc.ABC):
    @abc.abstractmethod
    def update(self, temperature, humidity, pressure):
        pass

class DisplayElement(abc.ABC):
    @abc.abstractmethod
    def display(self):
        pass

class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weather_data):
        self.temperature = None
        self.humidity = None
        self.weather_data = weather_data
        weather_data.register_observer(self)

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")

weather_data = WeatherData()
current_display = CurrentConditionsDisplay(weather_data)
weather_data.set_measurements(80, 65, 30.4)
# Current conditions: 80F degrees and 65% humidity
