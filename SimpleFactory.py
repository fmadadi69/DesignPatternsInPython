class Door:
    def get_width(self):
        pass

    def get_height(self):
        pass


class WoodenDoor(Door):

    # width = None
    # height = None

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_height(self):
        print(f"height of the wooden door is {self.height}")

    def get_width(self):
        print(f"width of the wooden door is {self.width}")


class DoorFactory:

    @staticmethod
    def makeWoodenDoor(width, height):
        return WoodenDoor(width, height)


woodenD = DoorFactory.makeWoodenDoor(21,30)
woodenD.get_width()
woodenD.get_height()






