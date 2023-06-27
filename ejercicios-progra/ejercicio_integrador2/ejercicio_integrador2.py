from data_stark import lista_personajes
from funciones_utn import *
import os
os.system("cls")

def listar_heroes_masculinos(lista_heroes,genero):
    for heroe in lista_heroes:
        if genero != "M" or genero != "F":
            print("Error. Debe ingresar M o F")
            break
        else:
            if heroe["genero"] == "M" and genero == "M":
                print(heroe["nombre"])
            elif heroe["genero"] == "F" and genero == "F":
                print(heroe["nombre"]) 

def heroe_mas_alto(lista_heroes, genero):
    altura_maxima = 0
    if len(lista_heroes) == 0:
        print("La lista ingresada esta vacia")
    else:
        for h in lista_heroes:
            altura = float(h["altura"])
            genero_heroe = h["genero"]
            if genero_heroe == genero:
                if altura > altura_maxima:
                    altura_maxima = altura
                    nombre_heroe = h["nombre"]
    if genero == "M":
        print("El heroe masculino mas alto es: {0} con {1}cm".format(nombre_heroe,altura_maxima))
    elif genero == "F":
        print("La heroina mas alta es: {0} con {1}cm".format(nombre_heroe,altura_maxima))

def heroe_mas_bajo(lista_heroes, genero):
    altura_minima = 10000000
    if len(lista_heroes) == 0:
        print("La lista ingresada esta vacia")
    else:
        for h in lista_heroes:
            altura = float(h["altura"])
            genero_heroe = h["genero"]
            if genero_heroe == genero:
                if altura < altura_minima:
                    altura_minima = altura
                    nombre_heroe = h["nombre"]
    if genero == "M":
        print("El heroe masculino mas bajo es: {0} con {1}cm".format(nombre_heroe,altura_minima))
    elif genero == "F":
        print("La heroina mas bajo es: {0} con {1}cm".format(nombre_heroe,altura_minima))

def promedio_altura_heroes(lista_heroes,genero):
    cantidad_heroes = 0
    acumulador_altura = 0
    if len(lista_heroes) == 0:
        print("La lista ingresada esta vacia")
    else:
        for h in lista_heroes:
            altura = float(h["altura"])
            genero_heroe = h["genero"]
            if genero_heroe == genero:
                acumulador_altura += altura
                cantidad_heroes += 1
        promedio = acumulador_altura / cantidad_heroes
        if genero == "M":
            print("El promedio de altura de los heroes masculinos es: {0}".format(promedio))
        elif genero == "F":
            print("El promedio de altura de las heroinas es: {0}".format(promedio))
        else:
            print("Error. Debe ingresar M o F")

def cantidad_heroes_color_ojos(lista_heroes):
    



while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("a. Nombrar cada heroe genero masculino")
    print("b. Nombrar cada heroe genero femenino")
    print("c. Heroe mas alto masculino")
    print("d. Heroe mas alto femenino")
    print("e. Heroe mas bajo masculino")
    print("f. Heroe mas bajo femenino")
    print("g. Promedio altura heroes masculinos")
    print("h. Promedio altura heroes femeninos")
    print("i. Informar nombre de los anteriores puntos")
    print("j. Mostrar cantidad de heroes por color de ojos")
    print("k. Mostrar cantidad de heroes por color de pelo")
    print("l. Mostrar cantidad de heroes por inteligencia")
    print("m. Listar heroes por color de ojos")
    print("n. Listar heroes por color de pelo")
    print("o. Listar heroes por inteligencia")
    print("s. Salir del programa")
    opcion = utn_input_string("Ingrese una opcion: ")

    match opcion:
        case "a":
            listar_heroes_masculinos(lista_personajes, "M")
        case "b":
            listar_heroes_masculinos(lista_personajes, "F")
        case "c":
            heroe_mas_alto(lista_personajes, "M")
        case "d":
            heroe_mas_alto(lista_personajes, "F")
        case "e":
            heroe_mas_bajo(lista_personajes, "M")
        case "f":
            heroe_mas_bajo(lista_personajes, "F")
        case "g":
            promedio_altura_heroes(lista_personajes, "M")
        case "h":
            promedio_altura_heroes(lista_personajes, "F")
        case "i":
            pass
        case "j":
            pass
        case "k":
            pass
        case "l":
            pass
        case "m":
            pass
        case "n":
            pass
        case "o":
            pass
        case "s":
            print("Gracias por usar mi app... :3")
            break
        case "cc":
            os.system("cls")
        case _:
            print("Error. Opcion incorrecta")
