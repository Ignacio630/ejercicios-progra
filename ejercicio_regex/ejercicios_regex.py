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