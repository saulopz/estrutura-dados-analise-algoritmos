class Pilha:
    def __init__(self, capacidade):
        self.itens = [None] * capacidade
        self.topo = -1

    def esta_vazia(self):
        return self.topo == -1

    def esta_cheia(self):
        return self.topo == len(self.itens) - 1

    def verificar_topo(self):
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        return self.itens[self.topo]

    def empilhar(self, item):
        if self.esta_cheia():
            raise Exception("Pilha cheia")
        self.topo += 1
        self.itens[self.topo] = item

    def desempilhar(self):
        if self.esta_vazia():
            raise Exception("Pilha vazia")
        item = self.itens[self.topo]
        self.topo -= 1
        return item

    def tamanho(self):
        return self.topo + 1

    def __str__(self):
        if self.esta_vazia():
            return "Pilha vazia"
        return "Pilha: " + str(self.itens[: self.topo + 1])


# Exemplo de uso da pilha
pilha = Pilha(5)
print(pilha)

pilha.empilhar(10)
pilha.empilhar(20)
print(pilha)

print("Topo:", pilha.verificar_topo())

desempilhado = pilha.desempilhar()
print("Desempilhado:", desempilhado)
print(pilha)

print("Tamanho da pilha:", pilha.tamanho())

pilha.empilhar(30)
print(pilha)

while not pilha.esta_vazia():
    print("Desempilhando:", pilha.desempilhar())

print(pilha)  # Deve mostrar que a pilha está vazia
