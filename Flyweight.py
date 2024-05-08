import json
from typing import Dict, List


class Flyweight:
    def __init__(self, shared_state: Dict) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: Dict) -> None:
        shared = json.dumps(self._shared_state)
        unique = json.dumps(unique_state)
        print(f"Flyweight: Displaying shared ({shared}) and unique ({unique}) status")


class FlyweightFactory:
    _flyweights: List = []

    def __init__(self, initial_flyweights: List) -> None:
        for item in initial_flyweights:
            self._flyweights.append(item)

    def get_flyweight(self, shared_state: Dict) -> Flyweight:
        if shared_state not in self._flyweights:
            print("Flyweight Factory: create new flyweight")
            self._flyweights.append(shared_state)
        else:
            print("Flyweight Factory: Reusing existing flyweight")
        return Flyweight(shared_state)

    def list_flyweights(self) -> None:
        for item in self._flyweights:
            print(item)


def add_car_to_police_database(factory: FlyweightFactory, plates: str, owner: str, brand: str, model: str,
                               color: str) -> None:
    print("Client: Adding a car to database:")
    flyweight = factory.get_flyweight({'brand':brand, 'model':model, 'color':color})
    flyweight.operation({'plates':plates, 'owner':owner})


if __name__ == "__main__":
    factory = FlyweightFactory([
        {"brand": "Chevrolet", "model": "Camaro2018", "color": "pink"},
        {"brand": "Mercedes Benz", "model": "C300", "color": "black"},
        # ... other car data ...
    ])
    factory.list_flyweights()  # List existing flyweights
    add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "M5", "red")
    add_car_to_police_database(factory, "CL23aaa", "Faezeh", "BMW", "M5", "red")
    factory.list_flyweights()  # List updated flyweights



