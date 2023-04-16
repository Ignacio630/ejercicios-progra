# 1)

# numeros = {1,2,3,4,5,6}
# numeroMayor = 0

# for i in numeros:
#     if i > numeroMayor:
#         numeroMayor = i

# print("El numero mayor es: {0}".format(numeroMayor))

# 2)

# palabras = ["Hola", "Adios", "Buenos", "Dias","Tardes","Noches", "felicidades"]
# print(type(palabras))
# palabraLarga = ""
# for palabra in palabras:
#     if len(palabra) > len(palabraLarga):
#         palabraLarga = palabra

# print("La palabra mas larga es: {0}".format(palabraLarga))


# Dado un número entero n, imprimir la secuencia de números pares menores o iguales a n.

# numeroEntero = int(input("Ingrese un numero entero: "))

# itera el rango de entre 0 y el numero ingresado + 1 para que incluya el numero ingresado si es par
# for i in range(0,numeroEntero+1):
#     if i % 2 == 0:
#         print(i)


#4) Dado un número entero n, imprimir la suma de los números impares menores o iguales a n.

# numeroEntero = int(input("Ingrese un numero entero: "))
# flag = 0
# for i in range(0,numeroEntero+1):
#     if i % 2 != 0:
#         flag += i

# print(flag)

#5) Dada una lista de números, imprimir el número más pequeño de la lista.

# lista = [1,2,3,4,5,6,7,8,9,10]
# menor = 0
# for i in lista:
#     if menor == 0 or i < menor:
#         menor = i

# print(menor)

# 6) Dada una lista de palabras, imprimir la cantidad total de vocales en la lista.

lista = ["Hola", "Adios", "Buenos", "Dias","Tardes","Noches", "felicidades"]
vocales = ("a","e","i","o","u")
totalVocales = 0
for palabra in lista:
    for letra in palabra:
        if letra in vocales:
            totalVocales += 1

print(totalVocales)