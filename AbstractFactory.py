from abc import ABC, abstractmethod


class Door:
    def getDescription(self):
        pass


class WoodenDoor(Door):
    def getDescription(self):
        print("This is a wooden Door")


class IronDoor(Door):
    def getDescription(self):
        print("This is Iron Door")


class DoorFittingExpert:
    def getDescription(self):
        pass


class Welder(DoorFittingExpert):
    def getDescription(self):
        print("I am Welder and fit Iron Door")


class Carpenter(DoorFittingExpert):
    def getDescription(self):
        print("I am Carpenter and fit Wooden Door")


class DoorFactory:
    def makeDoor(self):
        pass
    def makeFittingExpert(self):
        pass


class WoodenDoorFactory(DoorFactory):
    def makeDoor(self):
        return WoodenDoor()

    def makeFittingExpert(self):
        return Carpenter()


class IronDoorFactory(DoorFactory):
    def makeDoor(self):
        return IronDoor()

    def makeFittingExpert(self):
        return Welder()


woodenDoor = WoodenDoorFactory()
door = woodenDoor.makeDoor()
door.getDescription()

expert = woodenDoor.makeFittingExpert()
expert.getDescription()


# ################ THEMES ################## #
class Button(ABC):
    @abstractmethod
    def draw(self):
        pass


class CheckBox(ABC):
    @abstractmethod
    def draw(self):
        pass


class LightButton(Button):
    def draw(self):
        print("Drawing light button")


class DarkButton(Button):
    def draw(self):
        print("Drawing Dark Button")


class LightCheckBox(CheckBox):
    def draw(self):
        print("Drawing light Checkbox")


class DarkCheckbox(CheckBox):
    def draw(self):
        print("Drawing dark Checkbox")


class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class LightTheme(GUIFactory):
    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightCheckBox()


class DarkTheme(GUIFactory):
    def create_button(self):
        return DarkButton()

    def create_checkbox(self):
        return DarkCheckbox()


class Application:
    def __init__(self, factory:GUIFactory):
        self.factory = factory

    def create_gui(self):
        self.factory.create_button()
        self.factory.create_checkbox()


