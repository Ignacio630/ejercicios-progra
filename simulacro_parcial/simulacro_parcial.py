import json
import os
from funciones_utiles import *
import re
os.system("cls")


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        lista_heroes = json.loads(contenido)
    return lista_heroes


def formatear_lista(lista: list) -> list:
    lista_copia = lista.copy()
    flag_normalizado = False
    if len(lista_copia) == 0:
        return print("Error: Lista de héroes vacía")
    else:
        for personaje in lista_copia:
            for llave in personaje:
                if type(personaje[llave]) != float:
                    if personaje[llave].replace(".", "").isdigit():
                        personaje[llave] = float(personaje[llave])
                        flag_normalizado = True
    if flag_normalizado:
        return lista_copia


def listar_heroes(lista: list):
    lista_copia = lista.copy()

    print("______________________________________________________________________________________________")
    for heroe in lista_copia:
        print("|{0}|{1}|{2}|{3}\t|{4}\t|{5}|{6}|{7}|{8}|{9}|".format(heroe["nombre"].center(20), heroe["identidad"].center(30), heroe["empresa"].center(
            10), heroe["altura"], heroe["peso"], heroe["genero"], heroe["color_ojos"].center(15), heroe["color_pelo"].center(15), heroe["fuerza"], heroe["inteligencia"].center(5)))
    print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")


def listar_cantidad_heroes(lista: list, cantidad_heroes: int) -> list:
    """
    """
    lista_copia = lista.copy()

    if cantidad_heroes <= len(lista_copia) and cantidad_heroes > 0:
        for heroe in lista_copia[:cantidad_heroes]:
            print(heroe)
    else:
        print("Error, la cantidad que ingreso, no es posible traerla")


# listar_cantidad_heroes(data_stark_lista)

def ordenar_lista(lista: list, ordenamiento: str, atributo: str) -> list:
    lista_copia = lista.copy()
    atributo_parseado = atributo

    if len(lista_copia) <= 1:
        return lista_copia
    else:
        if ordenamiento == "asc":
            for indice in range(len(lista_copia)):
                for elemento in range(len(lista_copia) - indice - 1):
                    if float(lista_copia[elemento][atributo_parseado]) > float(lista_copia[elemento + 1][atributo_parseado]):
                        lista_copia[elemento], lista_copia[elemento +
                                                           1] = lista_copia[elemento + 1], lista_copia[elemento]
        elif ordenamiento == "des":
            for indice in range(len(lista_copia)):
                for elemento in range(len(lista_copia) - indice - 1):
                    if float(lista_copia[elemento][atributo_parseado]) < float(lista_copia[elemento + 1][atributo_parseado]):
                        lista_copia[elemento], lista_copia[elemento +
                                                           1] = lista_copia[elemento + 1], lista_copia[elemento]
        else:
            print("Error, criterio de ordenamiento inválido")

    return lista_copia


def imprimir_menu():
    print(" _______________________________________")
    print("|1- Listar cantidad de heroes elegidos")
    print("|2- Ordenar y listar heroes por altura")
    print("|3- Ordenar y listar heroes por fuerza")
    print("|4- Calcular promedio de atributos numericos")
    print("|5- Buscar heroes por inteligencia")
    print("|6- Exportar la lista de heroes segun opcion elegida")
    print("|7- Salir")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")


# almacenamos el archivo json en una variable
data_stark = leer_archivo('simulacro_parcial\data_stark.json')

# almacenamos la lista heroes
data_stark_lista = data_stark["lista_personajes"]

lista_formateada = formatear_lista(data_stark_lista)

listar_heroes(lista_formateada)
with open("simulacro_parcial/prueba.csv", "w") as file:
    for elemento in lista_formateada:
        file.write("{0},{1},{2}\n".format(
            elemento["nombre"], elemento["identidad"], elemento["empresa"]))

# while True:

#     imprimir_menu()
#     opcion = get_int("|->Ingrese una opcion: ","Error, opcion invalida")
#     if opcion == 1:
#         cantidad_heroes = get_int("Ingrese la cantidad de heroes que desea traer: ", "Error, el dato ingresado es incorrecto")
#         lista_heroes = listar_cantidad_heroes(data_stark_lista,cantidad_heroes)
#         # print(lista_heroes)

#     elif opcion == 2:
#         lista =  ordenar_lista(data_stark_lista,"asc","altura")
#         # print(lista)
#         for h in lista:
#             print(h["nombre"],h["fuerza"])
#     elif opcion == 3:
#         pass
#     elif opcion == 4:
#         pass
#     elif opcion == 5:
#         pass
#     elif opcion == 6:
#         pass
#     elif opcion == 7:
#         print("Saliendo...")
#         break
#     else:
#         print("Error, opcion invalida")
