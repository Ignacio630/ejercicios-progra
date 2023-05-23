import re
import os 

os.system("cls")

def imprimir_dato(string:str):
    if isinstance(string,str):
        print(string)
    else:
        print("No se paso por parametro un string")


def imprimir_menu():
    imprimir_dato("_________________________________")
    imprimir_dato("| 1- es_mayuscula\t\t|")
    imprimir_dato("| 2- es_minuscula\t|")
    imprimir_dato("| 3- es_entero\t|")
    imprimir_dato("| 4- es_solo_texto\t\t|")
    imprimir_dato("| 5- es_decimal\t|")
    imprimir_dato("| 6- es_alfanumerico\t\t|")
    imprimir_dato("| 7- es_binario\t\t|")
    imprimir_dato("| 8- comienza con ""u""\t|")
    imprimir_dato("| 9- imprimir palabras con 3 y 6 caracteres\t|")
    imprimir_dato("| 10- termina con ""Cion""\t\t|")
    imprimir_dato("| 11- Calcular promedio\t\t|")
    imprimir_dato("| 12- Salir\t\t\t|")
    imprimir_dato("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

def es_mayuscula(string:str)-> bool:
# Crear una función llamada es_mayuscula que reciba un string y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario

    patron = r'^[A-Z\s]+$'

    resultado = re.match(patron,string)

    return bool(resultado)
    
def es_minuscula(string:str)-> bool:
# Crear una función llamada es_minuscula que reciba un string y devuelva True en caso de que todas las letras sean mayúsculas o False en el caso contrario

    patron = r'^[a-z\s]+$'

    resultado = re.match(patron,string)

    return bool(resultado)


# Crear una función llamada es_entero que reciba un string y devuelva True en caso de que se trate de un número entero y False en caso contrario.

def es_entero(numero:str)->bool:
    patron = r'^[0-9+]?\d+$'

    resultado = re.match(patron,numero)

    return bool(resultado)

# Crear una función llamada es_solo_texto que reciba un string y devuelva True en caso de que trate solo de caracteres alfabéticos y el espacio y False en el caso contrario

# Crear una función llamada es_decimal que reciba dos strings: el primero representa la expresión a evaluar y el segundo el separador decimal (puede ser punto . o coma ,). Debe devolver True en caso que se trate de un número decimal y False en el caso contrario.


# Crear una función llamada es_alfanumerico que devuelva True en caso de tratarse de solo letras y números y False en el caso contrario (es decir que contenga caracteres especiales) 


# Crear una función llamada es_binario que devuelva True en caso de un número binario válido (solo ceros y unos) o False en el caso contrario

# Crear una función que reciba una lista de palabras y devuelva otra lista con las palabras  que comienzan con la letra ‘U’


# Crear una función que reciba un texto y devuelva una lista con las palabras que contienen entre 3 y 6 caracteres de largo


# Crear una función que reciba un texto y devuelva una lista de todas las palabras que terminan con ‘ción’. Ejemplo de texto: https://onlinegdb.com/swyremkF6


# Crear una función que reciba un texto y devuelva una la lista de palabras encuentra que comienzan con una vocal


# Crear una función llamada obtener_oraciones que reciba como parámetro un string y que devuelva una lista con las oraciones (delimitadores, ‘.’, ‘!’, ‘?’). Ejemplo de texto: https://onlinegdb.com/UMdr3hI3G

# Crear una función que reciba un texto como parámetro y que corrija los errores de ortografía que no cumplan con la regla ortográfica que indica que antes de V se escribe N y que antes de B se escribe M. 
# Por ejemplo, si el texto es: "Mi comvicción me hace sentir que es el momento de imvertir tiempo para finalmente enbarcar en esta nueva aventura." La función debería devolver:
# “Mi convicción me hace sentir que es el momento de invertir tiempo para finalmente embarcar en esta nueva aventura."


# Crear la función es_fecha que reciba dos string, el primero representa la expresión a evaluar y el segundo el separador de la fecha (puede ser la barra / o el guión -) y que devuelva True en caso de tratarse de una fecha válida y False en el caso contrario. Los formatos admitidos son: ‘dd/mm/aaaa’ o ‘dd-mm-aaaa’


# Crear la función es_hora que reciba un string y que devuelva True en caso de tratarse de una hora válida y False en el caso contrario. El formato admitido es ‘hh:mm:ss’

# Crear la función validar_codigo_postal que reciba un string como parámetro y devuelva True en caso de tratarse de código postal válido o False en caso contrario. 



# Crear la función validar_patente que reciba un string como parámetro y devuelva True en caso de tratarse de un número de patente válido o False en caso contrario.  Debe poder admitir estos dos tipos:





# Crear una función que se llame obtener_direcciones_email que reciba un texto y devuelva una lista con todas las direcciones de email válidas que encuentren en el mismo. Acá dejamos un texto de ejemplo: https://onlinegdb.com/Ln0jhatKeI



# Crear una función llamada validar_password que reciba un string y verifique si se trata de una contraseña cumple con los requisitos mínimos de seguridad:


# Al menos 8 caracteres
# Al menos una letra mayúscula y una letra minúscula
# Un número 
# Un carácter especial
	
# En caso de no cumplir con alguno de los requisitos, imprimir un mensaje informando cual no se cumplio
# Crear una función llamada validar_ip que reciba un string como parámetro y verifique si se trata de una dirección IP v4 válida, en caso de serlo retornar True de lo contrario retornar False. 
# Se considera una dirección IP válida si tiene el formato xxx.xxx.xxx.xxx, donde xxx es un número entero entre 0 y 255.




while True:
    imprimir_menu()
    opcion = input("Ingresa una opcion: ")

    if opcion == "1":
        texto = input("Ingrese un texto: ")
        
        if es_mayuscula(texto):
            imprimir_dato("El texto ingresado esta mayuscula")
        else:
            imprimir_dato("El texto ingresado no esta mayuscula")

    elif opcion == "2":
        texto = input("Ingrese un texto: ")

        if es_minuscula(texto):
            imprimir_dato("El texto ingresado esta minuscula")
        else:
            imprimir_dato("El texto ingresado no esta minuscula")
    elif opcion == "3":
        numero = input("Ingrese un numero: ")

        if es_entero(numero):
            imprimir_dato("El numero ingresado es entero")
        else:
            imprimir_dato("El numero ingresado no es entero")

    elif opcion == "4":
        pass
    elif opcion == "5":
        pass
    elif opcion == "6":
        pass
    elif opcion == "7":
        pass
    elif opcion == "8":
        pass
    elif opcion == "9":
        pass
    elif opcion == "10":
        pass
    elif opcion == "11":
        pass
    elif opcion == "12":
        pass
    elif opcion == "13":
        pass
    elif opcion == "14":
        pass
    elif opcion == "15":
        pass
    elif opcion == "16":
        pass
    elif opcion == "17":
        pass
    elif opcion == "18":
        pass
    elif opcion == "19":
        pass
    elif opcion == "20":
        pass
    elif opcion == "21":
        imprimir_dato("Saliendo..")
        break
    else:
        imprimir_dato("Opcion incorrecta")