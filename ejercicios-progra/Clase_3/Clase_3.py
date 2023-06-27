

#DICT


dict_alumno = {"edad":22,"legajo":205664,"Nombre":"Juan","Apellido":"Perez"}
dict_alumno["cuit"] = "22-123334444-9"

print("El legajo es {0}, el nombre es {1} y el apellido es {2}".format( dict_alumno["legajo"],
                                                                        dict_alumno["Nombre"],
                                                                        dict_alumno["Apellido"]))


print("El legajo es {0}, el nombre es {1} y el apellido es {2}, y su cuit es: {3}".format( dict_alumno["legajo"],
                                                                        dict_alumno["Nombre"],
                                                                        dict_alumno["Apellido"],
                                                                        dict_alumno["cuit"]))


clave = dict_alumno.keys()

for clave in dict_alumno.keys():
    value = dict_alumno[clave]
    print("La clave es: {0} y tiene el valor: {1}".format(clave, value))
    
for clave,valor in dict_alumno.items():
    print("La clave es: {0} y tiene el valor: {1}".format(clave, value))