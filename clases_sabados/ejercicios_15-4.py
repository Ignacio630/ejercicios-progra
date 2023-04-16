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
lista_frutas = {"Manzana": 2.5, "Banana": 1.5, "Naranja": 1.2, "Pera": 1.8, "Mandarina": 1.3, "Durazno": 2.1, "Ciruela": 2.3, "Uva": 2.5, "Mango": 2.7, "Melon": 2.9}

while lista_frutas != {}:
    nombre_fruta = input("Ingrese el nombre de una fruta: ").capitalize()
    if nombre_fruta in lista_frutas:
        print("El precio de la {0} es {1}".format(nombre_fruta, lista_frutas[nombre_fruta]))
        lista_frutas.pop(nombre_fruta)
    else:
        print("La fruta ingresada no se encuentra en la lista")