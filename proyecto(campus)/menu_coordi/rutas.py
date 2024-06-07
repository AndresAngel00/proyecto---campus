import datos

def registrar_rutas():
    ruta={}
    def num_no(num_input):
        for i in datos.data["rutas"]:
            if i ["ruta"]==num_input:
                return False
            return True
        while True:
            num_input=input("escriba el numero de la ruta:")
            if num_no(num_input):
                ruta["ruta"]=num_input
                break
            else:
                print("ya esta registrado una ruta")
                ruta["nombre"]=input("ingrese el nombre de la ruta")
                datos.data["rutas"].append(ruta)
                datos.guardar_usuario(datos.data)
                print("Su ruta fue registrada correctamente")

def mostrar_rutas():
    print("estas son las rutas que estan registradas")
    for ruta in datos.data["rutas"]:
        print("ruta:",ruta["ruta"],  "nombre:", ruta["nombre"])

def actualizar_rutas():
    rutas=input("ingrese que ruta quiere modificar:")
    for ruta in datos.data["rutas"]:
        if ruta["ruta"]==rutas:
            ruta["nombre"]=input("ingrese el nombre de la ruta:")
            datos.guardar_usuario(datos.data)
            print("la ruta fue actualizada")
            return
        print("no se encuentra una ruta con ese nombre")

def eliminar_rutas():
    rutas=input("ingrese que ruta quiere eliminar:")
    for ruta in datos.data["rutas"]:
        if ruta["ruta"]==rutas:
            datos.data["rutas"].remove(ruta)
            
            print("la ruta fue eliminada correctamente")
        else:
            print("no se encuentra una ruta con ese nombre")



