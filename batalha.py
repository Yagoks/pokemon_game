import time

def batalha(pokemon1, pokemon2):
    """Executa a batalha entre dois Pokémon, mostrando as ações e resultados no terminal."""
    running = True

    while running:
        # Mostrar status dos Pokémons
        print(f"\n{pokemon1.nome} (HP: {pokemon1.hp}) VS {pokemon2.nome} (HP: {pokemon2.hp})")

        # Simular turno
        if pokemon1.spd >= pokemon2.spd:
            print(f"\n{pokemon1.nome} ataca primeiro!")
            time.sleep(1)
            pokemon1.atacar(pokemon2)
            if pokemon2.esta_vivo():
                print(f"\n{pokemon2.nome} contra-ataca!")
                time.sleep(1)
                pokemon2.atacar(pokemon1)
        else:
            print(f"\n{pokemon2.nome} ataca primeiro!")
            time.sleep(1)
            pokemon2.atacar(pokemon1)
            if pokemon1.esta_vivo():
                print(f"\n{pokemon1.nome} contra-ataca!")
                time.sleep(1)
                pokemon1.atacar(pokemon2)

        # Exibir status
        print(f"\nStatus atualizado:")
        print(f"{pokemon1.nome} HP: {pokemon1.hp}")
        print(f"{pokemon2.nome} HP: {pokemon2.hp}")

        # Fim de jogo
        if not pokemon1.esta_vivo() or not pokemon2.esta_vivo():
            vencedor = pokemon1 if pokemon1.esta_vivo() else pokemon2
            print(f"\n{vencedor.nome} venceu a batalha!")
            running = False

        time.sleep(2)
