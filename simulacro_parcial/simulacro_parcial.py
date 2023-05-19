import json
import os
from funciones_utiles import *
os.system("cls")

def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
        lista_heroes = json.loads(contenido)
    return lista_heroes

# almacenamos el archivo json en una variable
data_stark = leer_archivo('simulacro_parcial\data_stark.json')

# almacenamos la lista heroes
data_stark_lista = data_stark["lista_personajes"]


def quick_sort(lista:list):


def listar_cantidad_heroes(lista:list, cantidad_heroes:int)-> list:
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
                        lista_copia[elemento], lista_copia[elemento + 1] = lista_copia[elemento + 1], lista_copia[elemento]
        elif ordenamiento == "des":
            for indice in range(len(lista_copia)):
                for elemento in range(len(lista_copia) - indice - 1):
                    if float(lista_copia[elemento][atributo_parseado]) < float(lista_copia[elemento + 1][atributo_parseado]):
                        lista_copia[elemento], lista_copia[elemento + 1] = lista_copia[elemento + 1], lista_copia[elemento]
        else:
            print("Error, criterio de ordenamiento inválido")

    return lista_copia
            

def imprimir_menu():
    print(" _______________________________________")
    print("|1-")
    print("|2-")
    print("|3-")
    print("|4-")
    print("|5-")
    print("|6-")
    print("|7- Salir")
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")





while True:
    
    imprimir_menu()
    opcion = get_int("|->Ingrese una opcion: ","Error, opcion invalida")
    if opcion == 1:
        cantidad_heroes = get_int("Ingrese la cantidad de heroes que desea traer: ", "Error, el dato ingresado es incorrecto")
        lista_heroes = listar_cantidad_heroes(data_stark_lista,cantidad_heroes)
        # print(lista_heroes)

    elif opcion == 2:
        lista =  ordenar_lista(data_stark_lista,"asc","altura")
        # print(lista)
        for h in lista:
            print(h["nombre"],h["fuerza"])
    elif opcion == 3:
        pass 
    elif opcion == 4:
        pass 
    elif opcion == 5:
        pass 
    elif opcion == 6:
        pass 
    elif opcion == 7:
        print("Saliendo...")
        break
    
    
