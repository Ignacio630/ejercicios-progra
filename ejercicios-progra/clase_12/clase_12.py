# archivo = open('./texto.txt','r+')


# for line in archivo:
#     print(line, end="-")

# archivo.close()



import json 

data = {}

data["cliente"] = []
data["cliente"].append({"nombre":"juan","edad": 12})
data["cliente"].append({"nombre":"pedro","edad": 23})

with open('data.json','w') as file:
    
    json.dump(data,file,indent=4,ensure_ascii=False)
    
    # data = json.load(file)
    
    
    
    

def parse_json(nombre_archivo:str):
    lista_bzrp = []
    
    with open(nombre_archivo,"r") as archivo:
        dict = json.load(archivo)
        lista_bzrp = dict["bzrp"]

    
    return lista_bzrp
    
    
    
    
def generar_json(nombre_archivo:str,lista:list):
    data_json = {}
    dict["bzrp"] = lista
    
    with open(nombre_archivo,'w') as file:
        json.dump(data_json,file,indent=4,ensure_ascii=False)



def generar_csv(nombre_archivo:str, lista:list):
    with open (nombre_archivo, "w") as archivo:
        for video in lista:
            #Falta reemplazar comas
            mensaje = "{0},{1},{2},{3},{4},{5}\n"
            mensaje = mensaje. format(
            video["title"],
            video["views"],
            video["length"],
            video["img_url"],
            video["url"],
            video["date"])
            archivo.write(mensaje)