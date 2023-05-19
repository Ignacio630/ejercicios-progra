import os
os.system("cls")
# Escribir una función que reciba un string y devuelva el mismo string todo en mayúsculas.

# def a_mayuscula(texto:str)-> str:
#     return texto.upper()

# texto = input("Texto: ")

# print(a_mayuscula(texto))

# Escribir una función que reciba un string y devuelva el mismo string todo en minúsculas.

# def a_minuscula(texto:str)-> str:
#     return texto.lower()

# texto = input("Texto: ")

# print(a_minuscula(texto))

# Escribir una función que tome dos strings y devuelva un nuevo string que contenga ambos strings concatenados, separados por un espacio.

# def concatenar(texto1:str, texto2:str)-> str:
#     return texto1 + " " + texto2
# texto1 = input("Texto 1: ")
# texto2 = input("Texto 2: ")
# print(concatenar(texto1, texto2))

# Escribir una función que tome un string y devuelva el número de caracteres que tiene el string.

# def contar_caracteres(texto:str)-> int:
#     return len(texto)
# texto = input("Texto: ")
# print(contar_caracteres(texto))

# Escribir una función que tome un string y un carácter y devuelva el número de veces que aparece ese carácter en el string.

# def contar_caracteres(texto:str, caracter:str)-> int:

#     return texto.count(caracter)

# texto = input("Texto: ")
# caracter = input("Caracter: ")
# print(contar_caracteres(texto, caracter))

 
# def contar_caracteres(texto:str, caracter:str)-> list:
# Escribir una función que tome un string y un carácter y devuelva una lista con todas las palabras en el string que contienen ese carácter.
#     lista = []
#     for palabra in texto.split():
#         if caracter in palabra:
#             lista.append(palabra)
#     return lista

# texto = input("Texto: ")
# caracter = input("Caracter: ")
# print(contar_caracteres(texto, caracter))


# def eliminar_espacios(texto:str)-> str:
# Escribir una función que tome un string y devuelva el mismo string con los espacios eliminados
#     return texto.replace(" ", "")

# texto = input("Texto: ")
# print(eliminar_espacios(texto))


# def nombre_apellido(nombre:str, apellido:str)-> dict:
# Escribir una función que reciba dos string (nombre y apellido) y devuelva un diccionario con el nombre y apellido, eliminando los espacios del comienzo y el final y colocando la primer letra en mayúscula
#     diccionario = {}
#     diccionario['nombre'] = nombre.replace(" ", "").capitalize()
#     diccionario['apellido'] = apellido.replace(" ", "").capitalize()
    
#     return diccionario

# print(nombre_apellido("juan","carLOS"))


# def listar_nombres(lista:list)-> str:
# Escribir una función que tome una lista de nombres y los una en una sola cadena separada por un salto de línea, por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".
    
#     aux_cadena = ""
#     for item in lista:
#         aux_cadena = aux_cadena + item.capitalize() + "\n"
#     return aux_cadena

# lista = ["pablo","marcos","PEDRo"]

# print(listar_nombres(lista))

# Escribir una función que tome un nombre y un apellido y devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".

# def generar_email(nombre:str, apellido:str)-> str:
#     return nombre[0].lower() + "."+ apellido.lower() + "@utn-fra.com.ar"

# print(generar_email("Ignacio","MEDICI"))


# Escribir una función que tome una lista de palabras y devuelva un string que contenga todas las palabras concatenadas con comas y "y" antes de la última palabra. Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], el string resultante debería ser "manzanas, naranjas y bananas"..

# def concatenar_palabras(lista:list)-> str:
#     aux_cadena = ""
#     for item in lista:
#         if item == lista[-1]:
#             aux_cadena = aux_cadena + "y " + item.capitalize()
#         else:
#             aux_cadena = aux_cadena + item.capitalize() + ", "
#     return aux_cadena

# lista = ["manzanas", "naranjas", "bananas","peras", "anana", "sandia"]

# print(concatenar_palabras(lista))

# Escribir una función que tome un número de tarjeta de crédito como input, verificar que todos los caracteres sean numéricos y devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, por ejemplo: "**** **** **** 1234". 


# def ocultar_numero(numeros:str)-> str:
#     retorno = ""
#     if numeros.isnumeric() or len(numeros) == 16:
#         retorno = "**** **** **** " + numeros[-4:]
#     else:
#         retorno = "Error, lo ingresado no son numeros o su longitud no es de  "
    
#     return retorno

# numero = input("Ingrese los numeros de su tarjeta: ")
# print(ocultar_numero(numero))

# Escribir una función que tome un correo electrónico y elimine cualquier carácter después del símbolo @, por ejemplo: "usuario@gmail.com" -> "usuario".

# def eliminar_mail(correo:str)-> str:
#     return correo.split("@")[0]

# print(eliminar_mail("i.medici@utn-fra.com"))

# Escribir una función que tome una URL y devuelva solo el nombre de dominio, por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..

# def eliminar_dominio(url:str)-> str:
#     return url.split(".")[1]

# resultado = eliminar_dominio("https://www.youtube.com/")

# print("El dominio de la url ingresada es: {0}".format(resultado))

# Escribir una función que tome una cadena de texto y devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo (sólo son válidos letras y espacios), por ejemplo: "H0l4, m4nd0!" -> "Hl mnd”

# def eliminar_simbolos_y_numeros(texto:str)-> str:
#     texto_formateado = ""
#     for caracter in texto:
#         if caracter.isalpha() or caracter.isspace():
#             texto_formateado += caracter
#     return texto_formateado
        
# resultado = eliminar_simbolos_y_numeros("Hol@ como 3st@s?!")

# print(resultado)

# Escribir una función que tome una cadena de texto y la convierta en un acrónimo, tomando la primera letra de cada palabra, por ejemplo: "Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.

# def acronimos_texto(texto:str)-> str:
#     texto_separado = texto.split(" ")
#     texto_retornado = ""
#     for text in texto_separado:
#         texto_retornado += text.capitalize()[0]
#     return texto_retornado

# texto_completo = "Universidad Tecnológica Nacional Facultad Regional Avellaneda"
# resultado = acronimos_texto(texto_completo)
    
# print("El acronimo de ""{0}"" es: {1}".format(texto_completo,resultado))

# Escribir una función que tome un número binario y lo convierta en una cadena de 8 bits, rellenando con ceros a la izquierda si es necesario, por ejemplo: "101" -> "00000101".

def rellenar_binario(nro_binario:str)-> str:
    ceros = "0"* (8 - len(nro_binario))
    return ceros + nro_binario
print(rellenar_binario("101"))
# Escribir una función que tome una cadena de car   acteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"


# Escribir una función que tome una cadena de caracteres y cuente la cantidad de dígitos que contiene, por ejemplo: "1234 Hola Mundo" -> contiene 4 dígitos.


# Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma, por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".


# Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.
