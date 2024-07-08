from abc import ABC, abstractmethod


class Transportation(ABC):
    @abstractmethod
    def get_eta(self):
        pass

    @abstractmethod
    def get_direction(self):
        pass


class Driving(Transportation):
    def get_eta(self):
        print("Calculating ETA (Driving)")
        return 1

    def get_direction(self):
        print("Calculating direction (Driving)")
        return 1


class Bicycling(Transportation):
    def get_eta(self):
        print("Calculating ETA (Bicycling)")
        return 2

    def get_direction(self):
        print("Calculating direction (Bicycling)")
        return 2


class Transit(Transportation):
    def get_eta(self):
        print("Calculating ETA (Transit)")
        return 3

    def get_direction(self):
        print("Calculating direction (Transit)")
        return 3


class Walking(Transportation):
    def get_eta(self):
        print("Calculating ETA (Walking)")
        return 4

    def get_direction(self):
        print("Calculating direction (Walking)")
        return 4


class DirectionService:
    def __init__(self, transportation: Transportation):
        self._transportation = transportation

    def get_eta(self):
        self._transportation.get_eta()

    def get_direction(self):
        self._transportation.get_direction()


direction_service = DirectionService(Walking())
direction_service.get_eta()
direction_service.get_direction()




