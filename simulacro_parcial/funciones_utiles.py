def get_string(mensaje:str,mensaje_error:str)-> str:
    
    while True:
        if isinstance(mensaje,str) != True or len(mensaje) == 0:
            print("No se ingreso un parametro valido")
            break
        else:
            dato = input(mensaje)
            
            for char in dato:
                if char.isalpha() or char.isspace():
                    return dato.lower()
                else:
                    print(mensaje_error)
    

def get_char(mensaje:str,mensaje_error:str)-> chr:
    retorno_str = -1
    while retorno_str == -1:
        if isinstance(mensaje,str) != True or len(mensaje) == 0:
            retorno_str = "No se ingreso un parametro valido"
            break
        else:
            dato = get_string(mensaje,mensaje_error)
            if len(dato) == 1:
                retorno_str = dato.lower()
                break
            
            else:
                print(mensaje_error)
        
    return retorno_str


def get_int(mensaje:str,mensaje_error:str)-> int:
    retorno_int = -1
    while retorno_int == -1:
        if isinstance(mensaje,str) != True or len(mensaje) == 0:
            retorno_int = "No se ingreso un parametro valido"
            break
        else:
            dato = input(mensaje)
            
            if dato.isnumeric():
                retorno_int = int(dato)
                break
            else:
                print(mensaje_error)
    
    return retorno_int