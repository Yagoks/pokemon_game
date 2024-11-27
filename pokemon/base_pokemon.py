# pokemon/base_pokemon.py
class Pokemon:
    def __init__(self, nome, tipo, hp, atk, defense, sp_atk, sp_def, spd):
        self.nome = nome
        self.tipo = tipo
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.spd = spd
        self.status_effects = []
        self.moves = []

    def escolher_movimento(self):
        print(f"\nEscolha um movimento para {self.nome}:")
        for i, move in enumerate(self.moves):
            print(f"{i + 1}. {move.nome} ({move.tipo})")
        escolha = int(input("Escolha o número do movimento: ")) - 1
        return self.moves[escolha]

    def atacar(self, alvo):
        movimento = self.escolher_movimento()
        movimento.executar(self, alvo)
    
    def esta_vivo(self):
        return self.hp > 0
