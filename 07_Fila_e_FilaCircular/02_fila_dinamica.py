# Nó da lista encadeada
class No:
    def __init__(self, valor):
        self.dado = valor   # informação a ser armazenada
        self.prox = None    # ponteiro para o próximo nó

# Fila dinâmica
class FilaDinamica:
    # construtor, inicializa a fila vazia
    def __init__(self):
        self.frente = None   # ponteiro para o primeiro nó
        self.tras = None     # ponteiro para o último nó
        self.qtd = 0         # quantidade de elementos
                             # -> não obrigatório, mas útil

    # verifica se a fila está vazia
    def isEmpty(self):
        return self.frente is None

    # adiciona elemento na fila
    def enqueue(self, valor):
        novo = No(valor)           # cria nó
        if self.isEmpty():
            self.frente = novo     # frente e tras apontam para o mesmo nó
            self.tras = novo
        else:
            self.tras.prox = novo  # liga último nó ao novo
            self.tras = novo       # atualiza o ponteiro tras
        self.qtd += 1

    # remove elemento da fila
    def dequeue(self):
        if self.isEmpty():
            print("Fila vazia!")
            return None
        valor = self.frente.dado
        self.frente = self.frente.prox  # avança frente
        if self.frente is None:         # se ficou vazia
            self.tras = None
        self.qtd -= 1
        return valor

    # retorna o valor da frente
    def peek(self):
        if self.isEmpty():
            print("Fila vazia!")
            return None
        return self.frente.dado

    # mostra os elementos da fila
    def show(self):
        elementos = []
        atual = self.frente
        while atual is not None:
            elementos.append(atual.dado)
            atual = atual.prox
        print("Fila:", elementos)


# --- Teste ---
fila = FilaDinamica()

fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
fila.show()   # [10, 20, 30]

print("Frente:", fila.peek())  # 10

print("Saiu:", fila.dequeue()) # remove 10
fila.show()   # [20, 30]

fila.enqueue(40)
fila.enqueue(50)
fila.show()   # [20, 30, 40, 50]

print("Saiu:", fila.dequeue()) # remove 20
fila.show()   # [30, 40, 50]
