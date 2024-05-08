class Washing:
    def wash(self):
        print("Washing...")


class Rinsing:
    def rinse(self):
        print("Rinsing...")


class Spinning:
    def spin(self):
        print("Spinning...")


class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def turn_on(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()


washing_machine = WashingMachine()
washing_machine.turn_on()
