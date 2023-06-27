# import os

# os.system("cls")

# # Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.

# texto = input("Ingrese un texto: ")

# def texto_a_mayuscula(texto):
#     return texto.upper()

# print(texto_a_mayuscula(texto))

# # Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.

# texto = input("Ingrese un texto: ")

# def texto_a_minuscula(texto):
#     return texto.lower()

# print(texto_a_minuscula(texto))

# # Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados 

# texto_1 = input("Ingrese el primer texto: ")
# texto_2 = input("Ingrese el segundo texto: ")

# def unir_dos_strings(texto_1,texto_2):
#     texto_3 = texto_1 + "," + texto_2
#     return texto_3

# texto_unido = unir_dos_strings(texto_1,texto_2)
# print(texto_unido)

# # Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.

# texto = input("Ingrese un texto: ")

# def nro_de_caracteres(string):
#     return len(string)

# caracteres = nro_de_caracteres(texto)

# print("El numero de caracteres del texto ingresado es: ", caracteres)

# # Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.


# texto = input("Ingrese un texto: ")
# caracter = input("Ingrese un caracter: ")

# def nro_de_ocurrencias(string, caracter):
#     return string.count(caracter)

# ocurrencias = nro_de_ocurrencias(texto,caracter)

# print("El numero de ocurrencias de {0} que aparece en {1} es {2}".format(caracter,texto,ocurrencias))

# # Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.

# ##### Hacer


# # Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados

# texto = input("Ingrese un texto: ")

# def eliminar_espacios(string):
#     texto_modificado = string.split(" ")

#     texto_sin_espacio = "".join(texto_modificado)
    
#     return texto_sin_espacio
    
# texto_sin_espacio = eliminar_espacios(texto)

# print(texto_sin_espacio)

# # Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula

# texto_1 = input("Ingrese texto uno: ")
# texto_2 = input("Ingrese texto dos: ")

# def diccionario_persona(nombre,apellido):
#     aux_nombre = nombre.strip()
#     aux_apellido = apellido.strip()
#     aux_dict = {"Nombre":aux_nombre.capitalize(), "Apellido": aux_apellido.capitalize()}
    
#     return aux_dict
 
# diccionario_modificado = diccionario_persona(texto_1,texto_2)
    
# print("Nombre: {0}\nApellido: {1}".format(diccionario_modificado["Nombre"],diccionario_modificado["Apellido"]))


# # Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".

# lista_personas= ["Juan", "María", "Pedro"]

# def separacion_por_linea(lista):
#     aux_string = '\n'.join(lista)
#     return aux_string

# personas_separadas_por_linea = separacion_por_linea(lista_personas)

# print(personas_separadas_por_linea)

# # Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".

# nombre = input("Ingrese su nombre: ")
# apellido = input("Ingrese su apellido: ")

# def crear_mail(nombre,apellido):
#     aux_nombre = nombre.strip()
#     aux_nombre = aux_nombre[0].lower()
#     aux_apellido = apellido.strip()
#     aux_apellido = aux_apellido.lower() 
#     email = "{0}_{1}@utn-fra.com.ar".format(aux_nombre,aux_apellido)
#     return email;

# print(crear_mail(nombre,apellido))
    
# Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas y "y" antes de la última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"

lista = ["manzanas", "naranjas", "bananas"]

def palabas_unidas(lista_palabras):

    if len(lista_palabras) == 0:
        return " "
    if len(lista_palabras) == 1:
        return lista_palabras[0]
    else:
        aux_string = ", ".join(lista_palabras[:-1])
        return aux_string + " y " + lista_palabras[-1]

texto_lista = palabas_unidas(lista)

print(texto_lista)

# Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 

# Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".

# Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..

# Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo, por ejemplo: "H0l4, m4nd0!" -> "Hl, mnd.

# Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.

# Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".


# Escribir una función que tome una cadena de caracteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"


# Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.


# Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma, por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".

# Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.
