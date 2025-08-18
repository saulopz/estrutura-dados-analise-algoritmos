# Tempo cúbico O(n^3)


def trios(lista):
    for i in lista:
        for j in lista:
            for k in lista:
                print(i, j, k)
