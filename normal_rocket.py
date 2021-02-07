from rocket import Rocket


class NormalRocket(Rocket):
    def get_type(self) -> str:
        return 'Normal rocket'
