# Inicializando o vetor
vetor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Invertendo o vetor
i = 0
while i < 10:
    temp = vetor[i]
    vetor[i] = vetor[9 - i]
    vetor[9 - i] = temp
    i += 1

# Exibindo o vetor invertido
print(vetor)
