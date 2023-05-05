from data_stark import lista_personajes
from funciones_utiles import *
import os
os.system("cls")

"""
    Parametros:
    Devolver:
"""
## Reutilizar

"""
    Normalizar los datos de la lista de heroes con los datos correspondientes
    
    Parametro:
    lista_heroes(list): lista de heroes
    
    Devolver:
    (list): Lista de heroes con los valores formateados
"""
def stark_normalizar_datos(lista_heroes):
    flag_normalizado = False
    if len(lista_heroes) == 0:
        return print("Error: Lista de héroes vacía")
    else:
        for personaje in lista_heroes:
            for llave in personaje:
                if type(personaje[llave]) != float:
                    if personaje[llave].replace(".","").isdigit():
                        personaje[llave] = float(personaje[llave])
                        flag_normalizado = True                
    if flag_normalizado:
        return lista_heroes        

"""
    Devuelve el nombre del heroe pasado por parametro
    
    Parametros:
    dict_heroes(dict): diccionario con todos los datos del heroe
    Devolver:
    (string): Devuelve el nombre del heroe pasado por parametro
"""
def obtener_nombre(dict_heroe):
    
    if len(dict_heroe) == 0:
        print("Se ingreso un diccionario vacio")
    else:
        return "Nombre: {0}".format(dict_heroe["nombre"]) 

""" 
    Imprime un String
    
    Parametros:
    strign(str): string que se va a imprimir
    Devolver:
    (str): imprime el string pasado por parametros  
"""
def imprimir_dato(string):
    if type(string) == str:
        print(string)
    else:
        print("No se paso por parametro un string")

"""
    Listar los nombres de todos los heroes de la lista
    
    Parametros:
    lista_heroes(list): Recibe la lista de personajes
    Devolver:
    Imprime los datos pasados por parametro
    Retorna(int): -1
"""
def stark_imprimir_nombres_heroes(lista_heroes):
    if len(lista_heroes) == 0:
        print("La lista ingresada se encuentra vacia")
        return -1
    else:
        for heroe in lista_heroes:
            imprimir_dato(obtener_nombre(heroe))

"""
    Mostrar el nombre y el dato que se paso por parametro
    
    Parametros:
    heroe(dict): El heroe del cual se obtendra el dato
    dato(str): El dato que se desea obtener del heroe
    Devolver:
    
"""


def obtener_nombre_y_dato(dict_heroe, dato_a_obtener):
    resultado = ""
    
    if dato_a_obtener in dict_heroe:
        resultado = dict_heroe[dato_a_obtener]
        return "{0} | {1}: {2}".format(obtener_nombre(dict_heroe),dato_a_obtener,resultado)
    else:
        return

def stark_imprimir_nombres_alturas(lista_heroes:list):
    if len(lista_heroes) == 0:
        print("La lista ingresada se encuentra vacia")
        return -1
    else:
        for heroe in lista_heroes:
            imprimir_dato(obtener_nombre_y_dato(heroe,"altura"))



lista_heroes_normalizada = []

while True:
    print("1-Imprimir superhereos Masculinos\n2-Imprimir superhereos Femeninos\n3-Imprimir superhereos Masculinos\n4-Limpiar consola\n5-Salir")
    opcion = input("Ingrese opcion: ")
    match opcion:
        case "1":
            lista_heroes_normalizada = stark_normalizar_datos(lista_personajes)
            print("Lista normaliada..")
        case "2":
            nro_heroe = int(input("Ingrese el numero de heroe: "))
            heroe_elegido = lista_heroes_normalizada[nro_heroe]
            nombre_heroe = obtener_nombre(heroe_elegido)
            imprimir_dato(nombre_heroe)
        case "3":
            stark_imprimir_nombres_heroes(lista_heroes_normalizada)
        case "4":
            nro_heroe = int(input("Ingrese el numero de heroe: "))
            # print(lis)
            heroe_elegido = lista_heroes_normalizada[nro_heroe]
            dato_a_obtener = input("Ingrese el dato a obtener del heroe: ")
            
            if obtener_nombre_y_dato(heroe_elegido,dato_a_obtener):
                imprimir_dato(obtener_nombre_y_dato(heroe_elegido,dato_a_obtener))
            else:
                print("El heroe o el atributo a mostrar no existe:")
        case "5":
            stark_imprimir_nombres_alturas(lista_heroes_normalizada)
        case "6":
            pass
        case "7":
            pass
        case "8":
            pass
        case "9":
            pass
        case "10":
            pass
        case "11":
            pass
        case "12":
            pass
        case "13":
            pass
        case "14":
            pass
        case "15":
            pass
        case "cc":
            os.system("cls")
        case "17":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida")
            pass