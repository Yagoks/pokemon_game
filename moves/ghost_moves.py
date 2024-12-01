# moves/ghost_moves.py
from .base_move import Move

class ShadowBall(Move):
    def __init__(self):
        super().__init__("Shadow Ball", "Ghost", 80, 90, "Special")

    def executar(self, usuario, alvo):
        super().executar(usuario, alvo)
        print(f"{usuario.nome} lançou uma bola de sombra contra {alvo.nome}!")
