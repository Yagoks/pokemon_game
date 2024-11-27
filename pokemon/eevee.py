# pokemon/eevee.py
from .base_pokemon import Pokemon
from moves.fairy_moves import BabyDollEyes
from moves.ground_moves import SandAttack
from moves.ghost_moves import ShadowBall
from moves.normal_moves import Tackle

class Eevee(Pokemon):
    def __init__(self):
        super().__init__("Eevee", "Normal", 155, 55, 50, 45, 65, 55)
        self.moves = [
            BabyDollEyes(),
            SandAttack(),
            ShadowBall(),
            Tackle()
        ]
