class No:
    def __init__(self, valor):
        self.dado = valor
        self.prox = None

class ListaSimples:
    # Inicializa a lista vazia
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def inserir_no_inicio(self, valor):
        novo = No(valor)
        novo.prox = self.inicio
        self.inicio = novo
        self.tamanho += 1

    def inserir_no_fim(self, valor):
        novo = No(valor)
        if self.inicio is None:
            self.inicio = novo
            return
        atual = self.inicio
        while atual.prox is not None:
            atual = atual.prox
        atual.prox = novo
        self.tamanho += 1

    def inserir_no_meio(self, valor, posicao):
        # Verifica se a posição é válida
        if posicao < 0 or posicao > self.tamanho:
            raise IndexError("Posição inválida")
        novo = No(valor) # Cria um novo nó
        # Se a posição for 0, insere no início
        if posicao == 0:
            self.inserir_no_inicio(valor)
            return
        atual = self.inicio # atual aponta para o início
        # percorre até a posição anterior
        for _ in range(posicao - 1): 
            atual = atual.prox
        novo.prox = atual.prox # novo aponta para o próximo
        atual.prox = novo # atual aponta para o novo
        self.tamanho += 1 # incrementa o tamanho da lista


    def buscar(self, valor):
        atual = self.inicio
        while atual is not None:
            if atual.dado == valor:
                return True
            atual = atual.prox
        return False

    # Remove o primeiro nó com o valor especificado
    def remover(self, valor):
        atual = self.inicio # aponta para o início
        anterior = None # aponta para o nó anterior
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
                self.tamanho -= 1 # decrementa o tamanho da lista
                return True
            anterior = atual # atualiza o nó anterior
            atual = atual.prox # atualiza o nó atual
        return False

    def mostrar(self):
        atual = self.inicio
        elementos = []
        while atual is not None:
            elementos.append(atual.dado)
            atual = atual.prox
        print("Lista:", elementos)
