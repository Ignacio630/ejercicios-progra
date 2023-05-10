def validar_lista(lista:list)-> bool:
    if len(lista) == 0:
        print("La lista se encuentra vacia")
        return False
    else:
        return True

def atributos_numericos_heroe(atributo:str)-> bool:

    if isinstance(atributo, int) or isinstance(atributo, float):         
        return True
    else:
        return False 


