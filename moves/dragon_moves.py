# moves/dragon_moves.py
from .base_move import Move
import random

class DragonBreath(Move):
    def __init__(self):
        super().__init__("Dragon Breath", "Dragon", 60, 100, "Special")

    def executar(self, usuario, alvo):
        super().executar(usuario, alvo)
        if random.random() < 0.2:
            print(f"{alvo.nome} está paralisado e pode perder turnos!")
            alvo.status_effects.append("Paralyze")
