def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        auxiliar = lista[min_idx]
        lista[min_idx] = lista[i]
        lista[i] = auxiliar
    return lista


minha_lista = [64, 34, 25, 12, 22, 11, 90]
selection_sort(minha_lista)
print("Lista ordenada:", minha_lista)
