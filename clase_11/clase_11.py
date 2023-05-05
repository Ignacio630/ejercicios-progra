import re 

# texto = "uno 1 dos 2 tres 3 cuatro"
# fecha = "2022-07-06 00:00:00"
# print(re.split('[\- :]{1}',fecha))
# print(re.split('[-]{1}',fecha))

# 1->
# def es_mayuscula(texto):
#     return bool(re.match(r"^[A-Z ]+$",texto))



# input = input("Ingrese un texto: ")

# print("Es mayuscula? {0}".format(es_mayuscula(input)))

# 2->

# def es_minuscula(texto):
#     return bool(re.match(r"^[a-z ]+$",texto))


# input = input("Ingrese un texto: ")

# print("Es minuscula? {0}".format(es_minuscula(input)))

# 3->

# def es_entero(numero):
#     return bool(re.match(r"^[0-9]+$",numero))


# input = input("Ingrese un numero: ")

# print("Es solo_texto? {0}".format(es_entero(input)))

# 4-> 

# def es_solo_texto(texto):
#     return bool(re.match(r"^[a-zA-Z ]+$",texto))


# input = input("Ingrese un texto: ")

# print("Es solo_texto? {0}".format(es_solo_texto(input)))

#  5->
def es_decimal(numero, separador):
    numero_solo = re.sub(separador, "", numero)
    es_digito_o_no = bool(re.match("-?[0-9]*$", numero_solo))
    if es_digito_o_no:
        research = re.search(separador, numero)
        return bool(research)
    else: 
        return False