import json
import os
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



def listar_cantidad_heroes(lista:list)-> list:
    """
    """
    lista_copia = lista.copy()
    
    cantidad_heroes = int(input("Ingrese la cantidad de heroes que desea validar: "))
    if cantidad_heroes <= len(lista_copia):
        for heroe in lista_copia[:cantidad_heroes]:
            print(heroe)
            

# listar_cantidad_heroes(data_stark_lista)

def ordenar_lista(lista: list, ordenamiento: str) -> list:
    lista_copia = lista.copy()
    
    if len(lista_copia) <= 1:
        return lista_copia
    else:
        if ordenamiento == "asc":
            for indice in range(len(lista_copia)):
                for elemento in range(len(lista_copia) - indice - 1):
                    if float(lista_copia[elemento]["altura"]) > float(lista_copia[elemento + 1]["altura"]):
                        lista_copia[elemento], lista_copia[elemento + 1] = lista_copia[elemento + 1], lista_copia[elemento]
        elif ordenamiento == "des":
            for indice in range(len(lista_copia)):
                for elemento in range(len(lista_copia) - indice - 1):
                    if float(lista_copia[elemento]["altura"]) < float(lista_copia[elemento + 1]["altura"]):
                        lista_copia[elemento], lista_copia[elemento + 1] = lista_copia[elemento + 1], lista_copia[elemento]
        else:
            print("Error, criterio de ordenamiento inválido")

    return lista_copia
            
# def ordenar_lista_altura(lista:list):
#     ordenamiento = input("Forma de ordenamiento ascendente(asc) o descendente(desc): ")
#     if ordenamiento == "asc":
        
#     elif ordenamiento == "desc":
        
#     else:
#         print("Opcion invalida")
lista =  ordenar_lista(data_stark_lista,"asc")

for h in lista:
    print(h["nombre"],h["altura"])