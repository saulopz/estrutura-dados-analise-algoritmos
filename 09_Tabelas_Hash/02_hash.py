# Tabela Hash com tratamento de colisão por encadeamento
# Autor: Saulo Popov Zambiasi
# Data: 25 de setembro de 2025
# Disciplina de Estruturas de Dados e Análise de Algoritmos
# Aula de Tabelas Hash
#
# Descrição: Implementação de uma tabela hash com tratamento de colisão
# por encadeamento. A tabela armazena contatos com código, nome e email.
# A função de hash utilizada é o operador mod.
#
# Observações: Poderiamos ter utilizado a implementação de lista encadeada
# que desenvolvemos anteriormente, mas para simplificar, utilizamos listas
# nativas do Python.

# Classe para representar um contato
class Contato:
    def __init__(self, codigo, nome, email):
        self.codigo = codigo
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.codigo}: {self.nome}, {self.email}"


# Tabela Hash com tratamento de colisão por encadeamento
class Hash:
    def __init__(self, tamanho_tabela):
        self.tamanho = tamanho_tabela                      # tamanho de hash
        self.tabela = [[] for _ in range(tamanho_tabela)]  # inicializa a tabela        


    # Função de hash simples: key mod tamanho
    def func_hash(self, key):
        return key % self.tamanho

    # Insere um contato na tabela hash
    def inserir(self, contato):
        chave = self.func_hash(contato.codigo) # calcula o índice
        self.tabela[chave].append(contato)     # insere o contato na lista do índice

    # Busca um contato na tabela hash pelo código
    def buscar(self, codigo):
        chave = self.func_hash(codigo)
        if self.tabela[chave] is not None:      # se a lista não está vazia
            for contato in self.tabela[chave]:  # percorre a lista
                if contato.codigo == codigo:    # se encontrar o contato
                    return contato              # retorna o contato
        return None

    # Adicionar este método à classe Hash:
    def mostrar_tabela(self):
        print("\n--- Estado da Tabela Hash ---")
        for i, dado in enumerate(self.tabela):
            print(f"[{i}]:", end=" ")
            if dado is None:
                print("vazio")
            else:
                contatos = [str(c) for c in dado]
                print(" -> ".join(contatos))
        print("-----------------------------\n")


# Exemplo de uso
hash_table = Hash(4)
hash_table.inserir(Contato(2, "Saulo", "saulopz@gmail.com"))
hash_table.inserir(Contato(6, "Joao", "joao@gmail.com"))
hash_table.inserir(Contato(13, "Marta", "marta@gmail.com"))
hash_table.inserir(Contato(12, "Roberta", "roberta@gmail.com"))
hash_table.inserir(Contato(7, "Marta", "marta@gmail.com"))
hash_table.mostrar_tabela()

# Busca e imprime contatos
for i in range(20):
    contato = hash_table.buscar(i)
    if contato is not None:
        print(f"{hash_table.func_hash(i)} - {contato}")
