import datos
def registrar_materias():
    materia={}
    def num_no(num_input):
        for i in datos.data["area"]:
            if i ["num"]==num_input:
                return False
            return True
        while True:
            num_input=input("escriba el numero de la materia:")
            if num_no(num_input):
                materia["num"]=num_input
                break
            else:
                print("ya esta registrado una materia")
                materia["nombre"]=input("ingrese el nombre de la materia")
                datos.data["area"].append(materia)
                datos.guardar_usuario(datos.data)
                print("Su materia fue registrada correctamente")

def mostrar_materia():
    print("estas son las materias que estan registradas")
    for materia in datos.data["area"]:
        print("num:",materia["num"],  "nombre:", materia["nombre"])

def actualizar_materia():
    areas=input("ingrese que materia quiere modificar:")
    for materia in datos.data["area"]:
        if materia["num"]==areas:
            materia["nombre"]=input("ingrese el nombre de la materia:")
            datos.guardar_usuario(datos.data)
            print("la materia fue actualizada")
            return
        print("no se encuentra una materia con ese nombre")

def eliminar_materia():
    areas=input("ingrese que materia quiere eliminar:")
    for materia in datos.data["area"]:
        if materia["num"]==areas:
            datos.data["area"].remove(materia)
            
            print("la materia fue eliminada correctamente")
        else:
            print("no se encuentra una materia con ese nombre")

        



    

