import time
# optimizar el cálculo reemplazando el bucle por una operación matemática.

def cantidad_pares_optimizado(n):
    import time
    start = time.time()
    pares = n // 2  # Simplemente calcula cuántos números pares hay
    end = time.time()
    return pares, (end - start) * 1000


print(f"Tiempo para la cantidad de numeros pares con n = 10 son: {cantidad_pares_optimizado(10)}")
print(f"Tiempo para la cantidad de numeros pares con n = 100 son: {cantidad_pares_optimizado(100)}")
print(f"Tiempo para la cantidad de numeros pares con n = 1000 son: {cantidad_pares_optimizado(1000)}")
print(f"Tiempo para la cantidad de numeros pares con n = 10000 son: {cantidad_pares_optimizado(10000)}")

# En lugar de recorrer todos los números para contar los pares, simplemente calculamos N // 2, porque la mitad de los números enteros hasta N son pares.
# Esta solución es constante, ya que independientemente del valor de N, la operación matemática se resuelve en un único paso.
# La complejidad pasa de O(N) a O(1), lo que significa que el tiempo de ejecución no aumenta con el tamaño de la entrada.
# Con O(1), la operación se ejecuta en un tiempo constante, lo que lo hace mucho más eficiente para valores grandes de N.
# En comparación, O(N) podría volverse lento si N crece significativamente (por ejemplo, N = 1,000,000).