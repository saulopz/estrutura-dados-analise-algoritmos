class No:
    def __init__(self, valor):
        self.dado = valor  # Valor do nó
        self.prox = None  # Ponteiro para o próximo nó
        self.ant = None  # Ponteiro para o nó anterior

class ListaDupla:
    # Inicializa a lista vazia
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    # Análise de complexidade: O(1)
    def inserir_no_inicio(self, valor):
        novo = No(valor)
        if self.inicio is None:  # A lista está vazia
            self.inicio = novo
            self.fim = novo
        else:
            novo.prox = self.inicio  # novo aponta para o antigo início
            self.inicio.ant = novo  # antigo início aponta para o novo
            self.inicio = novo  # início agora é o novo nó
        self.tamanho += 1

    # Análise de complexidade: O(1)
    def inserir_no_fim(self, valor):
        novo = No(valor)
        if self.fim is None:  # A lista está vazia
            self.inicio = novo
            self.fim = novo
        else:
            novo.ant = self.fim  # novo aponta para o antigo fim
            self.fim.prox = novo  # antigo fim aponta para o novo
            self.fim = novo  # fim agora é o novo nó
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
        novo.ant = atual  # novo aponta para o anterior
        if atual.prox is not None:
            atual.prox.ant = novo  # próximo do atual aponta para o novo
        atual.prox = novo  # atual aponta para o novo
        self.tamanho += 1  # incrementa o tamanho da lista

    # Análise de complexidade: O(n)
    def buscar(self, valor):
        atual = self.inicio
        while atual is not None:
            if atual.dado == valor:
                return True
            atual = atual.prox
        return False
    
    # Remove o primeiro nó com o valor especificado
    # Análise de complexidade: O(n)
    def removerPeloValor(self, valor):
        atual = self.inicio  # aponta para o início
        while atual is not None:
            if atual.dado == valor:
                if atual.ant is not None:
                    atual.ant.prox = atual.prox  # nó anterior aponta para o próximo
                else:
                    self.inicio = atual.prox  # atual é o início
                if atual.prox is not None:
                    atual.prox.ant = atual.ant  # nó próximo aponta para o anterior
                else:
                    self.fim = atual.ant  # atual é o fim
                self.tamanho -= 1  # decrementa o tamanho da lista
                return True
            atual = atual.prox  # atualiza o nó atual
        return False

    # Remove o nó na posição especificada
    # Análise de complexidade: O(n)
    def removerPelaPosicao(self, posicao):
        # Verifica se a posição é válida
        if posicao < 0 or posicao >= self.tamanho:
            raise IndexError("Posição inválida")

        atual = self.inicio  # aponta para o início
        # percorre até a posição desejada
        for _ in range(posicao):
            atual = atual.prox

        if atual.ant is not None:
            atual.ant.prox = atual.prox  # nó anterior aponta para o próximo
        else:
            self.inicio = atual.prox  # atual é o início

        if atual.prox is not None:
            atual.prox.ant = atual.ant  # nó próximo aponta para o anterior
        else:
            self.fim = atual.ant  # atual é o fim

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


lista = ListaDupla()
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