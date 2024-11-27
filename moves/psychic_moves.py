# moves/psychic_moves.py
from .base_move import Move

class Rest(Move):
    def __init__(self):
        super().__init__("Rest", "Psychic", 0, 100, "Buff")

    def executar(self, usuario, alvo):
        # Restaura 30% do HP máximo do Pokémon, mas perde o próximo turno
        cura = int(usuario.hp * 0.3)
        usuario.hp += cura
        print(f"{usuario.nome} usou Rest e recuperou {cura} pontos de HP!")
        print(f"{usuario.nome} perderá o próximo turno.")
        usuario.status_effects.append("Resting")
