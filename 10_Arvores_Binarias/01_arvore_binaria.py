class ArvoreBinariaEstatica:
    def __init__(self, capacidade):
        self.capacidade = capacidade  # Capacidade máxima da árvore
        self.arvore = [None] * capacidade  # Lista para armazenar os elementos da árvore
        self.tamanho = 0  # Número atual de elementos na árvore

    # Insere um valor na árvore
    def inserir(self, valor):
        if self.tamanho >= self.capacidade:
            raise Exception("A árvore está cheia")
        # Insere o valor na próxima posição disponível
        self.arvore[self.tamanho] = valor
        self.tamanho += 1  # Incrementa o tamanho da árvore

    # Retorna o valor da raiz da árvore
    def obter_raiz(self):
        if self.tamanho == 0:  # Se a árvore estiver vazia,
            return None  # retorna None
        return self.arvore[0]  # A raiz está sempre na posição 0

    # Retorna o valor do filho esquerdo de um nó dado seu índice
    def obter_filho_esquerdo(self, indice):
        filho_esquerdo = 2 * indice + 1  # Cálculo do índice do filho esquerdo
        # Verifica se o índice está dentro do tamanho atual da árvore
        if filho_esquerdo < self.tamanho:
            return self.arvore[filho_esquerdo]
        return None

    # Retorna o valor do filho direito de um nó dado seu índice
    def obter_filho_direito(self, indice):
        filho_direito = 2 * indice + 2  # Cálculo do índice do filho direito
        # Verifica se o índice está dentro do tamanho atual da árvore
        if filho_direito < self.tamanho:
            return self.arvore[filho_direito]
        return None

    # Retorna o valor do pai de um nó dado seu índice
    def obter_pai(self, indice):
        if indice == 0:  # A raiz não tem pai
            return None
        pai = (indice - 1) // 2  # Cálculo do índice do pai
        return self.arvore[pai]

    # Verifica se a árvore está vazia
    def esta_vazia(self):
        return self.tamanho == 0

    # Retorna o tamanho atual da árvore
    def obter_tamanho(self):
        return self.tamanho

    def __str__(self):
        return str(self.arvore[: self.tamanho])


def reordenar_para_balanceamento(vetor_ordenado):
    resultado = []
    def construir_ordem(start, end):
        if start > end:
            return
        mid = (start + end) // 2
        resultado.append(vetor_ordenado[mid])
        construir_ordem(start, mid - 1)
        construir_ordem(mid + 1, end)
    construir_ordem(0, len(vetor_ordenado) - 1)
    return resultado


# Exemplo de uso
if __name__ == "__main__":

    lista = [12, 25, 37, 50, 62, 75, 87, 100, 112, 125]
    lista = reordenar_para_balanceamento(sorted(lista))
    print("Ordem para inserção balanceada:", lista)

    arvore = ArvoreBinariaEstatica(len(lista))
    for numero in lista:
        arvore.inserir(numero)

    print("Árvore:", arvore)
    print("Raiz:", arvore.obter_raiz())
    print("Filho esquerdo da raiz:", arvore.obter_filho_esquerdo(0))
    print("Filho direito da raiz:", arvore.obter_filho_direito(0))
    print("Pai do nó no índice 2:", arvore.obter_pai(2))
    print("Tamanho da árvore:", arvore.obter_tamanho())
    print("A árvore está vazia?", arvore.esta_vazia())
