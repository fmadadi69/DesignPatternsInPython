class Burger:
    __size = None
    __cheese = False
    __pepperoni = False
    __lettuce = False
    __tomato = False

    def __init__(self, builder):
        self.__size = builder.size
        self.__cheese = builder.cheese
        self.__pepperoni = builder.pepperoni
        self.__lettuce = builder.lettuce
        self.__tomato = builder.tomato

    def order(self):
        return f"Burger with size {self.__size} is ordered"


class BurgerBuilder:
    size = 0
    cheese = False
    pepperoni = False
    lettuce = False
    tomato = False

    def __init__(self, size):
        self.size = size

    def with_cheese(self):
        self.cheese = True
        return self

    def with_pepperoni(self):
        self.pepperoni = True
        return self

    def with_lettuce(self):
        self.lettuce = True
        return self

    def with_tomato(self):
        self.tomato = True
        return self

    def build(self):
        return Burger(self)


burger = BurgerBuilder(10).with_cheese().with_pepperoni().with_lettuce().with_tomato().build()

print(vars(burger))
print(burger.order())


