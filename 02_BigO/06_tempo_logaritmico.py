# Tempo Logarítmico O(log n)
import random
import time


def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1


tamanhos = [1000, 10000, 100000]

for tamanho in tamanhos:
    lista = list(range(tamanho))
    random.shuffle(lista)
    alvo = lista[-1]  # pior caso
    inicio = time.time()
    busca_binaria(lista, alvo)
    fim = time.time()
    print(f"Tamanho {tamanho}: {fim - inicio:.6f} segundos")
