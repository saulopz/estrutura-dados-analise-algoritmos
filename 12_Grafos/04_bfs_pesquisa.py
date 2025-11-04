from collections import deque


def busca_em_largura(grafo, v, u):
    visitado = set()
    fila = deque([v])

    while fila:
        atual = fila.popleft()
        print("Visitando:", atual)

        if atual == u:
            print(">> Encontrado:", u)
            return True

        visitado.add(atual)

        for vizinho in grafo[atual]:
            if vizinho not in visitado and vizinho not in fila:
                fila.append(vizinho)

    print(">>", u, "não encontrado.")
    return False


# Exemplo de Grafo
#
#      A
#     / \
#    B   C
#   / \   \
#  D   E   F
#   \  |  /
#    \ | /
#      G

grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "G"],
    "E": ["B", "G"],
    "F": ["C", "G"],
    "G": ["D", "E", "F"],
}

print("BFS: Procurando E a partir de A")
busca_em_largura(grafo, "A", "E")
