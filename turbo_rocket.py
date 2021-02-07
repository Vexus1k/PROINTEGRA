from rocket import Rocket


class TurboRocket(Rocket):
    def __init__(self, speed: int = 1, altitude: int = 0):
        super().__init__(speed * 2)

    def get_type(self) -> str:
        return 'Turbo rocket'
