def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
        print(f"Iteración {i + 1}: {lista}")
tamaño = int(input("Captura el tamaño del arreglo: "))
numeros = []
for i in range(tamaño):
    num = int(input(f"Captura el elemento {i + 1}: "))
    numeros.append(num)
print("Lista original:", numeros)
burbuja(numeros)
print("Lista ordenada:", numeros)
