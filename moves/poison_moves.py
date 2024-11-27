# moves/poison_moves.py
from .base_move import Move
import random

class PoisonPowder(Move):
    def __init__(self):
        super().__init__("Poison Powder", "Poison", 0, 75, "Debuff")

    def executar(self, usuario, alvo):
        super().executar(usuario, alvo)
        print(f"{alvo.nome} foi envenenado!")
        if "Poison" not in alvo.status_effects:
            alvo.status_effects.append("Poison")
