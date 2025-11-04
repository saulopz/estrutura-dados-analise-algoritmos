from collections import deque


# Algoritmo Best First Searc (BFS)
def navegacao_em_largura(grafo, inicio):
    visitado = set()
    fila = deque([inicio])

    while fila:
        v = fila.popleft()
        if v not in visitado:
            print(v, end=" ")
            visitado.add(v)
            for vizinho in grafo[v]:
                if vizinho not in visitado:
                    fila.append(vizinho)


# Exemplo de Grafo
#
#      A
#     / \
#    B   C
#   / \ / \
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

print("Deep First Search:")
navegacao_em_largura(grafo, "A")
print()
