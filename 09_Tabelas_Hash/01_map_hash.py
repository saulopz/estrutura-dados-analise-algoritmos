def map_hash_numerico(key, size):
    return key % size


def map_hash_caracteres(nome):
    def retorna_indice_no_alfabeto(char):
        return ord(char.lower()) - ord("a")

    id1 = retorna_indice_no_alfabeto(nome[0])
    id2 = retorna_indice_no_alfabeto(nome[1])
    return (id1 * 26) + id2


# Testando as funções de hash
for i in range(20):
    print(f"{i}: {map_hash_numerico(i, 7)}")

# Testando a função de hash para strings (nomes)
nomes = [
    "Ana",
    "Beatriz",
    "Carlos",
    "Daniel",
    "Eduardo",
    "Fabio",
    "Gabriel",
    "Heloisa",
    "Igor",
    "Juliana",
    "Kleber",
]
for nome in nomes:
    print(f"{nome}: {map_hash_caracteres(nome)}")
