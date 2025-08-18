def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


minha_lista = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(minha_lista)
print("Lista ordenada:", minha_lista)
