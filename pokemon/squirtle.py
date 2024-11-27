# pokemon/squirtle.py
from .base_pokemon import Pokemon
from moves.water_moves import WaterGun, RainDance
from moves.steel_moves import IronDefense
from moves.dark_moves import Bite

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "Water", 144, 48, 65, 50, 64, 43)
        self.moves = [
            WaterGun(),
            IronDefense(),
            RainDance(),
            Bite()
        ]
