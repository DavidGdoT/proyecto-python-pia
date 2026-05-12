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
        (2) Elegir otras monedas
        (3) Agregar nuevas monedas
        (4) Ver monedas eleguidas
        (5) Ver conversiones
        (6) Imprimir gráfica
        (7) Terminar
        ------------------------------------
        """))
        if opcion_01 == "1":
            monedas, datos = con.conseguir_datos()   
        elif opcion_01 == "2":
            lista_mon.clear()
            lista_mon = con.monedas_elegidas(monedas)   
        elif opcion_01 == "3":
            lista_mon = con.monedas_elegidas(monedas)
        elif opcion_01 == "4":
            print(lista_mon)
        elif opcion_01 == "5":
            con.imprimir_conversiones(monedas, datos)                
        elif opcion_01 == "6":
            mon_values = con.datos_conversiones(monedas, datos)
            while True:
                opcion_02 = str(input("""
                ------------------------------------
                (1) Comparar monedas elegidas
                (2) Comparar todas las monedas
                (3) Retroceder
                ------------------------------------
                """))
                if opcion_02 == "1":
                    mon_values.clear()
                    mon_values = con.datos_conversiones(monedas, datos)
                    con.grafica_mon(lista_mon, mon_values)
                elif opcion_02 == "2":
                    con.grafica_mon(monedas.keys(), monedas.values())
                elif opcion_02 == "3":
                    break
                else:
                    print("Opción no valida")             
        elif opcion_01 == "7":
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
