def selecionar_nome_treinador():
    """Permite ao jogador inserir o nome do treinador Pokémon via terminal."""
    while True:
        nome = input("Digite o nome do seu treinador Pokémon: ").strip()
        if nome:
            return nome
        else:
            print("O nome do treinador não pode estar vazio. Por favor, insira um nome válido.")
