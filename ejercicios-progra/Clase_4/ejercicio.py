from data_stark import lista_personajes

def nombrar_superheroes():
    if len(lista_personajes) == 0:
        print("No hay superhéroes")
    else:
        for superheroe in lista_personajes:
            print("Nombre: {0}".format(superheroe["nombre"]))

def nombrar_superheroe_y_altura():
    if len(lista_personajes) == 0:
        print("No hay superhéroes")
    else:
        for superheroe in lista_personajes:
            print("Nombre: {0} y su altura es: {1}cm".format(superheroe["nombre"], superheroe["altura"]))

def altura_mas_alto():
    altura_maxima = 0
    if len(lista_personajes) == 0:
        print("No hay superhéroes")
    else:
        for superheroe in lista_personajes:
            if float(superheroe["altura"]) > altura_maxima:
                altura_maxima = float(superheroe["altura"])
        print("La altura máxima es: {0}".format(altura_maxima))

def altura_mas_bajo():
    altura_minimo = 99999
    if len(lista_personajes) == 0:
        print("No hay superhéroes")
    else:
        for superheroe in lista_personajes:
            if float(superheroe["altura"]) < altura_minimo:
                altura_minimo = float(superheroe["altura"])
        print("La altura minima es: {0}".format(altura_minimo))

def altura_promedio():
    acumulador_altura = 0
    if len(lista_personajes) == 0:
        print("No hay superhéroes")
    else:
        for superheroe in lista_personajes:
            acumulador_altura += float(superheroe["altura"])
        print("La altura promedio es: {0}".format(acumulador_altura / len(lista_personajes)))
        
def nombre_altura_maxima():
    altura_maxima = 0
    if len(lista_personajes) == 0:
        print("No hay superhéroes")
    else:
        for superheroe in lista_personajes:
            if float(superheroe["altura"]) > altura_maxima:
                altura_maxima = float(superheroe["altura"])
                nombre = superheroe["nombre"]
        print("La altura máxima es: {0}cm y el nombre es: {1}".format(altura_maxima, nombre))
    
def nombre_altura_minima():
    altura_minimo = 99999
    if len(lista_personajes) == 0:
        print("No hay superhéroes")
    else:
        for superheroe in lista_personajes:
            if float(superheroe["altura"]) < altura_minimo:
                altura_minimo = float(superheroe["altura"])
                nombre = superheroe["nombre"]
        print("La altura minima es: {0}cm y el nombre es: {1}".format(altura_minimo, nombre))

def superheroe_mas_pesado():
    peso_maximo = 0
    if len(lista_personajes) == 0:
        print("No hay superhéroes")
    else:
        for superheroe in lista_personajes:
            if float(superheroe["peso"]) > peso_maximo:
                peso_maximo = float(superheroe["peso"])
                nombre = superheroe["nombre"]
        print("El peso máximo es: {0}kg y el nombre es: {1}".format(peso_maximo, nombre))

def superheroe_menos_pesado():
    peso_minimo = 99999
    if len(lista_personajes) == 0:
        print("No hay superhéroes")
    else:
        for superheroe in lista_personajes:
            if float(superheroe["peso"]) < peso_minimo:
                peso_minimo = float(superheroe["peso"])
                nombre = superheroe["nombre"]
        print("El peso mínimo es: {0}kg y el nombre es: {1}".format(peso_minimo, nombre))

def mostrar_superheroes():
    if len(lista_personajes) == 0:
        print("No hay superhéroes")
    else:
        for superheroe in lista_personajes:
            print("Nombre: {0}\nIdentidad: {1}\nEmpresa: {2}\nAltura: {3}cm\nPeso: {4}kg\nGenero: {5}\nColor de ojos: {6}\nColor de pelo: {7}\nFuerza: {8}\nInteligencia: {9}\n".format(superheroe["nombre"], superheroe["identidad"], superheroe["empresa"], superheroe["altura"], superheroe["peso"], superheroe["genero"], superheroe["color_ojos"], superheroe["color_pelo"], superheroe["fuerza"], superheroe["inteligencia"]))
                  
while True:
    print("1. Nombre de cada superhéroe \n2. Nombre de cada superhéroe junto a la altura del mismo\n3. Superhéroe más alto \n4. Superhéroe más bajo\n5. Altura promedio de los superhéroes\n6. Nombre del superhéroe asociado al máximo\n7. Nombre del superhéroe asociado al mínimo\n8. Superhéroe más pesado\n9. Superhéroe menos pesado\n10. Mostrar todos los superhéroes\n11. Salir")
    opcion = input("Ingrese una opción: ")
    
    match opcion:
        case "1":
            nombrar_superheroes()
        case "2":
            nombrar_superheroe_y_altura()
        case "3":
            altura_mas_alto()
        case "4":
            altura_mas_bajo()
        case "5":
            altura_promedio()
        case "6":
            nombre_altura_maxima()
        case "7":
            nombre_altura_minima()
        case "8":
            superheroe_mas_pesado()
        case "9":
            superheroe_menos_pesado()
        case "10":
            mostrar_superheroes()
        case "11":
            print("Salir")
            break
        case _:
            print("Opción inválida")
            pass