def busca_em_profundidade(grafo, v, u, visitado=None):
    if visitado is None:
        visitado = set()

    print("Visitando:", v)
    visitado.add(v)

    # Se achou o alvo, termina
    if v == u:
        print(">> Encontrado:", u)
        return True

    # Continua a busca em profundidade
    for vizinho in grafo[v]:
        if vizinho not in visitado:
            if busca_em_profundidade(grafo, vizinho, u, visitado):
                return True  # Propaga o sucesso para o nível acima

    return False  # Se nenhum vizinho levou ao alvo


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

print("DFS: Procurando E a partir de A")
busca_em_profundidade(grafo, "A", "E")
