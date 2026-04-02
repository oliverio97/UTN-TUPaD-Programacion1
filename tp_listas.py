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


##### EJERCICIO 4 - LISTA CON VALORES REPETIDOS #####

# creando lista con repetidos y borrando los mismos en nueva lista

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

lista_sin_repetidos = []

for i in datos:
    if i not in lista_sin_repetidos:
        lista_sin_repetidos.append(i)

# mostrando elemento por elemento de la lista sin repetidos
for i in range(len(lista_sin_repetidos)):
    print(lista_sin_repetidos[i])


##### EJERCICIO 5 - LISTA CON NOMBRES DE ESTUDIANTES PRESENTES #####

lista_estudiantes = [
    "Leonel Messi",
    "Enzo Fernandez",
    "Emiliano Martinez",
    "Rodrigo DePaul",
    "Lionel Scaloni",
    "Julian Alvarez",
    "Lautaro Martinez",
    "Nicolas Paz",
]

# agregando nuevo estudiante o eliminando segun corresponda
estudiante = input(
    "Ingrese nombre del estudiante. Si ingresa un nombre ya existente, el mismo será borrado de la lista. En caso contrario, el nombre será añadido: "
)
if estudiante in lista_estudiantes:
    lista_estudiantes.remove(estudiante)
else:
    lista_estudiantes.append(estudiante)

for i in range(len(lista_estudiantes)):
    print(lista_estudiantes[i])


##### EJERCICIO 6 - ROTAR ELEMENTOS DE LISTA  #####

# creando lista con numeros
lista_con_numeros = [1, 2, 3, 4, 5, 6, 7]

# pegando el ultimo numero al principio y sumandole el resto despues
lista_con_numeros = lista_con_numeros[-1:] + lista_con_numeros[:-1]

print(lista_con_numeros)


##### EJERCICIO 7 - MATRIZ CON TEMPERATURAS  #####

temperaturas = [[30, 33][15, 32][25, 33][8, 16][10, 19][12, 22][15, 34]]
