import datos
def registros_campers():
    camper={}
    camper["cedula"]=input("Ingrese la cedula del camper:")
    def cedula_existe(cedula):
        
        "Verifica si una cédula ya existe en la lista de cédulas registradas."

        
        if cedula_existe in cedula:
            return True
        else:
            return False
        
    camper["nombres"]=input("Ingrese el nombre del camper:")
    camper["apellidos"]=input("Ingrese los apellidos del camper:")
    camper["direccion"]=input("Ingrese la direccion del camper:")
    camper["acudiente"]=input("Ingrese el nombre del acudiente del camper:")
    camper["numero de celular"]=input("Ingrese el numero del camper:")

    datos.data["campers"].append(camper)
    datos.guardar_usuario(datos.data)
    print("Camper registrado con exito")

def mostrar_campers():
        print("estos son los campers que estan registrados:")
        for camper in datos.data["campers"]:
            print("cedula", camper["cedula"],"nombres",camper["nombres"],"apellidos",camper["apellidos"],"direccion",camper["direccion"],"acudiente",camper["acudiente"],"numero de celular",camper["numero de celular"])
def actualiza_campers():
    camper_cedula=input("ingrese el numero de cedula del camper que quiere modificar:")
    for camper in datos.data["campers"]:
        if camper["cedula"]==camper_cedula:
                camper["nombres"]=input("Ingrese el nombre del camper:")
                camper["apellidos"]=input("Ingrese los apellidos del camper:")
                camper["direccion"]=input("Ingrese la direccion del camper:")
                camper["acudiente"]=input("Ingrese el nombre del acudiente del camper:")
                camper["numero de celular"]=input("Ingrese el numero del camper:")
                datos.guardar_usuario(datos.data)
                print("los datos han sido actualizados correctamente")
        return
    print("no se encontro el camper con la cedula ingresada")

def eliminar_campers():
    camper_cedula=input("ingrese la cedula del camper que desea eliminar:")
    for camper in datos.data["campers"]:
        if camper["cedula"]==camper_cedula:
              datos.data["campers"].remove(camper)
              datos.guardar_usuario(datos.data)
              print("el camper ha sido eliminado correctamente")
              return
        print("no se encontro el camper con la cedula ingresada")


                     

              


        
    


