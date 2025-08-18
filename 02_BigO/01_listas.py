lista = [1, 2, 3, 4, 5]
print(lista[0])        # acesso direto (O(1))
lista.append(6)        # inserção no fim (O(1) amortizado)
lista.insert(2, 99)    # inserção no meio (O(n))
lista.pop()            # remoção no fim (O(1))
lista.remove(2)        # remoção por valor (O(n))
