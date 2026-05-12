import base_mon
import matplotlib.pyplot as plt

def conseguir_datos():
    datos = base_mon.base_alterada()
    monedas = datos.get('conversion_rates')
    return monedas, datos

lista_mon = []
mon_values = []

def monedas_elegidas(monedas):
    while True:
        mon = str(input('Nombre de abreviado de la moneda (escribe "Stop" para terminar) ')).upper()
        if mon == 'STOP':
            if len(lista_mon) == 0:
               print('Agregar monedas')
            else:
               break
        elif mon in lista_mon:
            print('Moneda ya agregada')
        elif mon not in lista_mon:
            if mon in monedas.keys():
                lista_mon.append(mon)
            else:
                print("Moneda no existente")
    return lista_mon

def datos_conversiones(monedas, datos):
    for nombre in lista_mon:
        mon_values.append(monedas.get(nombre))
    return mon_values

def imprimir_conversiones(monedas, datos):
    for nombre in lista_mon:
        print('1', datos.get('base_code'),'=', monedas.get(nombre), nombre)

def grafica_mon(lista_mon, mon_values):
    plt.plot(lista_mon, mon_values, marker="p")
    plt.savefig("con.png")
