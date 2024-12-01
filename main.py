import sys
import os
import random

# Importar Pokemons
from pokemon.pikachu import Pikachu
from pokemon.bulbasaur import Bulbasaur
from pokemon.squirtle import Squirtle
from pokemon.charmander import Charmander
from pokemon.eevee import Eevee

# Escolher Pokemon e nome do treinador
from trainer_selection import selecionar_nome_treinador
from pokemon_selection import escolher_pokemon, escolher_oponente

# Função de batalha
from batalha import batalha

# Inicio
print("Bem-vindo ao jogo de batalha Pokémon!")
treinador_nome = selecionar_nome_treinador()
print(f"Olá, {treinador_nome}! Vamos começar!")

# Selecionar Pokemon
jogador_pokemon = escolher_pokemon()
print(f"Você escolheu {jogador_pokemon.nome}!")

# Oponente Escolhe aleatorio
oponente = escolher_oponente()
print(f"Seu oponente escolheu {oponente.nome}!")

# Iniciar batalha
batalha(jogador_pokemon, oponente)
