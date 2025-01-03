# Command Interface
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


# Receiver Classes
class Light:
    def turn_on(self):
        print("The light is ON.")

    def turn_off(self):
        print("The light is OFF.")


class Fan:
    def start(self):
        print("The fan is RUNNING.")

    def stop(self):
        print("The fan is STOPPED.")


# Concrete Command Classes
class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_on()

    def undo(self):
        self.light.turn_off()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.turn_off()

    def undo(self):
        self.light.turn_on()


class FanOnCommand(Command):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.start()

    def undo(self):
        self.fan.stop()


class FanOffCommand(Command):
    def __init__(self, fan: Fan):
        self.fan = fan

    def execute(self):
        self.fan.stop()

    def undo(self):
        self.fan.start()


# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()

    def press_undo(self):
        if self.command:
            self.command.undo()


# Client Code
if __name__ == "__main__":
    # Receivers
    light = Light()
    fan = Fan()

    # Concrete Commands
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    fan_on = FanOnCommand(fan)
    fan_off = FanOffCommand(fan)

    # Invoker
    remote = RemoteControl()

    # Light ON
    remote.set_command(light_on)
    remote.press_button()  # Output: The light is ON.
    remote.press_undo()    # Output: The light is OFF.

    print(f"{'-'*30}")

    # Fan ON
    remote.set_command(fan_on)
    remote.press_button()  # Output: The fan is RUNNING.
    remote.press_undo()    # Output: The fan is STOPPED.

    print(f"{'-'*30}")

    # Light OFF
    remote.set_command(light_off)
    remote.press_button()  # Output: The light is OFF.
    remote.press_undo()    # Output: The light is ON.
