import api_datos
import requests
import json

def nombres_monedas():
    nombres = (api_datos.obtener_datos().get('conversion_rates')).keys()
    return nombres

def verificador():
    while True:
        #imprimir una lista con los valores que se puedan elegir
        b = str(input('eligue una base: ')).upper()
        if b not in nombres_monedas():
            print('base no valida')
        else:
            print('base a utilizar en las conversiones: '+str(b))
            break
    return b

def base_alterada():
    b = verificador()
    url = 'https://v6.exchangerate-api.com/v6/b6d737f0e4b316d91afd4e28/latest/'+str(b)
    reponse = requests.get(url)
    data = json.loads(reponse.text)
    return data
