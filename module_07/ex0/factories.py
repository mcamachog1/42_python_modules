# factories.py

from .factory import CreatureFactory
from .creature import Creature
from .creatures import Flameling, Pyrodon, Aquabub, Torragon


class FlameFactory(CreatureFactory):
    BASE_NAME = "Flameling" 
    EVOLVED_NAME = "Pyrodon"
    name = "Flame"

    def create_base(self) -> Creature:
        return Flameling(self.BASE_NAME)

    def create_evolved(self) -> Creature:
        return Pyrodon(self.EVOLVED_NAME)


class AquaFactory(CreatureFactory):
    BASE_NAME = "Aquabub"
    EVOLVED_NAME = "Torragon"
    name = "Aqua"

    def create_base(self) -> Creature:
        return Aquabub(self.BASE_NAME)

    def create_evolved(self) -> Creature:
        return Torragon(self.EVOLVED_NAME)
