# moves/water_moves.py
from .base_move import Move

class WaterGun(Move):
    def __init__(self):
        super().__init__("Water Gun", "Water", 40, 90, "Special")

    def executar(self, usuario, alvo):
        super().executar(usuario, alvo)
        print(f"{alvo.nome} teve sua Speed reduzida em 10 pontos!")
        alvo.spd = max(0, alvo.spd - 10)

class RainDance(Move):
    def __init__(self):
        super().__init__("Rain Dance", "Water", 0, 100, "Buff")

    def executar(self, usuario, alvo):
        print(f"{usuario.nome} iniciou a chuva! Ataques de água são fortalecidos!")
        usuario.status_effects.append("Rain")
