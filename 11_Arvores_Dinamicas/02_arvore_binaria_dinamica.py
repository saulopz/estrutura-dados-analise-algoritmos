class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinariaDinamica:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor, local):
        if local is None:
            self.raiz = No(valor)
        elif valor < local.valor:
            if local.esquerda is None:
                local.esquerda = No(valor)
            else:
                self.inserir(valor, local.esquerda)
        elif valor > local.valor:
            if local.direita is None:
                local.direita = No(valor)
            else:
                self.inserir(valor, local.direita)

    # precisa ser previamente ordenada
    def inserir_balanceada(self, lista):
        if not lista:
            return None
        mid = len(lista) // 2
        no = No(lista[mid])
        if self.raiz is None:
            self.raiz = no
        no.esquerda = self.inserir_balanceada(lista[:mid])
        no.direita = self.inserir_balanceada(lista[mid + 1:])
        return no

    def buscar(self, valor, local):
        if self.raiz is None:
            return False
        if valor == local.valor:
            return True
        elif valor < local.valor:
            if local.esquerda is None:
                return False
            else:
                return self.buscar(valor, local.esquerda)
        elif valor > local.valor:
            if local.direita is None:
                return False
            else:
                return self.buscar(valor, local.direita)

    def preOrdem(self, local):
        print(local.valor, end=" ")
        if local.esquerda is not None:
            self.preOrdem(local.esquerda)
        if local.direita is not None:
            self.preOrdem(local.direita)

    def emOrdem(self, local):
        if local.esquerda is not None:
            self.emOrdem(local.esquerda)
        print(local.valor, end=" ")
        if local.direita is not None:
            self.emOrdem(local.direita)

    def posOrdem(self, local):
        if local.esquerda is not None:
            self.posOrdem(local.esquerda)
        if local.direita is not None:
            self.posOrdem(local.direita)
        print(local.valor, end=" ")


vet = [19, 23, 27, 1, 3, 13, 52, 93, 54, 74]
vet = sorted(vet)

arvore = ArvoreBinariaDinamica()
arvore.inserir_balanceada(vet)
print("Pré-ordem:", end=" ")
arvore.preOrdem(arvore.raiz)
print("\nEm ordem:", end=" ")
arvore.emOrdem(arvore.raiz)
print("\nPós-ordem:", end=" ")
arvore.posOrdem(arvore.raiz)
print("\nRAIZ: ", arvore.raiz.valor)

print(arvore.buscar(94, arvore.raiz))
