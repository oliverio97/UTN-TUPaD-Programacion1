# ### ACTIVIDAD 1 - FUNCION HOLA MUNDO ###


# def imprimir_hola_mundo():
#     print("Hola Mundo!")


# imprimir_hola_mundo()


# ### ACTIVIDAD 2 -  FUNCION SALUDAR USUARIO ###


# def saludar_usuario(nombre):
#     print(f"Hola {nombre}!")


# nombre = input("Ingresa tu nombre: ")
# saludar_usuario(nombre)


# ### ACTIVIDAD 3 - FUNCION INFORMACION PERSONAL ###


# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


# nombre = input("Ingresa tu nombre: ")
# apellido = input("Ingresa tu apellido: ")
# edad = input("Ingresa tu edad: ")
# residencia = input("Ingresa tu lugar de residencia: ")

# informacion_personal(nombre, apellido, edad, residencia)


# ### ACTIVIDAD 4 - CALCULAR AREA DEL CIRCULO ###


# import math


# def calcular_area_circulo(radio):
#     return math.pi * radio**2


# def calcular_perimetro_circulo(radio):
#     return 2 * math.pi * radio


# radio = int(input("Ingrese el radio del circulo: "))

# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# print(
#     f"El area del circulo es: {area:.2f} \nEl perimetro del circulo es: {perimetro:.2f}"
# )


### ACTIVIDAD 5 - FUNCION DE SEGUNDOS A HORAS ###


# def segundos_a_horas(segundos):
#     if segundos >= 3600:
#         return segundos // 3600
#     elif segundos < 3600 and segundos > 0:
#         return 0
#     else:
#         return None


# segundos = int(
#     input(
#         "Ingresa la cantidad de segundos para obtener la cantidad de horas en dichos segundos: "
#     )
# )
# horas = segundos_a_horas(segundos)

# if segundos_a_horas(segundos) == None:
#     print("No has ingresado una cantidad valida de segundos.")
# else:
#     print(f"La cantidad de horas en {segundos} segundos es: {horas}")


### ACTIVIDAD 6 - FUNCION TABLA DE MULTIPLICAR ###


# def tabla_multiplicar(numero):
#     for i in range(1, 11):
#         print(f"{numero} X {i} =  {numero * i}")


# numero = int(
#     input("Ingrese un numero para conocer su tabla de multiplicar de 1 al 10: ")
# )

# tabla_multiplicar(numero)


### ACTIVIDAD 7 - FUNCION OPERACIONES BASICAS ###


def operaciones_basicas(a, b):
    if b == 0:
        return None
    tupla = a + b, a - b, a * b, a / b
    return tupla


var = operaciones_basicas(10, 5)
if var is None:
    print(
        "No has ingresado un numero valido para la division. Recorda que no se puede dividir por 0."
    )
else:
    suma, resta, multiplicacion, division = var
    print(f"a + b = {suma}")
    print(f"a - b = {resta}")
    print(f"a * b = {multiplicacion}")
    print(f"a / b = {division}")


### ACTIVIDAD 8 - CALCULAR IMC ###


# def calcular_imc(peso, altura):
#     return peso / (altura**2)


# peso = float(input("Ingresa tu peso en kilogramos: "))
# altura = float(input("Ingresa tu altura en metros: "))

# IMC = calcular_imc(peso, altura)

# print(f"Tu IMC es de: {IMC:.2f}")


### ACTIVIDAD 9 - DE CELCUIS A FARENHEIT ###
