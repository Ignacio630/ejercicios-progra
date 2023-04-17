import os
os.system('cls')
# lista_personas = {"Juan": 20, "Ana": 25, "Pedro": 30, "Luis": 35, "Maria": 40}
# print(type(lista_personas))
# for p in lista_personas:
#     print("Nombre {0} - Edad {1}".format(p, ))

#2
#lista de 10 paises y su capital
# lista_paises = {"Argentina": "Buenos Aires", "Brasil": "Brasilia", "Chile": "Santiago", "Colombia": "Bogota", "Ecuador": "Quito", "Paraguay": "Asuncion", "Peru": "Lima", "Uruguay": "Montevideo", "Venezuela": "Caracas", "Bolivia": "La Paz"}

# nombre_pais = input("Ingrese el nombre de un pais: ").capitalize()

# while nombre_pais != "" and lista_paises != {}:
#     if nombre_pais in lista_paises:
#         print("La capital de {0} es {1}".format(nombre_pais, lista_paises[nombre_pais]))
#         break
#     else:
#         print("El pais ingresado no se encuentra en la lista")
#         nombre_pais = input("Ingrese el nombre de un pais: ").capitalize()

#3 
#lista de 10 frutas y su precio en dolares
# lista_frutas = {"Manzana": 2.5, "Banana": 1.5, "Naranja": 1.2, "Pera": 1.8, "Mandarina": 1.3, "Durazno": 2.1, "Ciruela": 2.3, "Uva": 2.5, "Mango": 2.7, "Melon": 2.9}

# while lista_frutas != {}:
#     nombre_fruta = input("Ingrese el nombre de una fruta: ").capitalize()
#     if nombre_fruta in lista_frutas:
#         print("El precio de la {0} es {1}".format(nombre_fruta, lista_frutas[nombre_fruta]))
#         break
#     else:
#         print("La fruta ingresada no se encuentra en la lista")
#         nombre_fruta = input("Ingrese el nombre de una fruta: ").capitalize()

#4

# crear un diccionario con 5 animales y su cantidad de patas

# lista_animales = {"Perro": 4, "Gato": 4, "Conejo": 4, "Pajaro": 2, "Tortuga": 4}

# while lista_animales != {}:
#     nombre_animal = input("Ingrese el nombre de un animal: ").capitalize()
#     if nombre_animal in lista_animales:
#         print("El {0} tiene {1} patas".format(nombre_animal, lista_animales[nombre_animal]))
#         break
#     else:
#         print("El animal ingresado no se encuentra en la lista")
#         nombre_animal = input("Ingrese el nombre de un animal: ").capitalize()

#5

# crear un diccionario con 20 alumnos y sus notas

# lista_alumnos = {"Juan": 10, "Ana": 9, "Pedro": 8, "Luis": 7, "Maria": 6, "Jose": 5, "Marta": 4, "Raul": 3, "Miguel": 2, "Lucia": 1, "Carlos": 10, "Sofia": 9, "Fernando": 8, "Jorge": 7, "Mariana": 6, "Javier": 5, "Micaela": 4, "Rocio": 3, "Martin": 2, "Lorena": 1}
# mayor_nota = 0
# while lista_alumnos != {}:
#     nombre_alumno = input("Ingrese el nombre de un alumno: ").capitalize()
#     if nombre_alumno in lista_alumnos:
#         print("La nota de {0} es {1}".format(nombre_alumno, lista_alumnos[nombre_alumno]))
#         break
#     else:
#         print("El alumno ingresado no se encuentra en la lista")
#         nombre_alumno = input("Ingrese el nombre de un alumno: ").capitalize()

# for a in lista_alumnos:
#     if lista_alumnos[a] > mayor_nota:
#         mayor_nota = lista_alumnos[a]
#         nombre_alumno = a
#         print("El alumno con mayor nota es {0} con {1}".format(nombre_alumno, mayor_nota))

#5)1) 

# lista_personas = {}

# while len(lista_personas) < 5:
#     p_key = input("Ingrese un nombre: ")
#     lista_personas[p_key] = int(input("Ingrese la edad: "))
#     if p_key == '' or lista_personas[p_key] == '':
#         print("Error, no se ingreso una persona")
#         p_key = input("Ingrese un nombre: ")
#         lista_personas[p_key] = int(input("Ingrese la edad: "))


# for p in lista_personas:
#     print("Nombre: {} Edad: {}".format(p.capitalize(),lista_personas[p]))

lista_personas = {}
seguir = "s"


while seguir != 'n':
    
    nombre = input("Ingrese un nombre: ")
    edad = int(input("Ingrese su edad: "))
    altura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en kg: "))
    ciudad = input("Ingrese su ciudad: ")

    lista_personas[nombre] = {"edad": edad, "altura": altura, "peso": peso, "ciudad": ciudad}
    seguir = input("Desea seguir? s/n: ").lower()
    
    if seguir != 'n' and seguir != 's':
        print("Error, ingrese una opcion valida")
        seguir = input("Desea seguir? s/n: ").lower()

for p in lista_personas:
    print("Nombre: {} Edad: {} Altura: {} Peso: {} Ciudad: {}".format(p.capitalize(),lista_personas[p]["edad"], lista_personas[p]["altura"], lista_personas[p]["peso"], lista_personas[p]["ciudad"].capitalize()))
