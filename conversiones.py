from api_datos import obtener_datos
import matplotlib.pyplot as plt

datos = obtener_datos()
monedas = datos.get('conversion_rates')
lista_mon = []
mon_values = []

while True:
    mon = str(input('nombre de abreviado de la moneda (escribe "stop" para terminar) '))
    if mon == 'stop':
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
    
for nombre in lista_mon:
    mon_values.append(monedas.get(nombre))
    print('1 USD =', monedas.get(nombre), nombre)
    
#para texto más extenso crear una bibloteca con las moendas elegidas
plt.plot(lista_mon, mon_values, marker="p")
plt.savefig("con.png")
