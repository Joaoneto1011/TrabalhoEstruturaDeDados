# Função para verificar se o vetor está ordenado de forma não decrescente
def esta_ordenado(vetor):
    for i in range(1, len(vetor)):
        if vetor[i] < vetor[i - 1]:
            return False
    return True

# Entrada do tamanho do vetor
N = int(input("Digite o tamanho do vetor: "))

# Verificação de tamanho válido
if N <= 0:
    print("Tamanho inválido.")
else:
    # Entrada dos elementos do vetor
    vetor = []
    print("Digite os elementos do vetor:")
    for i in range(N):
        elemento = int(input())
        vetor.append(elemento)

    # Verificação se está ordenado
    if esta_ordenado(vetor):
        print("SIM")
    else:
        print("NAO")
