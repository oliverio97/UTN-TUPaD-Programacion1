###### EJERCICIO 1 - "CAJA DEL KIOSCO" ######

nombre_cliente = input("Ingrese su nombre: ").strip()

while not nombre_cliente.isalpha() or nombre_cliente == "":
    print("Nombre incorrecto, ingrese su nombre, utilice solo letras: ")
    nombre_cliente = input("Ingrese su nombre: ").strip()


productos = input("ingresa la cantidad de productos a comprar: ").strip()

while not productos.isdigit() or int(productos) == 0:
    print("Ingrese solo numeros positivos para la cantidad de productos.")
    productos = input("ingresa la cantidad de productos a comprar: ")


total_sin_desc = 0
total_con_desc = 0
ahorro_total = 0

for i in range(1, int(productos) + 1):
    precio = int(input(f"Ingrese precio para el Producto {i}: "))
    tiene_descuento = input("Descuento (S/N): ").lower().strip()
    while not (tiene_descuento == "s" or tiene_descuento == "n"):
        print(
            "Error, ingrese solamente las letras S o N para indicar si tiene descuento."
        )
        tiene_descuento = input("Descuento (S/N): ").lower().strip()
    if tiene_descuento == "s":
        total_sin_desc += precio
        descuento = precio / 10
        precio = precio - descuento
        ahorro_total += descuento
    else:
        total_sin_desc += precio

total_con_desc = total_sin_desc - ahorro_total
promedio_por_producto = total_con_desc / int(productos)

print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc}")
print(f"Ahorro total: ${ahorro_total}")
print(f"Promedio por producto: ${promedio_por_producto:.2f}")

###### EJERCICIO 2 - ACCESO AL CAMPUS Y MENU SEGURO" ######

usuario_correcto = "alumno"
clave_correcta = "python123"
intentos_permitidos = 0

while intentos_permitidos < 3:
    print(f"Intento {intentos_permitidos+1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido\n")
        break
    else:
        print("Error: credenciales invalidas. \n")
        intentos_permitidos += 1


if intentos_permitidos == 3:
    print("Cuenta bloqueada.")
else:
    print("Bienvenido. Introduzca el numero de la opcion que desea acceder.")
    print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir: ")
    while True:
        menu = input("Opcion: ")
        if menu == "1":
            print("Inscripto")
        elif menu == "2":
            nueva_clave = input("Nueva clave: ")
            while len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
                nueva_clave = input("Nueva clave: ")
            confirma_clave = input("Ingrese nuevamente la nueva clave para confirmar: ")
            while confirma_clave != nueva_clave:
                print("Error. Las contraseñas no coinciden")
                confirma_clave = input(
                    "Ingrese nuevamente la nueva clave para confirmar: "
                )
            print("La clave se ha actualizado correctamente. ")
        elif menu == "3":
            print("¡Vas muy bien! No aflojes, vas a ser un gran programador.")
        elif menu == "4":
            print("Hasta luego.")
            break
        elif not menu.isdigit():
            print("Error: ingrese un número válido.")
        elif int(menu) < 1 or int(menu) > 4:
            print("Error: opción fuera de rango.")


###### Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)” ######

nombre_operador = input("Ingrese nombre del operador: ").replace(" ", "")

lunes_1 = ""
lunes_2 = ""
lunes_4 = ""
lunes_3 = ""
martes_1 = ""
martes_2 = ""
martes_3 = ""
turnos_lunes = 0
turnos_martes = 0


while not nombre_operador.isalpha():
    print("Ha ingresado un nombre incorrecto. Ingrese solo letras para el nombre. ")
    nombre_operador = input("Ingrese nombre del operador: ").replace(" ", "")


