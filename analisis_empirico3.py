import time
import matplotlib.pyplot as plt

def pares(n):
    start = time.time()
    pares_array = [i for i in range(2, n + 1, 2)]  
    end = time.time()
    return len(pares_array), (end - start) * 1000  # tiempo en milisegundos

# Valores de prueba
valores_n = [50, 100, 200, 400, 800, 1600, 3200, 6400, 12800]
tiempos = []

# Ejecutar y guardar tiempos
for n in valores_n:
    _, tiempo = pares(n)
    tiempos.append(tiempo)
    print(f"Tiempo para n = {n}: {tiempo:.5f} ms")

# Graficar barras
plt.figure(figsize=(10, 6))
plt.bar([str(n) for n in valores_n], tiempos, color='skyblue')
plt.title('Tiempo de ejecución de la función pares(n)')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo (milisegundos)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()