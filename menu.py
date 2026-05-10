import conversiones as con

def menu():
    i = []
    while True:
        opcion = str(input("""
        -----------¡Bienvenido!------------
        Eligue la una opción
        (1) Elegir base
        (2) Elegir Monedas
        (3) Ver monedas elegidas
        (4) Ver conversiones
        (5) Imprimir grafica/Finalizar
        (6) Salir
        ------------------------------------
        """))

        if opcion == '1':
            monedas, datos = con.conseguir_datos()
            if 1 not in i:
                i.append(1)

        elif opcion == '2':
            if 1 not in i:
                print('eligue una base primero')
            else:
                i.append(2)
                lista_mon = con.monedas_elegidas(monedas)

        elif opcion == '3':
            if 1 not in i:
                print('eligue una base primero')
            elif 1 in i and 2 not in i:
                print('no hay monedas elegidas')
            else:
                print(lista_mon)
            
        elif opcion == '4':
            if 1 not in i:
                print('eligue una base primero')
            elif 2 not in i:
                print('no hay monedas a convertir')
            else:
                mon_values = con.imprimir_conversiones(monedas, datos)

        elif opcion == '5':
            if 1 not in i:
                print('eligue una base primero')
            elif 2 not in i:
                print('no hay monedas para graficar')
            else:
                con.grafica_mon(lista_mon, mon_values)
                print('¡Gracias por su preferencia!')
                break
        
        elif opcion == '6':
            print('¡Hasta pronto!')

            break

        else:
            print('opcion no valida')
