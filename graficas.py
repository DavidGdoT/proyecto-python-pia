import conversiones as con
import matplotlib.pyplot as plt

def grafica_conversiones(lista_mon, mon_values):
    plt.plot(lista_mon, mon_values, marker="p")
    plt.title("Comparación de monedas")
    plt.xlabel("Monedas")
    plt.ylabel("Valores")
    plt.savefig("grafica_conversiones.png")
    plt.show()

def grafica_mayores(datos):
    while True:
        n = int(input("Cantidad de monedas a tomar (maximo 50): "))
        if n <= 0:
            print('Valor no valido')
        elif n >= 51:
            print('Limite sobrepasado')
        else:
            break
    ratio = datos["conversion_rates"]
    mayores = sorted(ratio.items(), key=lambda x: x[1], reverse=True)
    monedas_mayores = []
    valores_mayores = []
    for moneda, valor in mayores[:n]:
        monedas_mayores.append(moneda)
        valores_mayores.append(valor)
    plt.bar(monedas_mayores, valores_mayores)
    plt.title("Monedas con mayor valor")
    plt.xlabel("Monedas")
    plt.ylabel("Valores")
    plt.savefig("gráfica_mayores.png")
    plt.show()

def grafica_menores(datos):
    while True:
        n = int(input("Cantidad de monedas a tomar (maximo 50): "))
        if n <= 0:
            print('Valor no valido')
        elif n >= 51:
            print('Limite sobrepasado')
        else:
            break
    ratio = datos["conversion_rates"]
    menores = sorted(ratio.items(), key=lambda x: x[1])
    monedas_menores = []
    valores_menores = []
    for moneda, valor in menores[:n]:
        monedas_menores.append(moneda)
        valores_menores.append(valor)
    plt.bar(monedas_menores, valores_menores)
    plt.title("Monedas con menor valor")
    plt.xlabel("Monedas")
    plt.ylabel("Valores")
    plt.savefig("grafica_menores.png")
    plt.show()
