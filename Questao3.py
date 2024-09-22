# Função para exibir o tabuleiro
def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print("|".join(linha))
        print("-" * 5)

# Inicializa o tabuleiro vazio
tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]

# Função para verificar se a posição é válida
def posicao_valida(linha, coluna):
    return 1 <= linha <= 3 and 1 <= coluna <= 3 and tabuleiro[linha - 1][coluna - 1] == ' '

# Função principal para o jogo
def jogar():
    jogadas = 0
    jogador_atual = 'X'

    while jogadas < 9:  # Máximo de 9 jogadas (3x3)
        exibir_tabuleiro(tabuleiro)

        print(f"Jogador {jogador_atual}, sua vez.")
        linha = int(input("Digite o número da linha (1-3): "))
        coluna = int(input("Digite o número da coluna (1-3): "))

        if posicao_valida(linha, coluna):
            tabuleiro[linha - 1][coluna - 1] = jogador_atual
            jogadas += 1

            # Alterna entre os jogadores
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'
        else:
            print("Posição inválida! Tente novamente.")

    print("Fim de jogo!")
    exibir_tabuleiro(tabuleiro)

# Iniciar o jogo
jogar()
