def processar(lista1, lista2):
    for x in lista1:  # O(n)
        print(x)
    for y in lista2:  # O(m)
        print(y)


l1 = [0, 1, 2, 3]
l2 = [4, 5, 6, 7, 8]
processar(l1, l2)
