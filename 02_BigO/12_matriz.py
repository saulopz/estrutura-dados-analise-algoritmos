def mostrar_matriz(matriz, n, m):
    for i in range(n):  # n linhas
        for j in range(m):  # m colunas
            print(matriz[i][j])


matriz = [
    [1, 2],
    [3, 4],
    [5, 6],
]
linhas = 3
colunas = 2
mostrar_matriz(matriz, linhas, colunas)
