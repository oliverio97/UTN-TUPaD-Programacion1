# INICIALIZACION DE LISTAS PARALELAS
herramientas = []
existencias = []

while True:  # BUCLE PRINCIPAL CON OPCIONES
    print()
    print(
        "Bienvenido al sistema de gestion de ferretería. Ingresa una opcion del menu seleccionando su numero entre 1-8.\n"
    )
    menu = input(
        "1. Carga inicial de herramientas\n2. Carga de existencias\n3. Visualizacion de inventario\n4. Consulta de Stock (existencias)\n5. Reporte de agotados\n6. Alta de nuevo producto\n7. Actualizacion de stock (Venta/Ingreso)\n8.Salir \n"
    ).strip()
    print()
    while not menu.isdigit() or not (int(menu) > 0 and int(menu) < 9):
        print("No has ingresado una opcion valida. Ingresa un numero entre 1 y 8.\n")
        menu = input(
            "1. Carga inicial de herramientas\n2. Carga de existencias\n3. Visualizacion de inventario\n4. Consulta de Stock (existencias)\n5. Reporte de agotados\n6. Alta de nuevo producto\n7. Actualizacion de stock (Venta/Ingreso)\n8.Salir \n"
        ).strip()
        print()
    match menu:

        case "1":  # CARGA INICIAL DE HERRAMIENTAS
            herramientas = []
            existencias = []
            cant_herramientas = input(
                "Ingresa la cantidad de herramientas a cargar: "
            ).strip()
            while not cant_herramientas.isdigit() or not int(cant_herramientas) > 0:
                print(
                    "No has ingresado un numero valido. Ingresa un numero mayor que cero para la cantidad de herramientas a cargar.\n"
                )
                cant_herramientas = input(
                    "Ingresa la cantidad de herramientas a cargar: "
                ).strip()
            for i in range(int(cant_herramientas)):
                herramienta = (
                    input(f"Ingresa la herramienta n° {i+1}: ").strip().lower()
                )
                while (
                    len(herramienta) == 0
                    or herramienta in herramientas
                    or not herramienta.replace(" ", "").isalpha()
                ):
                    print(
                        "No has ingresado una herramienta valida. Ingresa una herramienta que no haya sido ingresada previamente. \n"
                    )
                    herramienta = (
                        input(f"Ingresa la herramienta n° {i+1}: ").strip().lower()
                    )
                herramientas.append(herramienta)
            print(
                "\nCarga inicial de herramientas realizada con exito. Recorda ingresar a la opcion 2 a continuacion para realizar la carga de existencias.\n"
            )

        case "2":  # CARGA INICIAL DE EXISTENCIAS
            existencias = []
            if len(herramientas) == 0:
                print(
                    "No has ingresado ninguna herramienta. Recuerda realizar la carga de herramientas mediante la opcion 1 antes de agregar existencias\n"
                )
            else:
                for i in herramientas:
                    existencia = input(
                        f"Ingresa las unidades en stock para la herramienta {i}: "
                    ).strip()
                    while not existencia.isdigit() or not int(existencia) >= 0:
                        print(
                            "No has ingresado una opcion correcta. Ingresa solamente un numero positivo para el stock, o el numero cero en caso de no contar con existencias de la herramienta. \n"
                        )
                        existencia = input(
                            f"Ingresa las unidades en stock para la herramienta {i}: "
                        ).strip()
                    existencias.append(int(existencia))
                print("\nCarga de existencias realizada con exito. \n")

        case "3":  # VISUALIZACION DE INVENTARIO CON HERRAMIENTAS Y STOCK
            if len(herramientas) == 0:
                print(
                    "No has ingresado ninguna herramienta. Recuerda realizar la carga de herramientas mediante la opcion 1 antes de verificar stock\n"
                )
            elif len(existencias) == 0:
                print(
                    "No has ingresado existencias para tus herramientas. Recuerda realizar la carga de existencias mediante la opcion 2 antes de verificar stock\n"
                )
            else:
                print("Inventario con unidades en Stock: \n")
                for i in range(len(herramientas)):
                    print(f"Herramienta: {herramientas[i]} - Stock: {existencias[i]}")
                print()

        case "4":  # BUSQUEDA POR HERRAMIENTA PARA CONSULTAR STOCK
            if len(herramientas) == 0:
                print(
                    "No has ingresado ninguna herramienta. Recuerda realizar la carga de herramientas mediante la opcion 1 antes de verificar existencias\n"
                )
            elif len(existencias) == 0:
                print(
                    "No has ingresado existencias para tus herramientas. Recuerda realizar la carga de existencias mediante la opcion 2 antes de verificar existencias\n"
                )
            else:
                consulta_stock = (
                    input(
                        "Ingresa el nombre de la herramienta para consultar las existencias de la misma: "
                    )
                    .strip()
                    .lower()
                )
                print()
                while not consulta_stock.replace(" ", "").isalpha():
                    print(
                        "No has ingresado una opcion valida. Recuerda ingresar solo palabras para buscar herramientas. \n"
                    )
                    consulta_stock = (
                        input(
                            "Ingresa el nombre de la herramienta para consultar las existencias de la misma: "
                        )
                        .strip()
                        .lower()
                    )
                encontrado = False
                for i in range(len(herramientas)):
                    if consulta_stock == herramientas[i]:
                        print(
                            f"La herramienta {consulta_stock} posee un stock de {existencias[i]} unidades. \n"
                        )
                        encontrado = True
                if encontrado == False:
                    print(
                        f"No se encontro la herramienta {consulta_stock} en el inventario. \n"
                    )

        case "5":  # REPORTE DE HERRAMIENTAS AGOTADAS
            if len(herramientas) == 0:
                print(
                    "No has ingresado ninguna herramienta. Recuerda realizar la carga de herramientas mediante la opcion 1 antes de verificar herramientas agotadas\n"
                )
            elif len(existencias) == 0:
                print(
                    "No has ingresado existencias para tus herramientas. Recuerda realizar la carga de existencias mediante la opcion 2 antes de verificar herramientas agotadas\n"
                )
            else:
                hay_agotadas = False
                print("Reporte de herramientas sin existencias: \n")
                for i in range(len(herramientas)):
                    if existencias[i] == 0:
                        hay_agotadas = True
                        print(
                            f"La herramienta {herramientas[i]} se encuentra agotada. "
                        )
                if hay_agotadas == False:
                    print("No se encontraron herramientas sin existencias.")
                print()

        case "6":  # ALTA DE NUEVA HERRAMIENTA Y STOCK CORRESPONDIENTE
            if len(herramientas) == 0:
                print(
                    "No has ingresado ninguna herramienta. Recuerda realizar la carga de herramientas mediante la opcion 1 antes de realizar altas de producto\n"
                )
            elif len(existencias) == 0:
                print(
                    "No has ingresado existencias para tus herramientas. Recuerda realizar la carga de existencias mediante la opcion 2 antes de realizar altas de producto\n"
                )
            else:
                print("Alta de producto: \n")
                nueva_herramienta = (
                    input("Ingresa la nueva herramienta para agregar al inventario: ")
                    .strip()
                    .lower()
                )
                if len(nueva_herramienta) == 0:
                    print(
                        "No ingresaste ninguna herramienta. Ingresa nuevamente a la opcion 6 si deseas agregar un nuevo producto. "
                    )
                elif nueva_herramienta in herramientas:
                    print(
                        "La herramienta ingresada ya se encuentra actualmente en inventario. Si deseas actualizar el stock ingresa a la opcion 7. \n"
                    )
                else:
                    stock_nueva_herramienta = input(
                        f"Ingresa la cantidad de unidades en stock para la herramienta {nueva_herramienta}: "
                    )
                    if (
                        not stock_nueva_herramienta.isdigit()
                        or not int(stock_nueva_herramienta) >= 0
                    ):
                        print(
                            "No has ingresado una opcion valida para las existencias. Ingresa nuevamente a la opcion 6 y repita el proceso. \n"
                        )
                    else:
                        print(
                            f"Se ha agregado la herramienta {nueva_herramienta} con exito.\n"
                        )
                        print(
                            f"El stock actualizado de {nueva_herramienta} es de {stock_nueva_herramienta} unidad/es."
                        )
                        herramientas.append(nueva_herramienta)
                        existencias.append(int(stock_nueva_herramienta))

        case (
            "7"
        ):  # ACTUALIZACION DE STOCK. 3 OPCIONES: VENTA E INGRESO Y MENU PRINCIPAL.
            if len(herramientas) == 0:
                print(
                    "No has ingresado ninguna herramienta. Recuerda realizar la carga de herramientas mediante la opcion 1 antes de actualizar stock\n"
                )
            elif len(existencias) == 0:
                print(
                    "No has ingresado existencias para tus herramientas. Recuerda realizar la carga de existencias mediante la opcion 2 antes de actualizar stock\n"
                )
            else:
                print(
                    "Actualizacion de Stock mediante venta o ingreso de existencias. Elige la operacion que desea realizar: \n"
                )
                print("1. Venta\n2. Ingreso\n3. Menu principal")
                menu_act_stock = input().strip()
                print()
                while not menu_act_stock.isdigit() or not (
                    int(menu_act_stock) > 0 and int(menu_act_stock) < 4
                ):
                    print(
                        "No has ingresado una opcion valida. Ingresa un numero entre 1-3 para continuar\n"
                    )
                    print("1. Venta\n2. Ingreso\n3. Menu principal")
                    menu_act_stock = input().strip()
                    print()

                match menu_act_stock:  # MENU DENTRO DE LA OPCION 7 CON OPCIONES DE VENTA, INGRESO Y VOLVER AL MENU PRINCIPAL

                    case (
                        "1"
                    ):  # ELEGIR HERRAMIENTA PARA REALIZAR VENTA Y DISMINUIR STOCK SI ES POSIBLE
                        print(
                            "Elige la herramienta sobre la cual se realizaron ventas: "
                        )
                        herramienta_venta = input().strip().lower()
                        if herramienta_venta not in herramientas:
                            print(
                                "La herramienta ingresada no se encuentra en el inventario. \n"
                            )
                        else:
                            for i in range(len(herramientas)):
                                if herramientas[i] == herramienta_venta:
                                    cantidad_venta = input(
                                        f"Ingresa la cantidad de unidades de la herramienta {herramienta_venta} vendidas: "
                                    ).strip()
                                    while (
                                        not cantidad_venta.isdigit()
                                        or not int(cantidad_venta) > 0
                                    ):
                                        print(
                                            "No has ingresado una opcion valida. Ingresa un numero mayor que cero para registrar ventas. \n"
                                        )
                                        cantidad_venta = input(
                                            f"Ingresa la cantidad de unidades de la herramienta {herramienta_venta} vendidas: "
                                        ).strip()
                                    print()
                                    if int(cantidad_venta) > int(existencias[i]):
                                        print(
                                            f"No hay suficientes existencias de {herramienta_venta} para realizar la venta. \n"
                                        )
                                        break
                                    else:
                                        existencias[i] = int(existencias[i]) - int(
                                            cantidad_venta
                                        )
                                        print(
                                            f"Se realizo correctamente la venta de  {cantidad_venta} unidades de {herramienta_venta}.\n"
                                        )
                                    print(
                                        f"El stock actualizado de {herramienta_venta} es de {existencias[i]} unidad/es\n"
                                    )

                    case "2":  # REALIZAR INGRESOS DE HERRAMIENTAS Y ACTUALIZAR STOCK
                        print(
                            "Elige la herramienta sobre la cual se realizaron ingresos de existencias: "
                        )
                        herramienta_ingreso = input().strip().lower()
                        if herramienta_ingreso not in herramientas:
                            print(
                                "La herramienta ingresada no se encuentra en el inventario. \n"
                            )
                        else:
                            for i in range(len(herramientas)):
                                if herramientas[i] == herramienta_ingreso:
                                    cantidad_ingreso = input(
                                        f"Ingresa la cantidad de unidades de {herramienta_ingreso} para agregar al stock: "
                                    ).strip()
                                    while (
                                        not cantidad_ingreso.isdigit()
                                        or not int(cantidad_ingreso) > 0
                                    ):
                                        print(
                                            "No has ingresado una opcion valida. Ingresa un numero mayor que cero para registrar ingresos. \n"
                                        )
                                        cantidad_ingreso = input(
                                            f"Ingresa la cantidad de unidades de {herramienta_ingreso} para agregar al stock: "
                                        ).strip()
                                    existencias[i] = int(existencias[i]) + int(
                                        cantidad_ingreso
                                    )
                                    print(
                                        f"Se agregaron {cantidad_ingreso} unidades de {herramienta_ingreso} correctamente.\n"
                                    )
                                    print(
                                        f"El stock actualizado de {herramienta_ingreso} es de {existencias[i]} unidad/es\n"
                                    )

                    case "3":  # VOLVER AL MENU PRINCIPAL
                        continue

        case "8":  # ESTA OPCION INTERRUMPE EL BUCLE Y FINALIZA EL PROGRAMA
            break
