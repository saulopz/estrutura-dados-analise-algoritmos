import random
import time


def busca_linear(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


tamanhos = [1000, 10000, 100000]

for tamanho in tamanhos:
    lista = list(range(tamanho))
    random.shuffle(lista)
    alvo = lista[-1]  # pior caso
    inicio = time.time()
    busca_linear(lista, alvo)
    fim = time.time()
    print(f"Tamanho {tamanho}: {fim - inicio:.6f} segundos")
