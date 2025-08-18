def quicksort(lista):
    if len(lista) <= 1:  # Lista com 0 ou 1 elemento já está ordenada
        return lista

    pivot = lista[len(lista) - 1]  # Escolhe o pivô como último elemento

    menores = []  # Lista para armazenar os elementos menores ou iguais ao pivô
    maiores = []  # Lista para armazenar os elementos maiores que o pivô

    # Percorre todos os elementos, menos o pivô
    for i in range(0, len(lista) - 1):  # índice inicial até final-1
        if lista[i] <= pivot:
            menores.append(lista[i])  # adiciona na lista de menores
        else:
            maiores.append(lista[i])  # adiciona na lista de maiores

    # Chama recursivamente para cada sublista e concatena o resultado
    return quicksort(menores) + [pivot] + quicksort(maiores)


minha_lista = [64, 34, 25, 12, 22, 11, 90]
minha_lista = quicksort(minha_lista)
print("Lista ordenada:", minha_lista)
