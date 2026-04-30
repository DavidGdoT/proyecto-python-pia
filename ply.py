import matplotlib.pyplot as plt
import requests
import json

n = int(input("Cantidad de items:"))
items = list(range(1, n, 1))
costo = []
print(items)
for it in items:
    url = 'https://pokeapi.co/api/v2/item/'+str(it)
    reponse = requests.get(url)
    data = json.loads(reponse.text)
    costo.append(data["cost"])

plt.plot(items, costo, marker = 'p')
plt.show()

    
    


