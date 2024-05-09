from abc import ABC, abstractmethod


class Door(ABC):
    @abstractmethod
    def getDescription(self):
        pass


class WoodenDoor(Door):
    def getDescription(self):
        print("This is a wooden Door")


class IronDoor(Door):
    def getDescription(self):
        print("This is Iron Door")


class DoorFittingExpert(ABC):
    @abstractmethod
    def getDescription(self):
        pass


class Welder(DoorFittingExpert):
    def getDescription(self):
        print("I am Welder and fit Iron Door")


class Carpenter(DoorFittingExpert):
    def getDescription(self):
        print("I am Carpenter and fit Wooden Door")


class DoorFactory(ABC):
    @abstractmethod
    def makeDoor(self) -> Door:
        pass
    @abstractmethod
    def makeFittingExpert(self) -> DoorFittingExpert:
        pass


class WoodenDoorFactory(DoorFactory):
    def makeDoor(self) -> Door:
        return WoodenDoor()

    def makeFittingExpert(self) -> DoorFittingExpert:
        return Carpenter()


class IronDoorFactory(DoorFactory):
    def makeDoor(self) -> Door:
        return IronDoor()

    def makeFittingExpert(self) -> DoorFittingExpert:
        return Welder()


class Application:
    def __init__(self, factory: DoorFactory):
        self.factory = factory

    def fit_door(self):
        door = self.factory.makeDoor()
        door_fitting_expert = self.factory.makeFittingExpert()

        door.getDescription()
        door_fitting_expert.getDescription()


woodenDoor = WoodenDoorFactory()
app1 = Application(woodenDoor)
app1.fit_door()

iron_door = IronDoorFactory()
app2 = Application(iron_door)
app2.fit_door()


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
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> CheckBox:
        pass


class LightTheme(GUIFactory):
    def create_button(self) -> Button:
        return LightButton()

    def create_checkbox(self) -> CheckBox:
        return LightCheckBox()


class DarkTheme(GUIFactory):
    def create_button(self) -> Button:
        return DarkButton()

    def create_checkbox(self) -> CheckBox:
        return DarkCheckbox()


class Application:
    def __init__(self, factory:GUIFactory):
        self.factory = factory

    def create_gui(self):
        button = self.factory.create_button()
        checkbox = self.factory.create_checkbox()

        button.draw()
        checkbox.draw()


light_theme = LightTheme()
dark_theme = DarkTheme()

app1 = Application(light_theme)
app1.create_gui()

app2 = Application(dark_theme)
app2.create_gui()



