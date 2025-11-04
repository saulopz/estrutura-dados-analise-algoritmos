class No:
    def __init__(self, dados):
        self.dados = dados
        self.filhos = []

    def adicionar_filho(self, no):
        self.filhos.append(no)

    def __repr__(self):
        return f"No('{self.dados}')"  # Facilitar a visualização.


# Percorre a árvore em Pré-Ordem (Raiz -> Filhos).
# A indentação mostra a hierarquia.
def percorrer_pre_ordem(no_atual, nivel=0):
    print("  " * nivel + f"- {no_atual.dados}")  # 1. Visita a Raiz (nó atal)
    for filho in no_atual.filhos:  # 2. Percorre recursivamente cada filho
        percorrer_pre_ordem(filho, nivel + 1)


# 1. Criação dos nós
raiz = No("Documentos")
pastas = No("Pastas")
arquivos = No("Arquivos")
fotos = No("Fotos Pessoais")
relatorio = No("Relatorio.pdf")
imagem1 = No("viagem.jpg")
imagem2 = No("familia.png")

# 2. Construindo a estrutura (Hierarquia)

# Nível 1: Filhos da Raiz "Documentos"
raiz.adicionar_filho(pastas)
raiz.adicionar_filho(arquivos)

# Nível 2: Filhos de "Arquivos"
arquivos.adicionar_filho(relatorio)

# Nível 2: Filhos de "Pastas"
pastas.adicionar_filho(fotos)

# Nível 3: Filhos de "Fotos Pessoais"
fotos.adicionar_filho(imagem1)
fotos.adicionar_filho(imagem2)

# Imprimindo a lista de filhos da raiz para verificar:
# print(f"Filhos da Raiz '{raiz.dados}': {raiz.filhos}")
# Saída: Filhos da Raiz 'Documentos': [No('Pastas'), No('Arquivos')]

print("\n--- Percurso Pré-Ordem (Hierarquia) ---")
percorrer_pre_ordem(raiz)
