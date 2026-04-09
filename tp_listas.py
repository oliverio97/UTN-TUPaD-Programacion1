import random

##### EJERCICIO 1 - LISTA CON NOTAS DE 10 ESTUDIANTES #####

notas_estudiantes = [9.5, 7, 6.5, 10, 5.5, 8, 7, 7.5, 8.5, 9]

# Mostrando la lista completa, elemento por elemento
for i in range(len(notas_estudiantes)):
    print(f"nota {i+1}:  {notas_estudiantes[i]}")

# calcular el promedio
total_notas = 0
for i in notas_estudiantes:
    total_notas += i

promedio = total_notas / len(notas_estudiantes)
print(f"El promedio de las notas es: {promedio}")

# obtener nota mas alta y mas baja
nota_mas_alta = max(notas_estudiantes)
nota_mas_baja = min(notas_estudiantes)

print(f"La nota mas alta es: {nota_mas_alta}")
print(f"La nota mas baja  es: {nota_mas_baja}")


##### EJERCICIO 2 - LISTA CON INPUT PARA CARGAR PRODUCTOS #####

# crear lista con input
lista_productos = []
for i in range(5):
    lista_productos.append(input(f"Ingrese el producto numero {i+1}: "))

# ordenar e imprimir la lista ordenada
lista_productos_ordenada = sorted(lista_productos)
for i in lista_productos_ordenada:
    print(f"producto n° {lista_productos_ordenada.index(i)+1}: {i}")

# pedir al usuario que elimine un elemento y mostrar la lista actualizada
lista_productos_ordenada.remove(input("Ingrese el elemento que desea eliminar: "))

for i in lista_productos_ordenada:
    print(f"producto n° {lista_productos_ordenada.index(i)+1}: {i}")


##### EJERCICIO 3 - LISTA CON NUMEROS AL AZAR #####

# generando lista vacia y llenandola con numeros al azar entre 1-100
lista_numeros = []

for i in range(15):
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


temperaturas = [[30, 33], [15, 32], [25, 33], [8, 16], [10, 19], [12, 22], [15, 34]]

# calculando los totales de temperaturas maximas y minimas
total_minimas = 0
total_maximas = 0
for filas in temperaturas:
    total_minimas += filas[0]
    total_maximas += filas[1]

cant_dias = len(temperaturas)

promedio_minimas = total_minimas / cant_dias
promedio_maximas = total_maximas / cant_dias

print(f"El promedio de temperaturas minimas de la semana fue de: {promedio_minimas}")
print(f"El promedio de temperaturas maximas de la semana fue de: {promedio_maximas}")

amplitud_maxima = 0
dia_max_amplitud = 0
for filas in range(len(temperaturas)):
    amplitud_termica = temperaturas[filas][1] - temperaturas[filas][0]
    if amplitud_termica > amplitud_maxima:
        amplitud_maxima = amplitud_termica
        dia_max_amplitud = filas + 1
        print(amplitud_maxima)

print(
    f"La amplitud maxima fue de: {amplitud_maxima}, registrada en el dia {dia_max_amplitud}"
)


##### EJERCICIO 8 - MATRIZ CON NOTAS DE ESTUDIANTES  #####


matriz_notas = [[8, 9, 10], [7, 5.5, 6], [7.5, 6.5, 8], [9.5, 8.5, 7.5], [7, 6.5, 9]]

for (
    indice,
    filas,
) in enumerate(matriz_notas):
    suma_notas = filas[0] + filas[1] + filas[2]
    print(f"El promedio de notas del estudiante {indice+1} es: {suma_notas / 3:.2f}")


numero_materias = len(matriz_notas[0])
print(numero_materias)


for i in range(len(matriz_notas[0])):
    suma_columna = 0
    for j in range(len(matriz_notas)):
        suma_columna += matriz_notas[j][i]
    print(f"El promedio de la materia {i+1} es: {suma_columna / numero_materias}")


##### EJERCICIO 9 - TABLERO DE TA TE TI  #####


tateti = [["-" for i in range(3)] for j in range(3)]

print("Bienvenido al juego del Ta Te Ti\n")

for fila in tateti:
    print(fila)
print()

