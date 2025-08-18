def busca_linear(lista, alvo):
    for i in range(0, len(lista)):
        if lista[i] == alvo:
            return i
    return -1


minha_lista = [10, 20, 30, 40, 50]
alvo = 30
resultado = busca_linear(minha_lista, alvo)
print(f"Elemento encontrado no índice {resultado}")
