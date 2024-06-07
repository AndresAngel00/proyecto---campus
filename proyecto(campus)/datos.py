import json
data={
"campers":[],
"trainer":[],
"coordinadores":[],
"areas":[],
"salones":[],
"Rutas":[],
"matriculas":[],
}
rut_archivos="db.json"
def guardar_usuario(data):
    global rut_archivos
    try:
        contenido=json.dumps(data,indent=4)
        with open(rut_archivos,"w")as file:
            file.write(contenido)
            print("los datos fueron guardados exitosamente")
    except Exception:
        print("los datos no fueron guardados")
        print("***********************************************")
    
def cargar_usuario():
    global rut_archivos
    global data
    try:
        with open (rut_archivos,"r")as file:
            data=json.load(file)
            print("los datos fueron cargados exitosamente")
    except  Exception:
        print("los datos no fueron cargados")
        print("***********************************************")
    



