from abc import ABC, abstractmethod
from tools import Tools


class Rocket(ABC):
    def __init__(self, speed: int = 1, altitude: int = 0):
        self.altitude = 0
        self.fuel = 3
        self.speed = speed
        self.color = Tools.random_color()

    def moveUp(self) -> bool:
        if (self.fuel < 0):
            return True
        else:
            self.altitude += self.speed
            self.fuel -= self.speed
            return self.fuel < 0

    def __str__(self) -> str:
        return f'{self.color.capitalize()} rocket has {str(self.altitude)} altitude and {str(self.fuel)} points of fuel'

    @abstractmethod
    def get_type(self) -> str:
        pass
