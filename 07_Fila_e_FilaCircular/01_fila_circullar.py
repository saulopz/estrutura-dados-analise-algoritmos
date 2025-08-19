class FilaCircular:
    def __init__(self, max=10):
        self.MAX = max
        self.dados = [None] * max  # vetor fixo
        self.frente = 0            # índice do primeiro
        self.tras = 0              # índice do próximo espaço livre
        self.qtd = 0               # quantidade de elementos

    def isEmpty(self):
        return self.qtd == 0

    def isFull(self):
        return self.qtd == self.MAX

    def enqueue(self, valor):
        if self.isFull():
            print("Fila cheia! Não é possível enfileirar.")
            return
        self.dados[self.tras] = valor
        # avança o índice de tras circularmente
        self.tras = (self.tras + 1) % self.MAX
        self.qtd += 1

    def dequeue(self):
        if self.isEmpty():
            print("Fila vazia! Não é possível desenfileirar.")
            return None
        valor = self.dados[self.frente]
        # avança o índice de frente circularmente
        self.frente = (self.frente + 1) % self.MAX
        self.qtd -= 1
        return valor

    def peek(self):
        if self.isEmpty():
            print("Fila vazia! Não há frente.")
            return None
        return self.dados[self.frente]

    def show(self):
        # Mostramos a fila no estilo didático
        # Como em linguagem C, varrendo manualmente
        i = self.frente
        elementos = []
        for _ in range(self.qtd):
            elementos.append(self.dados[i])
            i = (i + 1) % self.MAX
        print("Fila:", elementos)


# --- Teste ---
fila = FilaCircular(5)

fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
fila.show()  # [10, 20, 30]

print("Frente:", fila.peek())  # 10

print("Saiu:", fila.dequeue())  # remove 10
fila.show()  # [20, 30]

fila.enqueue(40)
fila.enqueue(50)
fila.enqueue(60)  # deve dar a volta
fila.show()  # [20, 30, 40, 50, 60]

print("Saiu:", fila.dequeue())  # remove 20
fila.show()  # [30, 40, 50, 60]
