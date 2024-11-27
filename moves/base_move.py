# moves/base_move.py
import random

class Move:
    def __init__(self, nome, tipo, poder, precisao, categoria):
        self.nome = nome
        self.tipo = tipo
        self.poder = poder
        self.precisao = precisao
        self.categoria = categoria

    def executar(self, usuario, alvo):
        if random.randint(1, 100) <= self.precisao:
            dano = self.calcular_dano(usuario, alvo)
            alvo.hp -= dano
            print(f"{usuario.nome} usou {self.nome} e causou {dano} de dano a {alvo.nome}!")
        else:
            print(f"{usuario.nome} usou {self.nome}, mas errou!")

    def calcular_dano(self, usuario, alvo):
        if self.categoria == "Physical":
            dano_base = usuario.atk + self.poder - alvo.defense
        elif self.categoria == "Special":
            dano_base = usuario.sp_atk + self.poder - alvo.sp_def
        else:
            return 0
        return max(0, dano_base)