while True:
    print("Bienvenido a su agenda de turnos. ¿Que desea hace a continuacion?")
    menu = input(
        "Ingrese la opcion deseada para continuar: \n"
        "1. Reservar turno \n"
        "2. Cancelar Turno \n"
        "3. Ver agenda del dia \n"
        "4. Ver resumen general \n"
        "5. Salir \n"
    )
    match menu:
        case "1":
            dia = input("Ingrese el numero para elegir dia: 1-Lunes 2-Martes: ")
            while not (dia == "1" or dia == "2"):
                print("Ingrese un dia correcto. Elija 1 para lunes o 2 para martes.")
                dia = input("Ingrese el numero para elegir dia: 1-Lunes 2-Martes: ")
            nombre_paciente = input(
                "Ingrese el nombre del paciente para reservar: "
            ).strip()
            while not nombre_paciente.isalpha():
                print("Nombre incorrecto. Ingrese solo letras para el paciente")
                nombre_paciente = input(
                    "Ingrese el nombre del paciente para reservar: "
                ).strip()
            while True:
                if dia == "1":
                    if (
                        nombre_paciente == lunes_1
                        or nombre_paciente == lunes_2
                        or nombre_paciente == lunes_3
                        or nombre_paciente == lunes_4
                    ):
                        print(
                            f"El paciente {nombre_paciente} ya tiene un turno reservado para ese dia."
                        )
                        break
                    else:
                        if len(lunes_1) == 0:
                            lunes_1 = nombre_paciente
                            turnos_lunes += 1
                            print("Turno reservado. Muchas gracias")
                            break
                        elif len(lunes_2) == 0:
                            lunes_2 = nombre_paciente
                            turnos_lunes += 1
                            print("Turno reservado. Muchas gracias")
                            break
                        elif len(lunes_3) == 0:
                            lunes_3 = nombre_paciente
                            turnos_lunes += 1
                            print("Turno reservado. Muchas gracias")
                            break
                        elif len(lunes_4) == 0:
                            lunes_4 = nombre_paciente
                            turnos_lunes += 1
                            print("Turno reservado. Muchas gracias")
                            break
                elif dia == "2":
                    if (
                        nombre_paciente == martes_1
                        or nombre_paciente == martes_2
                        or nombre_paciente == martes_3
                    ):
                        print(
                            f"El paciente {nombre_paciente} ya tiene un turno reservado para ese dia."
                        )
                        break
                    else:
                        if len(martes_1) == 0:
                            martes_1 = nombre_paciente
                            turnos_martes += 1
                            print("Turno reservado. Muchas gracias")
                            break
                        elif len(martes_2) == 0:
                            martes_2 = nombre_paciente
                            turnos_martes += 1
                            print("Turno reservado. Muchas gracias")
                            break
                        elif len(martes_3) == 0:
                            martes_3 = nombre_paciente
                            turnos_martes += 1
                            print("Turno reservado. Muchas gracias")
                            break

        case "2":
            dia_cancelar = input(
                "Ingrese el numero para elegir dia a cancelar: 1-Lunes 2-Martes: "
            )
            while not (dia_cancelar == "1" or dia_cancelar == "2"):
                print("Ingrese un dia correcto. Elija 1 para lunes o 2 para martes.")
                dia_cancelar = input(
                    "Ingrese el numero para elegir dia: 1-Lunes 2-Martes: "
                )
            nombre_paciente_cancelar = input(
                "Ingrese el nombre del paciente para cancelar: "
            ).strip()
            while not nombre_paciente_cancelar.isalpha():
                print("Nombre incorrecto. Ingrese solo letras para el paciente")
                nombre_paciente_cancelar = input(
                    "Ingrese el nombre del paciente para cancelar: "
                ).strip()
            if dia_cancelar == "1":
                if nombre_paciente_cancelar == lunes_1:
                    lunes_1 = ""
                    turnos_lunes -= 1
                    print(
                        f"Se ha cancelado el turno del paciente {nombre_paciente_cancelar} del dia {dia_cancelar}\n"
                    )
                elif nombre_paciente_cancelar == lunes_2:
                    lunes_2 = ""
                    turnos_lunes -= 1
                    print(
                        f"Se ha cancelado el turno del paciente {nombre_paciente_cancelar} del dia {dia_cancelar}\n"
                    )
                elif nombre_paciente_cancelar == lunes_3:
                    lunes_3 = ""
                    turnos_lunes -= 1
                    print(
                        f"Se ha cancelado el turno del paciente {nombre_paciente_cancelar} del dia {dia_cancelar}\n"
                    )
                elif nombre_paciente_cancelar == lunes_4:
                    lunes_4 = ""
                    turnos_lunes -= 1
                    print(
                        f"Se ha cancelado el turno del paciente {nombre_paciente_cancelar} del dia {dia_cancelar}\n"
                    )
                else:
                    print(
                        f"El paciente {nombre_paciente_cancelar} no tiene turnos asignados para el dia {dia_cancelar}\n"
                    )

            elif dia_cancelar == "2":
                if nombre_paciente_cancelar == martes_1:
                    martes_1 = ""
                    turnos_martes -= 1
                    print(
                        f"Se ha cancelado el turno del paciente {nombre_paciente_cancelar} del dia {dia_cancelar}\n"
                    )
                elif nombre_paciente_cancelar == martes_2:
                    martes_2 = ""
                    turnos_martes -= 1
                    print(
                        f"Se ha cancelado el turno del paciente {nombre_paciente_cancelar} del dia {dia_cancelar}\n"
                    )
                elif nombre_paciente_cancelar == martes_3:
                    martes_3 = ""
                    turnos_martes -= 1
                    print(
                        f"Se ha cancelado el turno del paciente {nombre_paciente_cancelar} del dia {dia_cancelar}\n"
                    )
                else:
                    print(
                        f"El paciente {nombre_paciente_cancelar} no tiene turnos asignados para el dia {dia_cancelar}\n"
                    )

        case "3":
            dia_comprobar = input(
                "Ingrese el numero para elegir dia a comprobar: 1-Lunes 2-Martes: "
            )
            while not (dia_comprobar == "1" or dia_comprobar == "2"):
                print("Ingrese un dia correcto. Elija 1 para lunes o 2 para martes.")
                dia_comprobar = input(
                    "Ingrese el numero para elegir dia: 1-Lunes 2-Martes: "
                )
            if dia_comprobar == "1":
                print(f"Turnos para el dia Lunes: \n")
                if lunes_1 == "":
                    print(f"Turno 1 : Libre")
                elif len(lunes_1) != 0:
                    print(f"Turno 1: asignado a {lunes_1}")
                if lunes_2 == "":
                    print(f"Turno 2 : Libre")
                elif len(lunes_2) != 0:
                    print(f"Turno 2: asignado a {lunes_2}")
                if lunes_3 == "":
                    print(f"Turno 3 : Libre")
                elif len(lunes_3) != 0:
                    print(f"Turno 3: asignado a {lunes_3}")
                if lunes_4 == "":
                    print(f"Turno 4 : Libre\n")
                elif len(lunes_4) != 0:
                    print(f"Turno 4: asignado a {lunes_4}\n")
            elif dia_comprobar == "2":
                print(f"Turnos para el dia Martes: \n")
                if martes_1 == "":
                    print(f"Turno 1 : Libre")
                elif len(martes_1) != 0:
                    print(f"Turno 1: asignado a {martes_1}")
                if martes_2 == "":
                    print(f"Turno 2 : Libre")
                elif len(martes_2) != 0:
                    print(f"Turno 2: asignado a {martes_2}")
                if martes_3 == "":
                    print(f"Turno 3 : Libre\n")
                elif len(martes_3) != 0:
                    print(f"Turno 3: asignado a {martes_3}\n")

        case "4":
            print("Turnos del dia Lunes: \n")
            if lunes_1 == "":
                print(f"Turno 1 : Libre")
            elif len(lunes_1) != 0:
                print(f"Turno 1: asignado a {lunes_1}")
            if lunes_2 == "":
                print(f"Turno 2 : Libre")
            elif len(lunes_2) != 0:
                print(f"Turno 2: asignado a {lunes_2}")
            if lunes_3 == "":
                print(f"Turno 3 : Libre")
            elif len(lunes_1) != 0:
                print(f"Turno 3: asignado a {lunes_3}")
            if lunes_4 == "":
                print(f"Turno 4 : Libre\n")
            elif len(lunes_4) != 0:
                print(f"Turno 4: asignado a {lunes_4}\n")
            print("Turnos del dia Martes: \n")
            if martes_1 == "":
                print(f"Turno 1 : Libre")
            elif len(martes_1) != 0:
                print(f"Turno 1: asignado a {martes_1}")
            if martes_2 == "":
                print(f"Turno 2 : Libre")
            elif len(martes_2) != 0:
                print(f"Turno 2: asignado a {martes_2}")
            if martes_3 == "":
                print(f"Turno 3 : Libre\n")
            elif len(martes_1) != 0:
                print(f"Turno 3: asignado a {martes_3}\n")
            if turnos_lunes > turnos_martes:
                print(f"El dia con mas turnos es Lunes, con {turnos_lunes} turnos. \n")
            elif turnos_lunes < turnos_martes:
                print(
                    f"El dia con mas turnos es Martes, con {turnos_martes} turnos. \n"
                )
            else:
                print("Los dias Lunes y Martes tienen la misma cantidad de turnos \n")

        case "5":
            break

        case _:
            if not menu.isdigit():
                print(
                    "No ha ingresado un numero. Ingrese una opcion valida con un numero entre 1 y 5."
                )
            else:
                print("Opcion fuera de rango. Ingrese una opcion entre 1 y 5.")


