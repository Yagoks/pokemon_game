# moves/steel_moves.py
from .base_move import Move
import random

class IronDefense(Move):
    def __init__(self):
        super().__init__("Iron Defense", "Steel", 0, 100, "Buff")

    def executar(self, usuario, alvo):
        print(f"{usuario.nome} aumentou sua Defesa em 30 pontos!")
        usuario.defense += 30


class MetalClaw(Move):
    def __init__(self):
        super().__init__("Metal Claw", "Steel", 50, 95, "Physical")

    def executar(self, usuario, alvo):
        super().executar(usuario, alvo)
        if random.random() < 0.5:
            print(f"{usuario.nome} teve seu Ataque aumentado em 10%.")
            usuario.atk += int(usuario.atk * 0.1)

class IronTail(Move):
    def __init__(self):
        super().__init__("Iron Tail", "Steel", 70, 80, "Physical")

    def executar(self, usuario, alvo):
        super().executar(usuario, alvo)
        if random.random() < 0.3:
            print(f"{alvo.nome} teve sua Defesa reduzida em 5 pontos!")
            alvo.defense = max(0, alvo.defense - 5)