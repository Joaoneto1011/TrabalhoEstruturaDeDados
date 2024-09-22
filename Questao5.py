# Definição da estrutura da banda utilizando dicionários
class Banda:
    def __init__(self, nome, tipo_musica, num_integrantes, ranking):
        self.nome = nome
        self.tipo_musica = tipo_musica
        self.num_integrantes = num_integrantes
        self.ranking = ranking

# Preenchendo as bandas com valores
bandas_favoritas = []

bandas_favoritas.append(Banda("Banda 1", "Rock", 5, 1))
bandas_favoritas.append(Banda("Banda 2", "Pop", 4, 2))
bandas_favoritas.append(Banda("Banda 3", "Jazz", 6, 3))
bandas_favoritas.append(Banda("Banda 4", "Metal", 4, 4))
bandas_favoritas.append(Banda("Banda 5", "Blues", 3, 5))

# Acessando os valores das bandas
for banda in bandas_favoritas:
    print(f"Nome: {banda.nome}")
    print(f"Tipo de Música: {banda.tipo_musica}")
    print(f"Número de Integrantes: {banda.num_integrantes}")
    print(f"Ranking: {banda.ranking}")
    print("---------------")