###### Ejercicio 4 -- "Escape Room: La Boveda" ######


energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
anti_spam = 0


agente = input("Introduzca su nombre de agente: ").strip().replace(" ", "")

while not agente.isalpha():
    print("Nombre incorrecto. Introduzca solamente letras para su nombre de agente.")
    agente = input("Introduzca su nombre de agente: ").strip().replace(" ", "")
print("Bienvenido a Escape Room: La Boveda. \n")
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print(
        f"Energia: {energia}\nTiempo: {tiempo}\nCerraduras abiertas: {cerraduras_abiertas}\nAlarma: {alarma}"
    )
    print("¿Que desea hacer a continuacion? \n")
    menu = input("1. Forzar cerradura \n2. Hackear panel \n3. Descansar \n")
    while not menu.isdigit():
        print("No has ingresado una opcion correcta. Ingresa un numero ente 1- 3")
        menu = input("1. Forzar cerradura \n2. Hackear panel \n3. Descansar \n")
    match menu:
        case "1":
            energia -= 20
            tiempo -= 2
            anti_spam += 1
            if anti_spam == 3:
                alarma = True
            elif energia < 40:
                print("¡Riesgo de alarma!")
                opcion_alarma = input(
                    "Ingresa un numero del 1 al 3 para intentar desactivarla: "
                )
                while not opcion_alarma.isdigit() or not (
                    opcion_alarma == "1" or opcion_alarma == "2" or opcion_alarma == "3"
                ):
                    print(
                        "No has ingresado una opcion correcta. Ingresa un numero ente 1- 3"
                    )
                    opcion_alarma = input(
                        "Ingresa un numero del 1 al 3 para intentar desactivarla: "
                    )
                if opcion_alarma == "3":
                    alarma = True
                else:
                    cerraduras_abiertas += 1
            else:
                cerraduras_abiertas += 1
        case "2":
            energia -= 10
            tiempo -= 3
            anti_spam = 0
            for i in range(4):
                codigo_parcial += "A"
                print(f"Codigo parcial: {codigo_parcial}")
            if len(codigo_parcial) >= 8:
                if cerraduras_abiertas < 3:
                    cerraduras_abiertas += 1
                    codigo_parcial = ""
        case "3":
            anti_spam = 0
            if alarma == True:
                energia += 5
            else:
                energia += 15
            if energia > 100:
                energia = 100
            tiempo -= 1
        case _:
            print(
                "No has ingresado un numero correcto de opcion. Ingresa un numero entre 1- 3."
            )
    if cerraduras_abiertas == 3:
        print("Victoria")
        break
    elif energia <= 0 or tiempo <= 0:
        print("Derrota")
        break
    elif alarma == True and tiempo <= 3:
        print("Derrota por bloqueo de alarma")
        break


