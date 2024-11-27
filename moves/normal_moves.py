# moves/normal_moves.py
from .base_move import Move

class Smokescreen(Move):
    def __init__(self):
        super().__init__("Smokescreen", "Normal", 0, 100, "Debuff")

    def executar(self, usuario, alvo):
        print(f"{alvo.nome} teve sua precisão reduzida em 10%.")
        if "AccuracyDown" not in alvo.status_effects:
            alvo.status_effects.append("AccuracyDown")

class Tackle(Move):
    def __init__(self):
        super().__init__("Tackle", "Normal", 40, 100, "Physical")

    def executar(self, usuario, alvo):
        super().executar(usuario, alvo)
        print(f"{usuario.nome} usou Tackle contra {alvo.nome}!")