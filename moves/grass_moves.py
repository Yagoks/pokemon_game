# moves/grass_moves.py
from .base_move import Move

class RazorLeaf(Move):
    def __init__(self):
        super().__init__("Razor Leaf", "Grass", 65, 95, "Physical")

class EnergyBall(Move):
    def __init__(self):
        super().__init__("Energy Ball", "Grass", 90, 100, "Special")
