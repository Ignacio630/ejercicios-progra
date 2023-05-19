import random
import time


def quick_sort(lista_original:list,flag_orden:bool)->list:
    lista_de = []
    lista_iz = []
    if(len(lista_original)<=1):
        return lista_original
    else:
        pivot = lista_original[0]
        for elemento in lista_original[1:]:
            if(elemento > pivot):
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    lista_iz = quick_sort(lista_iz,True)
    lista_iz.append(pivot) 
    lista_de = quick_sort(lista_de,True)
    lista_iz.extend(lista_de) 
    return lista_iz

def ivan_sort_B(lista_original:list,flag_orden:bool):
    lista = lista_original[:]
    rango_a = len(lista) - 1
    flag_swap = True

    while(flag_swap):
        flag_swap = False

        for indice_A in range(rango_a):
            if  flag_orden == False and lista[indice_A] < lista[indice_A+1] \
             or flag_orden == True and lista[indice_A] > lista[indice_A+1]:
                lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                flag_swap = True
    return lista

def ivan_sort_A(lista_original:list):
    lista = lista_original[:]
    rango_a = len(lista)
    flag_swap = True
    contador = 0
    while(flag_swap):
        flag_swap = False
        rango_a = rango_a - 1

        for indice_A in range(rango_a):
            contador += 1
            if  lista[indice_A] < lista[indice_A+1]:
                lista[indice_A],lista[indice_A+1] = lista[indice_A+1],lista[indice_A]
                flag_swap = True

    print(r"IVAN {0}".format(contador))

    return lista


lista = list(range(100000))
random.shuffle(lista)

antes = time.time()
lista_ordenada =quick_sort(lista,True)
despues = time.time()

tiempo =  despues - antes
print("Tardo {0}".format(tiempo))
# print(lista_ordenada)