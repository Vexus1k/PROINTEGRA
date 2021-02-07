from operator import attrgetter
from random import randint
from normal_rocket import NormalRocket
from turbo_rocket import TurboRocket
from rocket import Rocket


class RocketBoard:
    NORMAL_TYPE = 'Normal'
    TURBO_TYPE = 'Turbo'

    def __init__(self, amount_of_rockets: int = 0):
        self.rockets = [NormalRocket() for _ in range(amount_of_rockets)]

    def add_rocket(self, type: str, speed: int = 1, altitude: float = 0) -> None:
        if (type == self.NORMAL_TYPE):
            self.rockets.append(NormalRocket(speed, altitude))
        elif (type == self.TURBO_TYPE):
            self.rockets.append(TurboRocket(speed, altitude))
        else:
            raise Exception(f'Unknown rocket type: {type}')

    def add_many_rockets(self, amount_of_rockets: int) -> None:
        for _ in range(amount_of_rockets):
            self.rockets.append(NormalRocket())

    def start_race(self, rounds: int = 10) -> None:
        if not self.rockets:
            raise Exception("Rockets don't exist on this space")

        for _ in range(rounds):
            random_rocket_index = randint(0, len(self.rockets) - 1)
            rocket: Rocket = self.rockets[random_rocket_index]
            crashed: bool = rocket.moveUp()
            if (crashed):
                self.rockets.remove(rocket)
                print(f'{rocket.color.capitalize()} rocket has crashed')

    def print_rockets_status(self) -> None:
        for rocket in self.rockets:
            print(rocket)

    def print_best_rockets(self) -> None:
        highest_altitude: int = max(
            self.rockets, key=attrgetter('altitude')).altitude
        print('Rockets with the highest altitude:')
        for rocket in self.rockets:
            if (rocket.altitude == highest_altitude):
                print(rocket)
