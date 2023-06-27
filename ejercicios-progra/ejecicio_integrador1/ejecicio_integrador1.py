# Ignacio Javier Medici
# Division 1 H 

miembros_ids = [1,2,3,4,5,6,7,8,9,10]
miembros_nombres = ["Juan","Pedro","Maria","Jose","Luis","Ana","Lorena","Miguel","Sofia","Lucas"]
miembros_edades = [20,30,40,50,60,70,80,90,100,110]
miembros_membresias = ["Mensual","Anual","Mensual","Anual","Mensual","Anual","Mensual","Anual","Mensual","Anual"]

while True:
    # Mostrar menú de opciones
    print("Menú de opciones:")
    print("1. Agregar un nuevo miembro")
    print("2. Mostrar la informacion de todos los miembros")
    print("3. Actualizar el tipo de membresía de un miembro")
    print("4. Buscar información de un miembro")
    print("5. Calcular el promedio de edad de los miembros")
    print("6. Buscar el miembro más joven y el más viejo")
    print("0. Salir del programa")
    opcion = input("\nIngrese la opción deseada: ")
    
    # Opción 1: Agregar un nuevo miembro
    if opcion == "1":
        print("Ingrese los datos del nuevo miembro:")
        id_miembro = miembros_ids[-1] + 1
        nombre_miembro = input("Nombre: ")
        edad_miembro = int(input("Edad: "))
        tipo_membresia = input("Tipo de membresía (Mensual/Anual): ")
        tipo_membresia = tipo_membresia.lower()
        print(tipo_membresia)
        while tipo_membresia != "mensual" and tipo_membresia != "anual" :
            print("Tipo de membresía inválido. Intente de nuevo.")
            tipo_membresia = input("Tipo de membresía (Mensual/Anual): ")
        miembros_ids.append(id_miembro)
        miembros_nombres.append(nombre_miembro)
        miembros_edades.append(edad_miembro)
        miembros_membresias.append(tipo_membresia)
        print("Miembro agregado exitosamente.")
        pass
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        print("Nro ID.\tNombre\tEdad\tTipo membresia")
        for i in range(len(miembros_ids)):
            print("{0}\t{1}\t{2}\t{3}".format(miembros_ids[i], miembros_nombres[i], miembros_edades[i], miembros_membresias[i]))
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        id_miembro = int(input("Ingrese el ID del miembro: "))
        if id_miembro in miembros_ids:
            indice = miembros_ids.index(id_miembro)
            tipo_membresia = input("Tipo de membresía (Mensual/Anual): ")
            tipo_membresia = tipo_membresia.lower()
            while tipo_membresia != "mensual" and tipo_membresia != "anual" :
                print("Tipo de membresía inválido. Intente de nuevo.")
                tipo_membresia = input("Tipo de membresía (Mensual/Anual): ")
            miembros_membresias[indice] = tipo_membresia
            print("Tipo de membresía actualizado exitosamente.")
        pass
    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        if len(miembros_ids) > 0:
            id_miembro = int(input("Ingrese el ID del miembro: "))
            if id_miembro in miembros_ids:
                indice = miembros_ids.index(id_miembro)
                print("Nro ID.\tNombre\tEdad\tTipo membresia")
                print("{0}\t{1}\t{2}\t{3}".format(miembros_ids[indice], miembros_nombres[indice], miembros_edades[indice], miembros_membresias[indice]))
        pass
    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        if len(miembros_edades) > 0:
            promedio_edad = sum(miembros_edades) / len(miembros_edades)
            print("El promedio de edad de los miembros es: {0}".format(promedio_edad))
    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        if len(miembros_edades) > 0:
            miembro_mayor = miembros_edades[0]
            miembro_menor = miembros_edades[0]
            
            for edad in miembros_edades:
                if edad > miembro_mayor:
                    miembro_mayor = edad
                if edad < miembro_menor:
                    miembro_menor = edad
            
            print("Nro ID.\tNombre\tEdad\tTipo membresia")
            for i in range(len(miembros_ids)):
                if miembros_edades[i] == miembro_menor:
                    print("{0}\t{1}\t{2}\t{3}".format(miembros_ids[i], miembros_nombres[i], miembros_edades[i], miembros_membresias[i]))
            for i in range(len(miembros_ids)):
                if miembros_edades[i] == miembro_mayor:
                    print("{0}\t{1}\t{2}\t{3}".format(miembros_ids[i], miembros_nombres[i], miembros_edades[i], miembros_membresias[i]))
        pass
    # Opcion 0: Salir
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")