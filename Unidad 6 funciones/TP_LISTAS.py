### ACTIVIDAD 1 - FUNCION HOLA MUNDO ###


def imprimir_hola_mundo():
    print("Hola Mundo!")


imprimir_hola_mundo()


### ACTIVIDAD 2 -  FUNCION SALUDAR USUARIO ###


def saludar_usuario(nombre):
    print(f"Hola {nombre}!")


nombre = input("Ingresa tu nombre: ")
saludar_usuario(nombre)


### ACTIVIDAD 3 - FUNCION INFORMACION PERSONAL ###


def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)
