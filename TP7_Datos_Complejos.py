## EJERCICIO 1 - DICCIONARIO FRUTAS ###

precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

# añadimos pasando nueva clave y valor
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300


print(precios_frutas)


### EJERCICIO 2 - ACTUALIZAR PRECIOS DICCIONARIO FRUTAS ###

precios_frutas.update({"Banana": 1330})
precios_frutas.update({"Manzana": 1700})
precios_frutas.update({"Melon": 2800})


### EJERCICIO 3 - LISTA CON CLAVES ###

frutas = precios_frutas.keys()
lista_frutas = list(frutas)

print(lista_frutas)


## EJERCICIO 4 - NUMEROS TELEFONICOS ###

numeros_telefonicos = {}
for i in range(5):
    nombre = input("Ingresa un nombre de contacto: ")
    numero = input(f"Ingresa el numero de {nombre}: ")
    numeros_telefonicos.update({nombre: numero})

print(numeros_telefonicos)

consulta = input("Ingresa el nombre para buscar el contacto: ")

if consulta in numeros_telefonicos.keys():
    print(f"El numero de {consulta} es: {numeros_telefonicos[consulta]}")
else:
    print(f"El nombre {consulta} no se encuentra cargado.")


## EJERCICIO 5 - FRASE Y CONJUNTOS ###

frase = input("Ingresa una frase: ")
frase_conjunto = set(frase.split())
print(frase_conjunto)

frase_dict = frase.split()

dict_palabras = {}
for palabra in frase_conjunto:
    dict_palabras[palabra] = frase_dict.count(palabra)

print(dict_palabras)


## EJERCICIO 6 - ALUMNOS Y NOTAS ###

dict_notas = {}
for alumno in range(3):
    nombre_alumno = input("Ingresa el nombre del alumno: ")
    notas = 0
    for n in range(3):
        nota = float(input(f"Ingresa la nota {n+1}: "))
        notas += nota
    notas /= 3
    tupla_notas = (notas,)
    dict_notas[nombre_alumno] = tupla_notas

print(dict_notas)


## EJERCICIO 7 - ASISTENCIAS ###

asistencias = ["Ana", "Luis", "Ana", "Maria", "Luis", "Pedro", "Ana"]

conjunto_asistencias = set(asistencias)
print(f"Los empleados que asistieron al menos una vez fueron: {conjunto_asistencias}")

for i in conjunto_asistencias:
    print(f"{i} asistió {asistencias.count(i)} vez/veces.")


## EJERCICIO 8 - DICCIONARIO STOCK PRODUCTOS ###

productos = {
    "Papel Higienico": "20",
    "Jabon Liquido": "15",
    "Servilletas": "50",
    "Lavandina": "40",
    "Perfumina": "7",
    "Trapo de piso": "27",
}

print(f"Lista de productos con stock:")

for clave, valor in productos.items():
    print(f"{clave}: {valor}")

entrada_usuario = input(
    "Ingresa el nombre del producto para consultar stock si ya existe o agregarlo si no existe: "
)

if entrada_usuario in productos.keys():
    opcion = input(
        f"El producto {entrada_usuario} se encuentra en existencias. Ingrese 1 para consultar stock o 2 para agregar stock al producto: "
    )
    match opcion:
        case "1":
            print(
                f"El stock del producto {entrada_usuario} es: {productos[entrada_usuario]}"
            )
        case "2":
            agregar_stock = input(
                f"Ingrese las unidades para agregar stock a {entrada_usuario}: "
            )
            operacion = int(productos[entrada_usuario]) + int(agregar_stock)
            productos[entrada_usuario] = operacion
            print("lista de productos actualizada")
            for clave, valor in productos.items():
                print(f"{clave}: {valor}")
        case _:
            print("No ha ingresado una opcion valida.")
else:
    print(
        "El producto no existe. Ingrese las unidades para agregar el producto con su correspondiente stock."
    )
    agregar_stock = input(f"Unidades de {entrada_usuario}: ")
    productos[entrada_usuario] = agregar_stock
    print("lista de productos actualizada")
    for clave, valor in productos.items():
        print(f"{clave}: {valor}")


## EJERCICIO 9 - DICCIONARIO STOCK PRODUCTOS ###

agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "clase de ingles",
    ("miercoles", "11:00"): "yoga",
    ("jueves", "14:00"): "pilates",
    ("viernes", "18:00"): "padel",
}
lista_dias = agenda.keys()
print(lista_dias)
consulta_dia = input("Ingresa el dia para consultar actividad: ")
for elemento in lista_dias:
    if consulta_dia in elemento[0]:
        consulta_hora = input(
            f"Ingresa la hora para consultar actividad del dia {consulta_dia}: "
        )
        if consulta_hora in elemento[1]:
            print(
                f"La actividad agendad para el dia {consulta_dia} a las {consulta_hora} es : {agenda[elemento]}"
            )
            break
        else:
            print(
                f"No hay ninguna actividad agendada para el dia {consulta_dia} a esa hora."
            )
            break
else:
    print("No hay ninguna actividad agendada para el dia ingresado")


## EJERCICIO 10 - DICCIONARIO DE CAPITALES Y PAISES ###

dict_paises = {
    "argentina": "buenos aires",
    "chile": "santiago",
    "alemania": "berlin",
    "peru": "lima",
    "bolivia": "la paz",
}
dict_invertido = {}
for clave, valor in dict_paises.items():
    dict_invertido[valor] = clave

for clave, valor in dict_invertido.items():
    print(clave, ":", valor)
