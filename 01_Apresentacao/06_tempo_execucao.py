import time


def lenta():
    for _ in range(10**6):
        pass


inicio = time.time()
lenta()
fim = time.time()

print(f"Tempo de execução: {fim - inicio:.4f} segundos")
