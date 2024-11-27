# moves/electric_moves.py
from .base_move import Move
import random

class ThunderShock(Move):
    def __init__(self):
        super().__init__("Thunder Shock", "Electric", 40, 100, "Special")

    def executar(self, usuario, alvo):
        super().executar(usuario, alvo)
        if random.random() < 0.5:
            print(f"{alvo.nome} está paralisado!")
            alvo.status_effects.append("Paralyze")


class ElectroBall(Move):
    def __init__(self):
        super().__init__("Electro Ball", "Electric", 100, 75, "Special")

    def calcular_dano(self, usuario, alvo):
        bonus_velocidade = max(0, usuario.spd - 90)
        return super().calcular_dano(usuario, alvo) + bonus_velocidade
