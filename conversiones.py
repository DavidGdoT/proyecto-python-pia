from api_datos import obtener_datos

datos = obtener_datos()
monedas = datos.get('conversion_rates')
lista_mon = []

while True:
    mon = str(input('nombre de abreviado de la moneda (escribe "stop" para terminar) '))
    if mon in monedas.keys():
        lista_mon.append(mon)
    elif mon == 'stop':
        break
    else:
        print('moneda no existente')

for _ in lista_mon:
    print('1 USD =', monedas.get(_), _)
