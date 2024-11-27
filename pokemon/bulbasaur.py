# pokemon/bulbasaur.py
from .base_pokemon import Pokemon
from moves.grass_moves import RazorLeaf, EnergyBall
from moves.poison_moves import PoisonPowder
from moves.psychic_moves import Rest

class Bulbasaur(Pokemon):
    def __init__(self):
        super().__init__("Bulbasaur", "Grass/Poison", 145, 49, 49, 65, 65, 45)
        self.moves = [
            RazorLeaf(),
            PoisonPowder(),
            EnergyBall(),
            Rest()
        ]
