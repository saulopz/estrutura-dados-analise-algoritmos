import random


def gerar_lista_aleatoria(tamanho):
    lista = []  # passo 1: cria lista vazia
    for i in range(tamanho):  # passo 2: repete até atingir o tamanho
        numero = random.randint(0, 10000)  # passo 2a: gera número aleatório
        lista.append(numero)  # passo 2b: insere no final da lista
    return lista  # passo 3: retorna a lista


# Exemplo de uso
tamanho = 5
lista = gerar_lista_aleatoria(tamanho)
print(lista)
