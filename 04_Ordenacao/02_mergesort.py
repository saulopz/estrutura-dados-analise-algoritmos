def mergesort(lista):
    # Lista com 0 ou 1 elemento já está ordenada
    if len(lista) <= 1:
        return

    meio = len(lista) // 2  # Encontra o ponto médio da lista
    esquerda = lista[:meio]  # Sublista esquerda
    direita = lista[meio:]  # Sublista direita

    mergesort(esquerda)
    mergesort(direita)

    i = 0  # Índice para a sublista esquerda
    j = 0  # Índice para a sublista direita
    k = 0  # Índice para a lista original

    # Mescla as sublistas de volta na lista original
    while i < len(esquerda) and j < len(direita):
        # Compara os elementos das sublistas e
        # coloca o menor na lista original
        if esquerda[i] < direita[j]:
            lista[k] = esquerda[i]
            i += 1
        else:
            lista[k] = direita[j]
            j += 1
        k += 1  # incrementa o índice da lista original

    # Caso haja elementos restantes em uma das sublistas
    # Adiciona os elementos restantes, se houver
    while i < len(esquerda):
        lista[k] = esquerda[i]
        i += 1
        k += 1
    # Adiciona os elementos restantes da sublista direita
    while j < len(direita):
        lista[k] = direita[j]
        j += 1
        k += 1


minha_lista = [64, 34, 25, 12, 22, 11, 90]
mergesort(minha_lista)
print("Lista ordenada:", minha_lista)