while True:
    jugador_1_fila = input(
        'Jugador 1, jugas con las "X" ingresa la fila del 1 al 3 para jugar: '
    )

    while not jugador_1_fila.isdigit() or int(jugador_1_fila) not in range(1, 4):
        print("No has ingresado un numero. Ingresa un numero entre 1-3.")
        jugador_1_fila = input("Jugador 1, ingresa la fila del 1 al 3 para jugar: ")

    jugador_1_fila = int(jugador_1_fila) - 1

    jugador_1_columna = input("Jugador 1, ingresa la columna del 1 al 3 para jugar: ")

    while not jugador_1_columna.isdigit() or int(jugador_1_columna) not in range(1, 4):
        print("No has ingresado un numero. Ingresa un numero entre 1-3.")
        jugador_1_columna = input(
            "Jugador 1, ingresa la columna del 1 al 3 para jugar: "
        )

    jugador_1_columna = int(jugador_1_columna) - 1

    tateti[jugador_1_fila][jugador_1_columna] = "X"

    for fila in tateti:
        print(fila)

    tablero_lleno = True
    for fila in tateti:
        if "-" in fila:
            tablero_lleno = False
            break

    if tablero_lleno:
        print(" El tablero está lleno.")
        break

    jugador2_fila = input(
        'Jugador 2, jugas con las "O" ingresa la fila del 1 al 3 para jugar: '
    )

    while not jugador2_fila.isdigit() or int(jugador2_fila) not in range(1, 4):
        print("No has ingresado un numero. Ingresa un numero entre 1-3.")
        jugador2_fila = input("Jugador 2, ingresa la fila del 1 al 3 para jugar: ")

    jugador2_fila = int(jugador2_fila) - 1

    jugador2_columna = input("Jugador 2, ingresa la columna del 1 al 3 para jugar: ")

    while not jugador2_columna.isdigit() or int(jugador2_columna) not in range(1, 4):
        print("No has ingresado un numero. Ingresa un numero entre 1-3.")
        jugador2_columna = input("Jugador2, ingresa la columna del 1 al 3 para jugar: ")

    jugador2_columna = int(jugador2_columna) - 1

    tateti[jugador2_fila][jugador2_columna] = "O"

    for fila in tateti:
        print(fila)

    tablero_lleno = True
    for fila in tateti:
        if "-" in fila:
            tablero_lleno = False
            break

    if tablero_lleno:
        print(" El tablero está lleno.")
        break


##### EJERCICIO 10 - VENTAS DE TIENDA  #####

ventas_tienda = [
    [55, 100, 150, 75, 38, 123, 85],
    [32, 201, 132, 67, 92, 94, 67],
    [112, 134, 200, 158, 173, 99, 79],
    [27, 64, 70, 103, 55, 12, 101],
]
producto_mas_vendido = 0
ventas_producto_mas_vendido = 0

dia_mas_ventas = 0
dia_ganador = 0
# mostrando el total de ventas por producto
for indice, filas in enumerate(ventas_tienda):
    suma_producto = 0
    for elemento in filas:
        suma_producto += elemento
    if suma_producto > ventas_producto_mas_vendido:
        ventas_producto_mas_vendido = suma_producto
        producto_mas_vendido = indice + 1
    print(f"El total vendido del producto {indice + 1 } es: {suma_producto}\n")

print(
    f"El producto mas vendido es el producto n° {producto_mas_vendido} con {ventas_producto_mas_vendido} ventas\n"
)
for i in range(len(ventas_tienda[0])):
    suma_columna = 0
    for j in range(len(ventas_tienda)):
        suma_columna += ventas_tienda[j][i]
    print(f"el dia {i+1} tuvo en total: {suma_columna} ventas.\n")

    if suma_columna > dia_mas_ventas:
        dia_mas_ventas = suma_columna
        dia_ganador = i + 1

print(f"El día {dia_ganador} fue el mejor con {dia_mas_ventas} ventas.")


##### EJERCICIO 11 - LISTA CON NOMBRES DE ESTUDIANTES  #####


lista_estudiantes = [
    "Leonel Messi",
    "Enzo Fernandez",
    "Emiliano Martinez",
    "Rodrigo DePaul",
    "Lionel Scaloni",
    "Julian Alvarez",
    "Lautaro Martinez",
    "Nicolas Paz",
    "Franco Mastantuono",
    "Nicolas Otamendi",
]

busca_nombre = input("Ingrese el nombre del estudiante a buscar: ")

if busca_nombre in lista_estudiantes:
    print(
        f"El nombre se encontró en la lista en la posicion {lista_estudiantes.index(busca_nombre) + 1}"
    )
else:
    print("El nombre ingresado no está en la lista")


##### EJERCICIO 12 - LISTA CON NUMEROS ENTEROS #####


print(
    "A continuacion se le solicitara que ingrese 8 numeros enteros y se agregaran a una lista"
)
lista_enteros = []

for i in range(8):
    lista_enteros.append(int(input(f"Ingrese el numero {i+1}: ")))

print(f"La lista original es: {lista_enteros}")

lista_ordenada = sorted(lista_enteros)

print(f"La lista ordenada de menor a mayor es: {lista_ordenada}")

lista_ordenada.reverse()

print(f"La lista ordenada de mayor a menor es: {lista_ordenada}")


#### EJERCICIO 13 - LISTA DE PUNTAJES #####


puntajes = [450, 1200, 875, 990, 300, 1500, 640]

puntaje_mas_alto = 0
puntaje_mas_bajo = 999999

for i in puntajes:
    if i > puntaje_mas_alto:
        puntaje_mas_alto = i
    if i < puntaje_mas_bajo:
        puntaje_mas_bajo = i

print(f"El puntaje mas alto es: {puntaje_mas_alto}")
print(f"El puntaje mas bajo es: {puntaje_mas_bajo}")

puntajes.sort()
puntajes.reverse()

print(f"A continuacion, la lista ordenada: {puntajes}")

print(f"El puntaje 990 se encuentra en la posicion {puntajes.index(990)+1}")
