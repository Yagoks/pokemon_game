# moves/fairy_moves.py
from .base_move import Move

class BabyDollEyes(Move):
    def __init__(self):
        super().__init__("Baby-Doll Eyes", "Fairy", 0, 100, "Debuff")

    def executar(self, usuario, alvo):
        print(f"{alvo.nome} teve seu Ataque reduzido em 20 pontos!")
        alvo.atk = max(0, alvo.atk - 20)
