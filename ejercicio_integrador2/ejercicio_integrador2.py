lista_miembros = {"id": 12, "nombre": "Juan", "edad": 25, "tipo_membresia": "Anual",
                  "id": 13, "nombre": "Ana", "edad": 30, "tipo_membresia": "Mensual",
                  "id": 14, "nombre": "Pedro", "edad": 20, "tipo_membresia": "Anual",
                  "id": 15, "nombre": "Maria", "edad": 35, "tipo_membresia": "Mensual",
                  "id": 16, "nombre": "Luis", "edad": 40, "tipo_membresia": "Anual",}

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
        
        pass
    # Opción 2: Mostrar la informacion de todos los miembros
    elif opcion == "2":
        print("Nro ID.\tNombre\tEdad\tTipo membresia")
    # Opción 3: Actualizar el tipo de membresía de un miembro
    elif opcion == "3":
        pass
    # Opción 4: Buscar información de un miembro
    elif opcion == "4":
        pass
    # Opción 5: Calcular el promedio de edad de los miembros
    elif opcion == "5":
        pass
    # Opción 6: Buscar el miembro más joven y el más viejo
    elif opcion == "6":
        pass
    # Opcion 0: Salir
    elif opcion == "0":
        break
    else:
        print("Opción inválida. Intente de nuevo.")