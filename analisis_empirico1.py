# Algoritmo de una funcion para calcular la cantidad de números pares dentro de diferentes numeros N ingresados 
import matplotlib.pyplot as plt
import time

#Se importa el módulo time, que permite medir el tiempo de ejecución de un bloque de código.

#Se define una función llamada pares que recibe un parámetro n, que representa el 
#límite superior del rango de números a analizar (desde 1 hasta n)
def pares(n):
    start = time.time()     #Se guarda el tiempo de inicio justo antes de comenzar el procesamiento. 
                            #Esto servirá luego para calcular cuánto tiempo tardó en ejecutarse el algoritmo.                    
    pares = 0       #Se inicializa la variable pares en 0, donde se contabilizarán los números pares encontrados.
    for i in range(1, n + 1):  #Se utiliza un bucle for para recorrer todos los números desde 1 hasta n.                  
        if i % 2 == 0:  #Si el número actual es divisible por 2 (es decir, es par), se incrementa la variable pares.                
            pares += 1
                                #Se termina el bucle for.
    end = time.time()       #Se guarda el tiempo de finalización del bucle.
    return pares,(end - start)*1000  #Se devuelve la cantidad de números pares encontrados y el tiempo de ejecución en milisegundos.

# print("Algoritmo 1:")
# print(f"Tiempo para la cantidad de numeros pares con n = 10 son: {pares(10)}")
# print(f"Tiempo para la cantidad de numeros pares con n = 100 son: {pares(100)}")
# print(f"Tiempo para la cantidad de numeros pares con n = 1000 son: {pares(1000)}")
# print(f"Tiempo para la cantidad de numeros pares con n = 10000 son: {pares(10000)}")

# Cantidad de números pares:

# Para N = 10, el resultado es 5, lo que es correcto (pares: 2, 4, 6, 8, 10).
# Para N = 100, el resultado es 50, ya que hay 50 números pares en el rango de 1 a 100.
# Para N = 1000, el resultado es 500, siguiendo la misma lógica.

# Tiempo de ejecución:

# Para valores bajos (N = 10 y N = 100), el tiempo es prácticamente el mismo (0.0069 ms), ya que la ejecución es muy rápida.
# Para N = 1000, el tiempo aumenta ligeramente (0.0474 ms), lo que es lógico porque hay más iteraciones.

# En resumen, la complejidad del algoritmo es O(N), donde N es el tamaño de la entrada.


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
