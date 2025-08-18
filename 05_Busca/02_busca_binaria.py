def busca_binaria(lista, alvo):   # Busca binária
    esq = 0                       # Índice inicial (esquerda)
    dir = len(lista) - 1          # Índice final (direita)
    while esq <= dir:             # Enquanto o início não ultrapassar o fim
        meio = (esq + dir) // 2   # Ponto médio da lista
        if lista[meio] == alvo:   # Se o elemento do meio for o alvo
            return meio           # Retorna o índice do elemento encontrado
        elif lista[meio] < alvo:  # Se o elemento do meio for menor que o alvo
            esq = meio + 1        # Move o início para a direita
        else:                     # Se o elemento do meio for maior que o alvo
            dir = meio - 1        # Move o fim para a esquerda
    return -1                     # Se elemento não for encontrado, retorna -1


minha_lista = [10, 20, 30, 40, 50]
alvo = 30
resultado = busca_binaria(minha_lista, alvo)
print(f"Elemento encontrado no índice {resultado}")
