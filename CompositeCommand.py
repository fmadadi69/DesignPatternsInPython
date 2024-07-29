from abc import ABC, abstractmethod
from typing import List


class SmartHomeAutomation:
    def __init__(self):
        self._lights = False
        self._door_lock = False
        self._temperature = 0

    def turn_on_lights(self):
        self._lights = True
        print(f'Lights turned {"ON" if self._lights == True else "OFF"}')

    def turn_off_lights(self):
        self._lights = False
        print(f'Lights turned {"ON" if self._lights == True else "OFF"}')

    def lock_the_door(self):
        self._door_lock = True
        print(f'Door is {"LOCKED" if self._door_lock == True else "UNLOCKED"}')

    def unlock_the_door(self):
        self._door_lock = False
        print(f'Door is {"LOCKED" if self._door_lock == True else "UNLOCKED"}')

    def set_thermostate(self, temp):
        self._temperature = temp
        print(f'Thermostate set to {self._temperature}')


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class TurnOnLightsCommand(Command):
    def __init__(self, smart_home: SmartHomeAutomation):
        self._smart_home = smart_home

    def execute(self):
        return self._smart_home.turn_on_lights()


class TurnOffLightsCommand(Command):
    def __init__(self, smart_home: SmartHomeAutomation):
        self._smart_home = smart_home

    def execute(self):
        return self._smart_home.turn_off_lights()


class LockTheDoorCommand(Command):
    def __init__(self, smart_home: SmartHomeAutomation):
        self._smart_home = smart_home

    def execute(self):
        return self._smart_home.lock_the_door()


class UnLockTheDoorCommand(Command):
    def __init__(self, smart_home: SmartHomeAutomation):
        self._smart_home = smart_home

    def execute(self):
        return self._smart_home.unlock_the_door()


class SetThermostateCommand(Command):
    def __init__(self, smart_home: SmartHomeAutomation, temperature):
        self._smart_home = smart_home
        self._temp = temperature

    def execute(self):
        return self._smart_home.set_thermostate(self._temp)


class GoodMorningCommand(Command):
    def __init__(self):
        self._commands: List[Command] = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute(self):
        self.add_command(TurnOnLightsCommand(SmartHomeAutomation()))
        self.add_command(UnLockTheDoorCommand(SmartHomeAutomation()))
        self.add_command(SetThermostateCommand(SmartHomeAutomation(), 22))
        for item in self._commands:
            item.execute()


class GoodNightCommand(Command):
    def __init__(self):
        self._commands: List[Command] = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def execute(self):
        self.add_command(TurnOffLightsCommand(SmartHomeAutomation()))
        self.add_command(LockTheDoorCommand(SmartHomeAutomation()))
        self.add_command(SetThermostateCommand(SmartHomeAutomation(), 18))
        for item in self._commands:
            item.execute()


class Button:
    def __init__(self, command: Command):
        self._command = command

    def click(self):
        return self._command.execute()


button = Button(GoodMorningCommand())
button.click()

button2 = Button(GoodNightCommand())
button2.click()
