from math import e
import datos
def registro_de_notas_nuevo():
    camper_cedula=input("Ingresa la cedula del camper:")
    for camper in datos.data["camper"]:
        if camper["cedula"]==camper_cedula:
            try:
                nota1=float(input("ingrese la nota teorica del camper"))
                nota2=float(input("ingrese la nota practica del camper"))    
                if 0 <= nota1 <=100 and 0 <= nota2 <=100:
                    promedio_camper=(nota1*0.3)+(nota2*0.7)
                    camper["promedio"]=promedio_camper
                    if promedio_camper >=60:
                        camper["estado del camper"]="aprobado"
                    else:
                        camper["estado del camper"]="Reprobado"
                    datos.guardar_usuario(datos.data)
                    print(f"las notas fueron registradas y el estado del camper se actualizo a {camper['Estado']}")
                else:
                    print(".")
            except ValueError:
                print("error, por favor ingrese un numero.")
            return
        print("no se encuentra un camper registrado con ese documento.")

        
def mostrar_notas_registradas():
    for estudiante in datos.data["matricula"]:
        print("Número de matrícula:", estudiante["numero"])
        print("Nota teórica:", estudiante["nota_teoria"])
        print("Nota práctica:", estudiante["nota_practica"])
        print("------------------------")
        
def eliminar_notas_registradas(numero_matricula):
    for estudiante in datos.data["matricula"]:
        if estudiante["numero"] == numero_matricula:
            estudiante["nota_teoria"] = None
            estudiante["nota_practica"] = None
            print(f"Notas eliminadas para el estudiante con número de matrícula {numero_matricula}")
            return
    print(f"No se encontraron notas para el estudiante con número de matrícula {numero_matricula}")
    

def editar_notas_registradas(numero_matricula):
    for estudiante in datos.data["matricula"]:
        if estudiante["numero"] == numero_matricula:
            try:
                nueva_nota_teoria = float(input("Ingrese la nueva nota teórica: "))
                nueva_nota_practica = float(input("Ingrese la nueva nota práctica: "))
                estudiante["nota_teoria"] = nueva_nota_teoria
                estudiante["nota_practica"] = nueva_nota_practica
                print("Notas actualizadas correctamente.")
                return
            except ValueError:
                print("Error: Ingrese un valor numérico válido para las notas.")
    print(f"No se encontraron notas para el estudiante con número de matrícula {numero_matricula}.")



        
                    
                    


                    


