import random
from pokemon.pikachu import Pikachu
from pokemon.bulbasaur import Bulbasaur
from pokemon.squirtle import Squirtle
from pokemon.charmander import Charmander
from pokemon.eevee import Eevee

def escolher_pokemon():
    """Permite ao jogador escolher um Pokémon via terminal."""
    print("Escolha seu Pokémon:")
    pokemons = [Pikachu(), Bulbasaur(), Squirtle(), Charmander(), Eevee()]

    for i, p in enumerate(pokemons):
        print(f"{i + 1}. {p.nome} (HP: {p.hp}, Tipo: {p.tipo})")
    
    while True:
        try:
            escolha = int(input("Digite o número do Pokémon que você quer escolher: ")) - 1
            if escolha in range(len(pokemons)):
                return pokemons[escolha]
            else:
                print("Escolha inválida. Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def escolher_oponente():
    """Escolhe um Pokémon adversário."""
    print("Escolha seu Pokémon:")
    pokemons = [Pikachu(), Bulbasaur(), Squirtle(), Charmander(), Eevee()]

    for i, p in enumerate(pokemons):
        print(f"{i + 1}. {p.nome} (HP: {p.hp}, Tipo: {p.tipo})")
    
    while True:
        try:
            escolha = int(input("Digite o número do Pokémon que você quer escolher: ")) - 1
            if escolha in range(len(pokemons)):
                return pokemons[escolha]
            else:
                print("Escolha inválida. Por favor, digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")