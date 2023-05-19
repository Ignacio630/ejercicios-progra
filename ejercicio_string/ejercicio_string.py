import os
from funciones_utiles import *
os.system("cls")

#1
def a_mayuscula(texto:str)-> str:
    return texto.upper()

#2
def a_minuscula(texto:str)-> str:
    return texto.lower()

#3
def concatenar(texto1:str, texto2:str)-> str:
    return texto1 + " " + texto2

#4
def contar_caracteres(texto:str)-> int:
    return len(texto)

#5
def contar_caracteres_recurrentes(texto:str, caracter:str)-> int:

    return texto.count(caracter)

#6 
def palabras_contenidas(texto:str, caracter:str)-> list:
    lista = []
    for palabra in texto.split():
        if caracter in palabra:
            lista.append(palabra)
    return lista

#7
def eliminar_espacios(texto:str)-> str:
    return texto.replace(" ", "")

#8
def nombre_apellido(nombre:str, apellido:str)-> dict:
    diccionario = {}
    diccionario['nombre'] = nombre.replace(" ", "").capitalize()
    diccionario['apellido'] = apellido.replace(" ", "").capitalize()
    
    return diccionario

#9
def listar_nombres(lista:list)-> str:
   
    aux_cadena = ""
    for item in lista:
        aux_cadena = aux_cadena + item.capitalize() + "\n"
    return aux_cadena

#10
def generar_email(nombre:str, apellido:str)-> str:
    return nombre[0].lower() + "."+ apellido.lower() + "@utn-fra.com.ar"

#11
def concatenar_palabras(lista:list)-> str:
    aux_cadena = ""
    for item in lista:
        if item == lista[-1]:
            aux_cadena = aux_cadena + "y " + item.capitalize()
        else:
            aux_cadena = aux_cadena + item.capitalize() + ", "
    return aux_cadena

#12
def ocultar_numero(numeros:str)-> str:
    retorno = ""
    if numeros.isnumeric() or len(numeros) == 16:
        retorno = "**** **** **** " + numeros[-4:]
    else:
        retorno = "Error, lo ingresado no son numeros o su longitud no es de  "
    
    return retorno

#13
def eliminar_mail(correo:str)-> str:
    return correo.split("@")[0]

#14

def eliminar_dominio(url:str)-> str:
    return url.split(".")[1]

#15
def eliminar_simbolos_y_numeros(texto:str)-> str:
    texto_formateado = ""
    for caracter in texto:
        if caracter.isalpha() or caracter.isspace():
            texto_formateado += caracter
    return texto_formateado
        
#16
def acronimos_texto(texto:str)-> str:
    texto_separado = texto.split(" ")
    texto_retornado = ""
    for text in texto_separado:
        texto_retornado += text.capitalize()[0]
    return texto_retornado

#17
def rellenar_binario(nro_binario:str)-> str:
    ceros = "0" * (8 - len(nro_binario))
    return ceros + nro_binario
<<<<<<< HEAD
print(rellenar_binario("101"))
# Escribir una función que tome una cadena de car   acteres y reemplace todas las letras mayúsculas por letras minúsculas y todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"
=======

#18
def intercambiar_mayus_minus(cadena:str)-> str:
    cadena_formateada = ""

    for letra in cadena:
        if letra.islower():
            cadena_formateada += letra.upper()
        else:
            cadena_formateada += letra.lower()
    return cadena_formateada
>>>>>>> dd9077cc9e8d8a2b7cc1f61f12c8eb171b4308b2


#19
def cantidad_digitos(cadena:str)-> int:
    contador_digitos = 0
    for caracter in cadena:
        if caracter.isdigit():
            contador_digitos += 1
    return contador_digitos

# Escribir una función que tome una lista de direcciones de correo electrónico y las una en una sola cadena separada por punto y coma, por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> "juan@gmail.com;maria@hotmail.com".
#20



# Crear una función que reciba como parámetro un string y devuelva un diccionario donde cada clave es una palabra y cada valor es un entero que indica cuántas veces aparece esa palabra dentro del string.
#21

def imprimir_menu():

    print("______________________________________________________________")
    print("1) Todo a mayuscula")
    print("2) Todo a minuscula")
    print("3) Concatenar dos cadenas")
    print("4) Cantidad de caracteres de la cadena")
    print("5) Cantidad de veces que aparece un caracter en la cadena")
    print("6) Palabras que contienen un caracter")
    print("7) Eliminar espacios de la cadena")
    print("8) Nombre y apellido en un diccionario")
    print("9) Unir nombres en una cadena separada por un salto de linea")
    print("10) Crear un email")
    print("11) Palabras separadas por "","" e ""y""")
    print("12) Ocultar numeros de tarjeta de credito")
    print("13) Eliminar caracteres despues de @")
    print("14) Nombre de dominio")
    print("15) Caracteres alfabeticos")
    print("16) Acrónimo")
    print("17) Convertir a 8 bits")
    print("18) Cambiar mayusculas por minusculas y viceversa")
    print("19) Cantidad de digitos")
    print("20) Unir emails en una cadena separada por ;")
    print("21) Cantidad de veces que aparece una palabra")
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")


imprimir_menu()
while True:

    opcion = get_int("Ingrese una opcion: ","Error, el dato ingresado no es un numero valido")

    match opcion:
        case 1:
            texto = get_string("Ingrese un texto: ","Error, dato invalido")
            resultado = a_mayuscula(texto)

            print("El texto en mayuscula es: {0}".format(resultado))
        case 2:
            texto = get_string("Ingrese un texto: ","Error, dato invalido")
            resultado = a_minuscula(texto)
            print("El texto en minuscula es: {0}".format(resultado))
        case 3:
            texto1 = get_string("Ingrese un texto: ","Error, dato invalido")
            texto2 = get_string("Ingrese un texto: ","Error, dato invalido")
            resultado = concatenar(texto1, texto2)
            print("La cadena concatenada es: {0}".format(resultado))

        case 4:
            texto = get_string("Ingrese un texto: ","Error, dato invalido")
            resultado = contar_caracteres(texto)
            print("La cantidad de caracteres es: {0}".format(resultado))
        case 5:
            texto = get_string("Ingrese un texto: ","Error, dato invalido")
            caracter = get_char("Ingresar caracter: ")
            resultado = contar_caracteres_recurrentes(texto)
            print("La cantidad de caracteres recurrentes es: {0}".format(resultado))
        case 6:
            texto = get_string("Ingrese un texto: ")
            resultado = palabras_contenidas(texto)
            print("Las palabras que contienen es: {0}".format(resultado))
        case 7:
            pass
        case 8:
            pass
        case 9:
            pass
        case 10:
            pass
        case 11:
            pass
        case 12:
            pass
        case 13:
            pass
        case 14:
            pass
        case 15:
            pass
        case 16:
            pass
        case 17:
            pass
        case 18:
            pass
        case 19:
            pass
        case 20:
            pass
        case 21:
            pass
        case 22:
            print("Saliendo..")
            break
        case _:
            print("Opcion no valida")