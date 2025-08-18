class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


class PilhaDinamica:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.topo is None

    def verificar_topo(self):
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        return self.topo.valor

    def empilhar(self, valor):
        novo_no = No(valor)
        novo_no.proximo = self.topo
        self.topo = novo_no
        self.tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        valor = self.topo.valor
        self.topo = self.topo.proximo
        self.tamanho -= 1
        return valor

    def tamanho(self):
        return self.tamanho

    def __str__(self):
        if self.esta_vazia():
            return "Pilha vazia"
        itens = []
        atual = self.topo
        while atual:
            itens.append(atual.valor)
            atual = atual.proximo
        return "Pilha: " + str(itens)


# Exemplo de uso da pilha dinâmica
pilha = PilhaDinamica()
print(pilha)
pilha.empilhar(10)
pilha.empilhar(20)
print(pilha)
print("Topo:", pilha.verificar_topo())
desempilhado = pilha.desempilhar()
print("Desempilhado:", desempilhado)
print(pilha)
print("Tamanho da pilha:", pilha.tamanho)
pilha.empilhar(30)
print(pilha)
