import base_mon
import matplotlib.pyplot as plt

datos = base_mon.base_alterada()
monedas = datos.get('conversion_rates')
lista_mon = []
mon_values = []

def monedas_elegidas():
    while True:
        mon = str(input('nombre de abreviado de la moneda (escribe "stop" para terminar) ')).upper()
        if mon == 'STOP':
            if len(lista_mon) == 0:
               print('agregar monedas')
            else:
               break
        elif mon in lista_mon:
            print('moneda ya agregada')
        elif mon not in lista_mon:
            if mon in monedas.keys():
                lista_mon.append(mon)
            else:
                print("moneda no existente")
    print(lista_mon)
    return lista_mon

def imprimir_conversiones():
    for nombre in lista_mon:
        mon_values.append(monedas.get(nombre))
        print('1', datos.get('base_code'),'=', monedas.get(nombre), nombre)
    return mon_values
    
#para texto más extenso crear una bibloteca con las moendas elegidas
plt.plot(lista_mon, mon_values, marker="p")
plt.savefig("con.png")
