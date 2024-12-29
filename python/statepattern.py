# State base class (Interface)
from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle_request(self):
        pass

    @abstractmethod
    def next_state(self, context):
        pass


# Concrete State classes
class RedLight(State):
    def handle_request(self):
        print("The light is RED. Stop!")

    def next_state(self, context):
        context.set_state(GreenLight())


class GreenLight(State):
    def handle_request(self):
        print("The light is GREEN. Go!")

    def next_state(self, context):
        context.set_state(YellowLight())


class YellowLight(State):
    def handle_request(self):
        print("The light is YELLOW. Slow down!")

    def next_state(self, context):
        context.set_state(RedLight())


# Context class that holds the current state
class TrafficLight:
    def __init__(self):
        self._current_state = RedLight()  # Initial state

    def set_state(self, state):
        self._current_state = state

    def handle_request(self):
        self._current_state.handle_request()

    def next_state(self):
        self._current_state.next_state(self)


# Example usage
if __name__ == "__main__":
    traffic_light = TrafficLight()

    import pdb; pdb.set_trace()

    # Cycle through the states
    traffic_light.handle_request()  # Output: The light is RED. Stop!
    traffic_light.next_state()

    traffic_light.handle_request()  # Output: The light is GREEN. Go!
    traffic_light.next_state()

    traffic_light.handle_request()  # Output: The light is YELLOW. Slow down!
    traffic_light.next_state()

    traffic_light.handle_request()  # Output: The light is RED. Stop!