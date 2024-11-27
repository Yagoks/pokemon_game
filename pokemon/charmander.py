# pokemon/charmander.py
from .base_pokemon import Pokemon
from moves.fire_moves import Inferno
from moves.dragon_moves import DragonBreath
from moves.normal_moves import Smokescreen
from moves.steel_moves import MetalClaw

class Charmander(Pokemon):
    def __init__(self):
        super().__init__("Charmander", "Fire", 139, 52, 43, 60, 50, 65)
        self.moves = [
            DragonBreath(),
            Inferno(),
            Smokescreen(),
            MetalClaw()
        ]
