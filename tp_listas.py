import random

##### EJERCICIO 1 - LISTA CON NOTAS DE 10 ESTUDIANTES #####

notas_estudiantes = [9.5, 7, 6.5, 10, 5.5, 8, 7, 7.5, 8.5, 9]

# # Mostrando la lista completa, elemento por elemento
# for i in range(len(notas_estudiantes)):
#     print(f"nota {i+1}:  {notas_estudiantes[i]}")

# # calcular el promedio
# total_notas = 0
# for i in notas_estudiantes:
#     total_notas += i

# promedio = total_notas / len(notas_estudiantes)
# print(f"El promedio de las notas es: {promedio}")

# # obtener nota mas alta y mas baja
# nota_mas_alta = max(notas_estudiantes)
# nota_mas_baja = min(notas_estudiantes)

# print(f"La nota mas alta es: {nota_mas_alta}")
# print(f"La nota mas baja  es: {nota_mas_baja}")


# ##### EJERCICIO 2 - LISTA CON INPUT PARA CARGAR PRODUCTOS #####

# # crear lista con input
# lista_productos = []
# for i in range(5):
#     lista_productos.append(input(f"Ingrese el producto numero {i+1}: "))

# # ordenar e imprimir la lista ordenada
# lista_productos_ordenada = sorted(lista_productos)
# for i in lista_productos_ordenada:
#     print(f"producto n° {lista_productos_ordenada.index(i)+1}: {i}")

# # pedir al usuario que elimine un elemento y mostrar la lista actualizada
# lista_productos_ordenada.remove(input("Ingrese el elemento que desea eliminar: "))

# for i in lista_productos_ordenada:
#     print(f"producto n° {lista_productos_ordenada.index(i)+1}: {i}")


##### EJERCICIO 3 - LISTA CON NUMEROS AL AZAR #####

# generando lista vacia y llenandola con numeros al azar entre 1-100
lista_numeros = []

for i in range(100):
    lista_numeros.append(random.randint(1, 100))

# creando lista de pares y lista de impares y llenandolas segun corresponda

lista_pares = []
lista_impares = []

for i in lista_numeros:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

# mostrando cuantos numeros tiene cada lista
cant_pares = len(lista_pares)
cant_impares = len(lista_impares)
print(f"La lista de numeros pares tiene {cant_pares} numeros.")
print(f"La lista de numeros impares tiene {cant_impares} numeros.")
