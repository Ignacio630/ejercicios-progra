nombre = "Juan"
numero_entero = 3
numero_flotante = 0.123

if(numero_entero > 8):
    print("El numero es mayor a 8")

lista = [1,2,3,4,5,6]

for e in lista:
    print(e)


while numero_entero > 1:
    print(numero_entero)
    if numero_entero >= 3: 
        print("Numero >= 3")
        break




def es_par(num):
    if num % 2 == 0:
        return print("es par")
    else:
        return print("no es par")
    
es_par(3)