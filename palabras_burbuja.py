def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print(f"Intercambio en Iteración {i + 1}, paso {j + 1}: {lista}")           
        print(f"Estado de la lista después de la iteración {i + 1}: {lista}")
tamaño = int(input("Captura el número de palabras a ordenar: "))
palabras = []
for i in range(tamaño):
    palabra = input(f"Captura la palabra {i + 1}: ")
    palabras.append(palabra)
print("Lista original:", palabras)
burbuja(palabras)
print("Lista ordenada:", palabras)

