def utn_input_int(mensaje):
    """Solicita un número entero al usuario y lo devuelve."""
    
    while True:
        numero = input(mensaje)        
        if numero.isdigit():
            return int(numero)
        else:
            print("ERROR. Debe ingresar un número entero...")

def utn_input_string(mensaje):
    """Solicita un número entero al usuario y lo devuelve."""
    
    while True:
        numero = input(mensaje)        
        if numero.isalpha():
            return numero
        else:
            print("ERROR. Debe ingresar un texto...")

