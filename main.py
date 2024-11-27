import pygame
import sys
import os
import random
from pokemon.pikachu import Pikachu
from pokemon.bulbasaur import Bulbasaur
from pokemon.squirtle import Squirtle
from pokemon.charmander import Charmander
from pokemon.eevee import Eevee

# Inicializar Pygame
pygame.init()

# Configurar tela
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pokemon Battle Game")

# Caminho base para o diretório atual
base_dir = os.path.dirname(__file__)

# Caminhos absolutos para os assets
background_path = os.path.join(base_dir, "assets", "images", "background", "battle_bg.png")
pikachu_sprite_path = os.path.join(base_dir, "assets", "images", "pikachu.png")
bulbasaur_sprite_path = os.path.join(base_dir, "assets", "images", "bulbasaur.png")
squirtle_sprite_path = os.path.join(base_dir, "assets", "images", "squirtle.png")
charmander_sprite_path = os.path.join(base_dir, "assets", "images", "charmander.png")
eevee_sprite_path = os.path.join(base_dir, "assets", "images", "eevee.png")

attack_sound_path = os.path.join(base_dir, "assets", "sounds", "attack_sound.wav")
select_sound_path = os.path.join(base_dir, "assets", "sounds", "select_sound.wav")
battle_music_path = os.path.join(base_dir, "assets", "sounds", "battle_music.mp3")

# Verificar se os arquivos existem antes de carregar
def verificar_arquivo(caminho):
    if not os.path.exists(caminho):
        print(f"Erro: Arquivo não encontrado em {caminho}")
        sys.exit()

verificar_arquivo(background_path)
verificar_arquivo(pikachu_sprite_path)
verificar_arquivo(bulbasaur_sprite_path)
verificar_arquivo(squirtle_sprite_path)
verificar_arquivo(charmander_sprite_path)
verificar_arquivo(eevee_sprite_path)
verificar_arquivo(attack_sound_path)
verificar_arquivo(select_sound_path)
verificar_arquivo(battle_music_path)

# Carregar assets
background = pygame.image.load(background_path)
pikachu_sprite = pygame.image.load(pikachu_sprite_path)
bulbasaur_sprite = pygame.image.load(bulbasaur_sprite_path)
squirtle_sprite = pygame.image.load(squirtle_sprite_path)
charmander_sprite = pygame.image.load(charmander_sprite_path)
eevee_sprite = pygame.image.load(eevee_sprite_path)

# Escalar as imagens para caber na tela
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Sons
attack_sound = pygame.mixer.Sound(attack_sound_path)
select_sound = pygame.mixer.Sound(select_sound_path)
pygame.mixer.music.load(battle_music_path)

# Tocar música de fundo
pygame.mixer.music.play(-1)  # Repetir indefinidamente

# Funções auxiliares
def draw_pokemon(screen, pokemon_sprite, x, y):
    """Desenha o sprite do Pokémon na tela."""
    screen.blit(pokemon_sprite, (x, y))

def draw_background(screen, bg):
    """Desenha o fundo da batalha."""
    screen.blit(bg, (0, 0))

def play_attack_sound():
    """Toca o som de ataque."""
    attack_sound.play()

def animate_attack(screen, attacker_sprite, x_start, x_end, y):
    """Anima o movimento de ataque."""
    for x in range(x_start, x_end, 5):
        screen.fill((0, 0, 0))  # Limpar tela
        draw_background(screen, background)
        draw_pokemon(screen, attacker_sprite, x, y)
        pygame.display.flip()
        pygame.time.delay(50)

def escolher_pokemon():
    print("Escolha seu Pokémon:")
    pokemons = [Pikachu(), Bulbasaur(), Squirtle(), Charmander(), Eevee()]
    sprites = [pikachu_sprite, bulbasaur_sprite, squirtle_sprite, charmander_sprite, eevee_sprite]

    for i, p in enumerate(pokemons):
        print(f"{i + 1}. {p.nome} (HP: {p.hp}, Tipo: {p.tipo})")
    
    escolha = int(input("Digite o número do Pokémon que você quer escolher: ")) - 1
    return pokemons[escolha], sprites[escolha]

def batalha(pokemon1, pokemon2, sprite1, sprite2):
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Desenhar o fundo
        draw_background(screen, background)

        # Desenhar Pokémon
        draw_pokemon(screen, sprite1, 100, 300)  # Pokémon do jogador
        draw_pokemon(screen, sprite2, 600, 300)  # Pokémon do oponente

        # Simular turno
        if pokemon1.spd >= pokemon2.spd:
            play_attack_sound()
            animate_attack(screen, sprite1, 100, 300, 300)
            pokemon1.atacar(pokemon2)
            if pokemon2.esta_vivo():
                play_attack_sound()
                animate_attack(screen, sprite2, 600, 300, 300)
                pokemon2.atacar(pokemon1)
        else:
            play_attack_sound()
            animate_attack(screen, sprite2, 600, 300, 300)
            pokemon2.atacar(pokemon1)
            if pokemon1.esta_vivo():
                play_attack_sound()
                animate_attack(screen, sprite1, 100, 300, 300)
                pokemon1.atacar(pokemon2)

        # Atualizar a tela
        pygame.display.flip()
        clock.tick(30)

        # Exibir status
        print(f"{pokemon1.nome} HP: {pokemon1.hp}")
        print(f"{pokemon2.nome} HP: {pokemon2.hp}")

        # Fim de jogo
        if not pokemon1.esta_vivo() or not pokemon2.esta_vivo():
            vencedor = pokemon1 if pokemon1.esta_vivo() else pokemon2
            print(f"{vencedor.nome} venceu!")
            running = False

# Início do jogo
print("Bem-vindo ao jogo de batalha Pokémon!")
treinador_nome = input("Digite o nome do seu treinador Pokémon: ")
print(f"Olá, {treinador_nome}! Vamos começar!")

jogador_pokemon, jogador_sprite = escolher_pokemon()
print(f"Você escolheu {jogador_pokemon.nome}!")

# Escolha aleatória do oponente
oponente = random.choice([Pikachu(), Bulbasaur(), Squirtle(), Charmander(), Eevee()])
oponente_sprite = {
    "Pikachu": pikachu_sprite,
    "Bulbasaur": bulbasaur_sprite,
    "Squirtle": squirtle_sprite,
    "Charmander": charmander_sprite,
    "Eevee": eevee_sprite,
}[oponente.nome]
print(f"Seu oponente escolheu {oponente.nome}!")

# Iniciar batalha
batalha(jogador_pokemon, oponente, jogador_sprite, oponente_sprite)
