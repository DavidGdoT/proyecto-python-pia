import requests
import json

def obtener_datos():
    url = 'https://v6.exchangerate-api.com/v6/b6d737f0e4b316d91afd4e28/latest/USD'
    reponse = requests.get(url)
    data = json.loads(reponse.text)
    return data

if __name__ == "__main__":
    datos = obtener_datos()
    print(datos)
