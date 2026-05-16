### ACTIVIDAD 1 - EXPLICACION DE ERRORES EN CODIGO ###

a = 10
b = input(
    "Introduce un número: "
)  # ACA SE PIDE POR CONSOLA UN NUMERO PERO LA FUNCION INPUT PREDETERMINADAMENTE DEVUELVE UN STRING A MENOS QUE SE CONVIERTA CON INT()
result = (
    a / b
)  # ACA SE INTENTA REALIZAR UNA OPERACION NO VALIDA, SE INTENTA DIVIDIR UN ENTERO POR UN STRING. SE PRODUCE UNA EXCEPCION DE TIPO TYPE ERROR
print(f"Resultado: {result}")


numbers = [1, 2, 3]
print(
    numbers[5]
)  # ACA SE INTENTA ACCEDER A UN INDICE INEXISTENTE EN LA LISTA, DADO QUE LA LISTA SOLO TIENE 3 ELEMENTOS, POR LO QUE EL ULTIMO ELEMENTO SERA INDICE [2]


### ACTIVIDAD 2 - ARREGLO DEL CODIGO ANTERIOR ###

a = 10
b = int(
    input("Introduce un numero: ")
)  # se agrega la funcion int para convertir a entero lo introducido por el usuario
result = a / b
print(f"Resultado: {result}")

numbers = [1, 2, 3]
print(numbers[-1])  # visualizamos el ultimo elemento de la lista


### ACTIVIDAD 3 - CODIGO ANTERIOR CON BLOQUES TRY- EXCEPT ###

try:
    a = 10
    b = input("Introduce un numero: ")
    result = a / b
    print(f"Resultado: {result}")
    numbers = [1, 2, 3]
    print(numbers[5])
except:
    print("operacion no soportada")


### ACTIVIDAD 4 - MANEJO DE MULTIPLES EXCEPCIONES ###

# bloque 1: manejo de excepciones sobre la operacion.
try:
    a = 10
    b = input("Introduce un numero: ")
    result = a / b
    print(f"Resultado: {result}")
except TypeError:
    print(
        "operacion no soportada"
    )  # este es el unico error que va a arrojar la operacion
except ZeroDivisionError:
    print("No es posible dividir por cero.")
except Exception as e:
    print("Ocurrió el siguiente error: ", type(e).__name__)

# bloque 2: excepciones sobre lista
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Indice fuera de rango")
except Exception as e:
    print("Ocurrió el siguiente error: ", type(e).__name__)


### ACTIVIDAD 5 - CODIGO CON BLOQUES ELSE Y FINALLY ###

try:
    a = 10
    b = input("Introduce un numero: ")
    result = a / b
    print(f"Resultado: {result}")
except TypeError:
    print("operacion no soportada")
except ZeroDivisionError:
    print("No es posible dividir por cero.")
except Exception as e:
    print("Ocurrió el siguiente error: ", type(e).__name__)
else:
    print("El programa se ha ejecutado correctamente")
finally:
    print("Fin del programa")


try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("Indice fuera de rango")
except Exception as e:
    print("Ocurrió el siguiente error: ", type(e).__name__)
else:
    print("El programa se ha ejecutado correctamente")
finally:
    print("Fin del programa")

### ACTIVIDAD 6 - MANEJO DE NUMERO INTRODUCIDO POR EL USUARIO ###

try:
    numero = int(input("Ingresa un numero: "))
except ValueError:
    print("Debe ingresar un numero valido.")
except Exception as e:
    print(f"Ocurrio un error inesperado: {type(e).__name__}")
else:
    print(f"El numero ingresado es {numero}")


### ACTIVIDAD 7 - BUCLE CON MANEJO DE ERROR ###

while True:
    try:
        numero = int(input("Ingresa un numero: "))
    except ValueError:
        print("Debe ingresar un numero valido.")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {type(e).__name__}")
    else:
        print(f"El numero ingresado es {numero}")
        break
