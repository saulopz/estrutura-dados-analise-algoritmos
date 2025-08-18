# Tempo Linear O(n)


def soma(lista):
    total = 0  # O(1) ← inicialização simples
    for item in lista:  # O(n) ← percorre todos os elementos
        total += item  # O(1) ← operação constante em cada passo
    return total  # O(1) ← retorno direto
