import time
def quick_sort(lista:list)-> list:
    lista_de = []
    lista_iz = []
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]

        for elemento in lista[1:]:
            if elemento > pivot:
                lista_de.append(elemento)
            else:
                lista_iz.append(elemento)
    lista_iz = quick_sort(lista_iz)
    lista_iz.append(pivot)
    
    lista_de = quick_sort(lista_de)
    lista_iz.extend(lista_de)
    
    return lista_iz
    

antes = time.time()
print(quick_sort([2,1,1,3,4,5,12,123,54]))
despues = time.time()

tiempo = despues - antes

print("El tiempo que tardo es {0}".format(tiempo))