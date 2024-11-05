def insercion(lista):
    n = len(lista)
    for i in range(1, n): 
        elemento_a_insertar = lista[i] 
        j = i - 1
        while j >= 0 and lista[j] > elemento_a_insertar:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elemento_a_insertar
        print(f"Iteración {i}: {lista}")
tamaño = int(input("Captura el tamaño del arreglo: "))
numeros = []
for i in range(tamaño):
    num = int(input(f"Captura el elemento {i + 1}: "))
    numeros.append(num)
print("Lista original:", numeros)
insercion(numeros)
print("Lista ordenada:", numeros)
