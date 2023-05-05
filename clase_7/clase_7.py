#15

lista_peliculas = [{"titulo": 'Los vengadores', "genero": "Accion", "director":"Hermanos Russo"}, {"titulo": 'Los indestructibles', "genero": "Accion", "director":"Hermanos Russo"}, {"titulo": 'titanic', "genero": "drama", "director":"Hermanos Russo"}]

def peliculas_por_genero(lista_peliculas):
    dict_contador_genero = {}
    for pelicula in lista_peliculas:
        genero = pelicula["genero"]
        titulo = pelicula["titulo"]
        if genero in dict_contador_genero:
            aux_lista = dict_contador_genero[genero]
            aux_lista.append(titulo)
        else:
            aux_lista = []
            aux_lista.append(titulo)
            dict_contador_genero[genero] = aux_lista
    return dict_contador_genero    
        
result = peliculas_por_genero(lista_peliculas)

for key in result:
    print(len(result[key]))
    print(result[key])