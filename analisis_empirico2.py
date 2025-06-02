import time
# optimizar el cálculo reemplazando el bucle por una operación matemática.
import matplotlib.pyplot as plt
def pares(n):
    start = time.time()
    pares = n // 2  # Simplemente calcula cuántos números pares hay
    end = time.time()
    return pares, (end - start) * 1000

# print("Algoritmo 2:")
# print(f"Tiempo para la cantidad de numeros pares con n = 10 son: {pares(10)}")
# print(f"Tiempo para la cantidad de numeros pares con n = 100 son: {pares(100)}")
# print(f"Tiempo para la cantidad de numeros pares con n = 1000 son: {pares(1000)}")
# print(f"Tiempo para la cantidad de numeros pares con n = 10000 son: {pares(10000)}")

# En lugar de recorrer todos los números para contar los pares, simplemente calculamos N // 2, porque la mitad de los números enteros hasta N son pares.
# Esta solución es constante, ya que independientemente del valor de N, la operación matemática se resuelve en un único paso.
# La complejidad pasa de O(N) a O(1), lo que significa que el tiempo de ejecución no aumenta con el tamaño de la entrada.
# Con O(1), la operación se ejecuta en un tiempo constante, lo que lo hace mucho más eficiente para valores grandes de N.
# En comparación, O(N) podría volverse lento si N crece significativamente (por ejemplo, N = 1,000,000).


# Valores de prueba
valores_n = [50, 100, 200, 400, 800, 1600, 3200, 6400]
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