# pokemon/pikachu.py
from .base_pokemon import Pokemon
from moves.electric_moves import ThunderShock, ElectroBall
from moves.normal_moves import Tackle
from moves.steel_moves import IronTail
from moves.base_move import Move

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "Electric", 135, 55, 40, 50, 50, 90)
        self.moves = [
            ThunderShock(), 
            ElectroBall(), 
            Tackle(), 
            IronTail()
        ]
