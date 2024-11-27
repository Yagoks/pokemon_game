# moves/ground_moves.py
from .base_move import Move

class SandAttack(Move):
    def __init__(self):
        super().__init__("Sand Attack", "Ground", 0, 100, "Debuff")

    def executar(self, usuario, alvo):
        print(f"{alvo.nome} teve sua precisão reduzida em 20%.")
        if "AccuracyDown" not in alvo.status_effects:
            alvo.status_effects.append("AccuracyDown")
