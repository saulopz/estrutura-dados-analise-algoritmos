class No:
    def __init__(self, valor):
        self.dado = valor
        self.prox = None


class ListaSimples:
    # Inicializa a lista vazia
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    # Análise de complexidade: O(1)
    def inserir_no_inicio(self, valor):
        novo = No(valor)
        novo.prox = self.inicio
        self.inicio = novo
        if self.fim is None:
            self.fim = novo
        self.tamanho += 1

    # Análise de complexidade: O(1)
    def inserir_no_fim(self, valor):
        novo = No(valor)
        if self.fim is None:  # A lista está vazia
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.prox = novo
            self.fim = novo
        self.tamanho += 1

    # Análise de complexidade: O(n)
    def inserir_no_meio(self, valor, posicao):
        # Verifica se a posição é válida
        if posicao < 0 or posicao > self.tamanho:
            raise IndexError("Posição inválida")

        # Se a posição for 0, insere no início
        if posicao == 0:
            self.inserir_no_inicio(valor)
            return

        # Se a posição for igual ao tamanho, insere no fim
        if posicao == self.tamanho:
            self.inserir_no_fim(valor)
            return

        # Insere no meio
        novo = No(valor)  # cria um novo nó
        atual = self.inicio  # atual aponta para o início
        # percorre até a posição anterior de onde se quer inserir
        for _ in range(posicao - 1):
            atual = atual.prox
        novo.prox = atual.prox  # novo aponta para o próximo
        atual.prox = novo  # atual aponta para o novo
        self.tamanho += 1  # incrementa o tamanho da lista

    # Análise de complexidade: O(n)
    def existe_valor(self, valor):
        atual = self.inicio
        while atual is not None:
            if atual.dado == valor:
                return True
            atual = atual.prox
        return False
    
    # Retorna o valor na posição especificada
    # Análise de complexidade: O(n)
    def buscar_valor_pela_posicao(self, posicao):
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posição inválida")
        atual = self.inicio
        for _ in range(posicao):
            atual = atual.prox
        return atual.dado

    # Remove o primeiro nó com o valor especificado
    # Análise de complexidade: O(n)
    def removerPeloValor(self, valor):
        atual = self.inicio  # aponta para o início
        anterior = None  # aponta para o nó anterior
        # percorre a lista
        while atual is not None:
            # Se o valor do nó atual for igual ao valor a ser removido
            if atual.dado == valor:
                # Se for o primeiro nó, atualiza o início
                if anterior is None:
                    self.inicio = atual.prox
                # Se não for o primeiro nó, atualiza o próximo do nó anterior
                else:
                    anterior.prox = atual.prox
                self.tamanho -= 1  # decrementa o tamanho da lista
                return True
            anterior = atual  # atualiza o nó anterior
            atual = atual.prox  # atualiza o nó atual
        return False

    # Remove o nó na posição especificada
    # Análise de complexidade: O(n)
    def removerPelaPosicao(self, posicao):
        # Verifica se a posição é válida
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posição inválida")

        atual = self.inicio  # aponta para o início
        anterior = None  # aponta para o nó anterior

        # Se for a primeira posição, atualiza o início
        if posicao == 0:
            self.inicio = atual.prox
            self.tamanho -= 1
            return True

        # Percorre até a posição desejada
        for _ in range(posicao):
            anterior = atual
            atual = atual.prox

        # Atualiza o próximo do nó anterior
        anterior.prox = atual.prox
        self.tamanho -= 1  # decrementa o tamanho da lista
        return True

    # Mostra os elementos da lista
    # Análise de complexidade: O(n)
    def mostrar(self):
        atual = self.inicio
        elementos = []
        while atual is not None:
            elementos.append(atual.dado)
            atual = atual.prox
        print("Lista:", elementos)


lista = ListaSimples()
lista.inserir_no_inicio(10)
lista.mostrar()  # Lista: [10]
lista.inserir_no_inicio(18)
lista.mostrar()  # Lista: [18, 10]
lista.inserir_no_fim(20)
lista.mostrar()  # Lista: [18, 10, 20]
lista.inserir_no_fim(29)
lista.mostrar()  # Lista: [18, 10, 20, 29]
lista.inserir_no_meio(15, 2)
lista.mostrar()  # Lista: [18, 10, 15, 20, 29]
print(lista.buscar(15))  # True
print(lista.buscar(25))  # False
lista.removerPeloValor(15)
lista.mostrar()  # Lista: [18, 10, 20, 29]
lista.removerPelaPosicao(0)
lista.mostrar()  # Lista: [10, 20, 29]
print("Tamanho da lista:", lista.tamanho)  # Tamanho da lista: 3
