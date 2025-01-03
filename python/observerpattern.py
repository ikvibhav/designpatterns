from abc import ABC, abstractmethod

'''
Example - Weather Station
- Weather Station is the subject
- Phone Display and Window Display are the observers
- Weather Station notifies the observers when the weather data changes
'''


# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure):
        pass


# Subject Class
class WeatherStation:
    def __init__(self):
        self._observers = []  # List of observers
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    # Method to set new weather data and notify observers
    def set_weather_data(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()


# Concrete Observers
class PhoneDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Phone Display - Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")


class WindowDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Window Display - Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")


# Client Code
if __name__ == "__main__":
    # Create the WeatherStation (subject)
    weather_station = WeatherStation()

    # Create observers
    phone_display = PhoneDisplay()
    window_display = WindowDisplay()

    # Register observers with the WeatherStation
    weather_station.add_observer(phone_display)
    weather_station.add_observer(window_display)

    # Update weather data
    weather_station.set_weather_data(25, 65, 1013)  # Notify observers
    print("-" * 50)

    weather_station.set_weather_data(30, 70, 1010)  # Notify observers
    print("-" * 50)

    # Remove one observer
    weather_station.remove_observer(phone_display)

    # Update weather data again
    weather_station.set_weather_data(20, 60, 1015)  # Only notify the remaining observer