###### Ejercicio 4 -- "Escape Room: La Arena del Gladiador" ######

import time


while True:
    nombre = (
        input('Bienvenido a "La arena del Gladiador". Ingresa nombre del jugador: ')
        .strip()
        .upper()
    )
    if nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras")

# Inicializacion de estadisticas

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
daño_base_atq_pes = 15
daño_base_enemigo = 12
Turno_gladiador = True

print("=== INICIO DEL COMBATE ===")
while vida_gladiador > 0 and vida_enemigo > 0:
    if Turno_gladiador == True:
        print(
            f"{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}"
        )
        mov_valido = False
        while not mov_valido:
            accion = input(
                f"Elige accion: \n 1. Ataque pesado\n 2. Rafaga Veloz\n 3. Curar \n"
            )
            if accion.isdigit() and (accion == "1" or accion == "2" or accion == "3"):
                mov_valido = True
            else:
                print("Error: Ingrese un número válido")

        match accion:
            case "1":
                if vida_enemigo < 20:
                    daño_final = daño_base_atq_pes * 1.5
                else:
                    daño_final = daño_base_atq_pes
                vida_enemigo -= int(daño_final)

                print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")
            case "2":
                print(">> ¡Inicias una ráfaga de golpes!")
                for i in range(3):
                    vida_enemigo -= 5
                    print(" > Golpe conectado por 5 de daño")
            case "3":
                if pociones > 0:
                    vida_gladiador += 30
                    pociones -= 1
                    print("Recuperas 30 puntos de vida")
                else:
                    print("¡No quedan pociones!")
        time.sleep(1)
        Turno_gladiador = False
    else:
        vida_gladiador -= 12
        print(f"¡El enemigo te atacó por {daño_base_enemigo} puntos de daño!")
        time.sleep(1)
        Turno_gladiador = True
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
elif vida_gladiador <= 0:
    print("DERROTA. Has caído en combate.")
