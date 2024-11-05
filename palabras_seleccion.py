def seleccion(lista):
    n = len(lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
        print(f"Iteración {i + 1}: {lista}")

tamaño = int(input("Captura el tamaño del arreglo: "))
palabras = []
for i in range(tamaño):
    palabra = input(f"Captura la palabra {i + 1}: ")
    palabras.append(palabra)

print("Lista original:", palabras)
seleccion(palabras)
print("Lista ordenada:", palabras)
