# Algoritmo Deep First Search (DFS)
def navegacao_em_profundidade(grafo, v, visitado=None):
    if visitado is None:
        visitado = set()

    print(v, end=" ")
    visitado.add(v)

    for vizinho in grafo[v]:
        if vizinho not in visitado:
            navegacao_em_profundidade(grafo, vizinho, visitado)


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
navegacao_em_profundidade(grafo, "A")
print()
