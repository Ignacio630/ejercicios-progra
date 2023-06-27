from data_stark import lista_personajes
import os
os.system("cls")

# 1 Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
# 2 Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
# 3 Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
# 4 Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
# 5 Recorrer la lista y determinar cuál es el superhéroe más bajo  de género M 
# 6 Recorrer la lista y determinar cuál es el superhéroe más bajo  de género F 
# 7 Recorrer la lista y determinar la altura promedio de los  superhéroes de género M
# 8 Recorrer la lista y determinar la altura promedio de los  superhéroes de género F
# 9 Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
# 10 Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# 11 Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# 12 Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’). 
# 13 Listar todos los superhéroes agrupados por color de ojos.
# 14 Listar todos los superhéroes agrupados por color de pelo.
# 15 Listar todos los superhéroes agrupados por tipo de inteligencia

def listar_nombre_por_genero(genero, lista_personajes):
    for personaje in lista_personajes:
        genero_personaje = personaje["genero"]
        if genero_personaje == genero:
            print(personaje["nombre"])

def listar_personje_por_altura_y_genero(altura, genero, lista_personajes):
    altura_maxima = 0
    if len(lista_personajes) == 0:
        print("No hay superhéroes")
    else:
        for superheroe in lista_personajes:
            genero_personaje = superheroe["genero"]
            if altura == "A":
                if float(superheroe["altura"]) > altura_maxima and genero_personaje == genero :
                    altura_maxima = float(superheroe["altura"])
                    nombre_personaje = superheroe["nombre"]
            elif altura == B:
                if float(superheroe["altura"]) < altura_maxima and genero_personaje == genero :
                    altura_maxima = float(superheroe["altura"])
                    nombre_personaje = superheroe["nombre"]   
        print("El nombre del personaje mas alto es: {0}".format(nombre_personaje))
    
while True:
    print("1-Imprimir superhereos Masculinos\n2-Imprimir superhereos Femeninos\n3-Imprimir superhereos Masculinos\n4-Limpiar consola\n5-Salir")
    opcion = input("Ingrese opcion: ")
    match opcion:
        case "1":
            listar_nombre_por_genero("M", lista_personajes)
        case "2":
            listar_nombre_por_genero("F", lista_personajes)
        case "3":
            listar_personje_por_altura_y_genero("A","M", lista_personajes)
        case "4":
           listar_personje_por_altura_y_genero("A","F", lista_personajes)
        case "5":
            pass
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
        case "16":
            os.system("cls")
        case "17":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida")
            pass

    