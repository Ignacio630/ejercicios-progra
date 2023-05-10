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
def stark_normalizar_datos(lista_heroes:list)-> list:
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
def obtener_nombre(dict_heroe:dict)-> str:
    
    if len(dict_heroe) == 0:
        print("Se ingreso un diccionario vacio")
    else:
        return "Nombre: {0}".format(dict_heroe["nombre"]) 

""" 
    Imprime un String
    
    Parametros:
    strign(str): string que se va a imprimir
    Devolver:
    (): imprime el string pasado por parametros  
"""
def imprimir_dato(string:str):
    if type(string) == str:
        print(string)
    else:
        print("No se paso por parametro un string")


"""
    Listar los nombres de todos los heroes de la lista
    
    Parametros:
    lista_heroes(list): Recibe la lista de personajes
    Devolver:
    retorna(int): -1 
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


def obtener_nombre_y_dato(dict_heroe:dict, dato_a_obtener:str):
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

def calcular_max(lista_heroes, llave):
    atributo_maximo = 0
    heroe_maximo = {}
    if len(lista_heroes) == 0:
        print("La lista esta vacia")
    else:
        for heroe in lista_heroes:
            if heroe[llave] > atributo_maximo:
                atributo_maximo = heroe[llave]
                heroe_maximo = heroe
        return heroe_maximo
            

def calcular_min(lista_heroes, llave):
    atributo_minimo = float('inf')
    heroe_minimo = {}
    if len(lista_heroes) == 0:
        print("La lista esta vacia")
    else:
        for heroe in lista_heroes:
            if heroe[llave] < atributo_minimo:
                atributo_minimo = heroe[llave]
                heroe_minimo = heroe
        return heroe_minimo

def calcular_max_min_dato(lista_heroe,valor,atributo):
    if len(lista_heroe) == 0:
        print("La lista esta vacia")
    else:
        if valor.lower() == "maximo":
            return calcular_max(lista_heroe,atributo)
        elif valor.lower() == "minimo":
            return calcular_min(lista_heroe,atributo)
        else:
            print("El valor ingresado no es correcto")
            return -1

def stark_calcular_imprimir_heroe(lista_heroes,valor,atributo):
    if len(lista_heroes) == 0:
        print("La lista esta vacia")
        return -1
    else:
        if atributo == "altura" or atributo == "peso" or atributo == "fuerza":
            resultado_heroe = calcular_max_min_dato(lista_heroes,valor,atributo)
            imprimir_dato(obtener_nombre_y_dato(resultado_heroe,atributo))
        else:
            print("El dato ingresado no es valido")
# Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de héroes y un string que representara el dato/key de los héroes que se requiere sumar. 
# Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes de hacer la suma. 
# La función deberá retorna la suma de todos los datos según la key pasada por parámetro

def sumar_dato_heroe(lista_heroe:list,dato:str)-> float:
    acumulador_dato = 0
    if len(lista_heroe) == 0:
        print("Lista vacia")
    else:
        for heroe in lista_heroe:
            if type(heroe) != dict:
                print("El heroe ingresado no es un diccionario")
            else:
                acumulador_dato += heroe[dato]
        return acumulador_dato

def dividir(dividendo:int,divisor:int)-> int:
    if divisor == 0:
        print("No se puede dividir por 0 :)")
        return 0
    else:
        return dividendo/divisor

def calcular_promedio(lista_heroes:list, dato:str)->float:
    if not validar_lista(lista_heroes):
        return -1
    else:
        
        
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
            dato_a_obtener = input("Ingresar el dato del heroe que desea calcular: ")
                        
            if dato_a_obtener.lower() == "altura" or dato_a_obtener.lower() == "peso" or dato_a_obtener.lower() == "fuerza":
                resultado_heroe = calcular_max(lista_heroes_normalizada,dato_a_obtener)
                imprimir_dato(obtener_nombre_y_dato(resultado_heroe,dato_a_obtener))
            else:
                print("El dato ingresado no es valido")
        case "7":
            dato_a_obtener = input("Ingresar el dato del heroe que desea calcular: ")
            dato_a_obtener.lower()    
            if dato_a_obtener == "altura" or dato_a_obtener == "peso" or dato_a_obtener == "fuerza":
                resultado_heroe = calcular_min(lista_heroes_normalizada,dato_a_obtener)
                imprimir_dato(obtener_nombre_y_dato(resultado_heroe,dato_a_obtener))
            else:
                print("El dato ingresado no es valido")
        case "8":
            valor_deseado = input("Que calculo desea hacer? minimo/maximo: ")
            dato_a_obtener = input("Ingresar el dato del heroe que desea calcular: ")
            if dato_a_obtener == "altura" or dato_a_obtener == "peso" or dato_a_obtener == "fuerza":
                resultado_heroe = calcular_max_min_dato(lista_heroes_normalizada,valor_deseado,dato_a_obtener)
                imprimir_dato(obtener_nombre_y_dato(resultado_heroe,dato_a_obtener))
            else:
                print("El dato ingresado no es valido")
        case "9":
            # valor_deseado = input("Que calculo desea hacer? minimo/maximo: ")
            valor_deseado = input("Que calculo desea hacer? minimo/maximo: ")
            dato_a_obtener = input("Ingresar el dato del heroe que desea calcular: ")
            
            stark_calcular_imprimir_heroe(lista_heroes_normalizada,valor_deseado,dato_a_obtener)
        case "10":
            dato_a_obtener = input("Ingresar el dato del heroe que desea calcular: ")
            
            resultado = sumar_dato_heroe(lista_heroes_normalizada,dato_a_obtener)
            print("La suma de {0} es {1:.2f}".format(dato_a_obtener, resultado))
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
        case "16":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida")
            pass