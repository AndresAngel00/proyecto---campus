import datos
def registros_trainer():
    trainer={}
    trainer["cedula"]=input("Ingrese la cedula del trainer:")
    def cedula_existe(cedula):
        
        "Verifica si una cédula ya existe en la lista de cédulas registradas."

        if cedula_existe in cedula:
            return True
        else:
            return False
        
    trainer["nombres"]=input("Ingrese el nombre del trainer:")
    trainer["apellidos"]=input("Ingrese los apellidos del trainer:")
    trainer["direccion"]=input("Ingrese la direccion del trainer:")
    trainer["acudiente"]=input("Ingrese el nombre del acudiente del trainer:")
    trainer["numero de celular"]=input("Ingrese el numero del trainer:")

    datos.data["trainers"].append(trainer)
    datos.guardar_usuario(datos.data)
    print("trainer registrado con exito")

def mostrar_trainers():
    print("estos son los trainers registrados en campuslands:")
    for trainer in datos.data["trainer"]:
        print("cedula", trainer["cedula"],"nombres",trainer["nombres"],"apellidos",trainer["apellidos"],"direccion",trainer["direccion"],"acudiente",trainer["acudiente"],"numero de celular",trainer["numero de celular"])
def actualizar_trainer():
    trainer_cedula=input("ingrese el numero de cedula del trainer que quiere modificar")
    for trainer in datos.data["trainer"]:
        if trainer["cedula"]==trainer_cedula:
            trainer["nombres"]=input("Ingrese el nombre del trainer:")
            trainer["apellidos"]=input("Ingrese los apellidos del trainer:")
            trainer["direccion"]=input("Ingrese la direccion del trainer:")
    import re
    
    while True:
            numero_input = input("Escriba el número del trainer: ")
            if re.match(r'^[0-9]+$', numero_input):
                trainer["trainer"] = numero_input
                print("Número de trainer registrado correctamente.")
                break
            else:
                print("el numero celular debe tener solo numeros:")
            datos.guardar_usuario(datos.data)
            print("los datos han sido actualizados correctamente")
            return
    print("no se encontro el trainer con la cedula ingresada")

def eliminar_trainer():
    trainer_cedula=input("ingrese la cedula del trainer que desea eliminar:")
    for trainer in datos.data["trainer"]:
        if trainer["cedula"]==trainer_cedula:
              datos.data["trainer"].remove(trainer)
              datos.guardar_usuario(datos.data)
              print("el trainer ha sido eliminado correctamente")
              return
         
             