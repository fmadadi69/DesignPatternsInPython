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
