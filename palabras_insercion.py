def insercion(lista):
    n = len(lista)
    for i in range(1, n):
        palabra_a_insertar = lista[i]
        j = i-1
        while j >= 0 and lista[j] > palabra_a_insertar:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = palabra_a_insertar
tamaño = int(input("Captura el número de palabras a ordenar: "))
palabras = []
for i in range(tamaño):
    palabra = input(f"Captura la palabra {i + 1}: ")
    palabras.append(palabra)

print("Lista original:", palabras)
insercion(palabras)  
print("Lista ordenada:", palabras)