import conversiones as con

def menu():
    print("------------¡Bienvenido!------------\nEsta aplicación calcula la conversión\nde todas las monedas del mundo.\n-----------------------------------")
    monedas,datos = con.conseguir_datos()
    print("-----------------------------------")
    menu_inicio(monedas, datos)

def menu_introducir_monedas(monedas, datos, lista_mon):
    while True:
        opcion_01 = str(input("""
        ------------------------------------
        (1) Cambiar de base
        (2) Ver monedas eleguidas
        (3) Ver conversiones
        (4) Imprimir gráfica
        (5) Salir
        ------------------------------------
        """))
        if opcion_01 == "1":
            monedas, datos = con.conseguir_datos()

        elif opcion_01 == "2":
            print(lista_mon)

        elif opcion_01 == "3":
            con.imprimir_conversiones(monedas, datos)
                
        elif opcion_01 == "4":
            mon_values = con.datos_conversiones(monedas, datos)
            con.grafica_mon(lista_mon, mon_values)
            print('¡Gracias por su preferencia!')
            return
    
        elif opcion_01 == "5":
            print("----------¡Hasta luego!----------")
            return

        else:
            print("Opción no valida")

def menu_inicio(monedas, datos):
    while True:
        opcion = str(input("""
        ------------------------------------
        Eligue una opción
        (1) Cambiar de base
        (2) Introducir Monedas
        (3) Salir
        ------------------------------------
        """))
        if opcion == '1':
            monedas, datos = con.conseguir_datos()

        elif opcion == '2':
            lista_mon = con.monedas_elegidas(monedas)
            menu_introducir_monedas(monedas, datos, lista_mon)
            break
        
        elif opcion == '3':
            print("----------¡Hasta luego!----------")
            return

        else:
            print("Opción no valida")
