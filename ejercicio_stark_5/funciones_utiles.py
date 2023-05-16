def get_str(mensaje:str):
    retorno_str = -1
    while retorno_str == -1:
        if isinstance(mensaje,str) != True or len(mensaje) == 0:
            retorno_str = "No se ingreso un parametro valido"
            break
        else:
            dato = input(mensaje)
            
            if dato.isalpha():
                retorno_str = dato.lower()
                break
    
    return retorno_str

dato = get_str("Dato: ")

print(dato)