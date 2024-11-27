# moves/dark_moves.py
from .base_move import Move
import random

class Bite(Move):
    def __init__(self):
        super().__init__("Bite", "Dark", 60, 100, "Physical")

    def executar(self, usuario, alvo):
        super().executar(usuario, alvo)
        if random.random() < 0.1:
            print(f"{alvo.nome} ficou assustado e perdeu o turno!")
            alvo.status_effects.append("Flinch")
