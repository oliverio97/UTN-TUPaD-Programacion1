### EJERCICIO 1 - FUNCION BASICA ###


def saludar_usuario(nombre):
    return f"Hola {nombre}!"


nombre = input("Ingresa tu nombre: ")
saludo = saludar_usuario(nombre)
print(saludo)

### EJERCICIO 2 - PARAMETROS Y RETORNO ###


def suma(a, b):
    return a + b


num1 = 5
num2 = 10

sumar = suma(num1, num2)

print(sumar)


### EJERCICIO 3 - USO DE CONDICIONALES ###


def es_par(x):
    if x % 2 == 0:
        return True
    return False


num_par = 12
num_impar = 7

print(f"{num_par} es un numero par? {es_par(num_par)}")
print(f"{num_impar} es un numero impar? {es_par(num_impar)}")


### EJERCICIO 4 - REUTILIZACION DE FUNCIONES ###


def calcular_promedio(a, b, c):
    return (a + b + c) / 3


def aprobado(x):
    if x >= 6:
        return "Aprobado"
    return "Desaprobado"


# Prueba con un promedio aprobado
promedio1 = calcular_promedio(6, 7, 9)
aprobo = aprobado(promedio1)
print(f"El promedio de {promedio1:.2f} esta aprobado")

# prueba con un promedio desaprobado

promedio2 = calcular_promedio(5, 4, 6)
no_aprobo = aprobado(promedio2)
print(f"El promedio de {promedio2} esta desaprobado")


### EJERCICIO 5 - LISTAS Y LOGICA ###


def mayor_de_lista(lista):
    mayor = 0
    for i in lista:
        if i > mayor:
            mayor = i
    return mayor


lista = [1, 5, 47, 13, 22, -5, 12, 9, 11]

busqueda_num_mayor = mayor_de_lista(lista)

print(f"El numero mayor de la lista es: {busqueda_num_mayor}")
