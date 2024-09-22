# Inicializa a matriz 10x10
matriz = []

# Entrada dos elementos da matriz
print("Digite os elementos da matriz 10x10:")
for i in range(10):
    linha = []
    for j in range(10):
        elemento = int(input(f"Elemento [{i+1}][{j+1}]: "))
        linha.append(elemento)
    matriz.append(linha)

# Inicializa as variáveis para armazenar o maior valor e sua posição
maior_valor = matriz[0][0]
linha_maior = 0
coluna_maior = 0

# Percorre a matriz para encontrar o maior valor
for i in range(10):
    for j in range(10):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha_maior = i
            coluna_maior = j

# Exibe o maior valor e sua localização
print(f"O maior valor é {maior_valor} e está na linha {linha_maior + 1}, coluna {coluna_maior + 1}.")
