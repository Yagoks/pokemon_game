# moves/fire_moves.py
from .base_move import Move

class Inferno(Move):
    def __init__(self):
        super().__init__("Inferno", "Fire", 100, 50, "Special")

    def executar(self, usuario, alvo):
        super().executar(usuario, alvo)
        print(f"{usuario.nome} sofreu efeito de Burn! Causa dano contínuo por 3 turnos.")
        alvo.status_effects.append("Burn")
