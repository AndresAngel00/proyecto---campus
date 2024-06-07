import datos
from menu_ges.gestion_camper import *
from menu_ges.gestion_trainer import *
from menu_ges.gestion_coordinador import *
from menu_ges.gestion_coordinador import *
from menu_coordi.matriculas import *
from menu_coordi.materias import *
from menu_coordi.rutas import *



def menu_():
    datos.cargar_usuario()
    while True:
        print("***********************************************")
        print("Bienvenido a campuslands:")
        print("1. Ingresar como camper:")
        print("2. Ingresar como trainer:")
        print("3. Ingresar como coordinador:")
        print("4. salir")
        print("***********************************************")
        opcion=0
        try:
            opcion=int(input("ingrese la opcion a escoger:"))
        except Exception:
            print("opcion invalida, por favor digite una de las opciones en el menu")
        if opcion == 1:
            menu_camper()
        elif opcion == 2:
            menu_trainer()
        elif opcion == 3:
            menu_coordinador()
        elif opcion == 4:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("opcion invalida, por favor digite una de las opciones en el menu")




#definiciones de los menus (camper,trainer,coordinador)
#opciones camper
def menu_camper():
    while True:
        print("***********************************************")
        print(" menu camper:")
        print("1.Mostrar los campers:")
        print("2.Registrar un camper nuevo:")
        print("3.Editar los datos del camper:")
        print("4.eliminar camper:")
        print("5.regresar al menu principal:")
        print("***********************************************")
        try:
            opcion=int(input("ingrese la opcion deseada:"))
        except ValueError:
            print("opcion invalida, por favor ingrese una opcion valida")
            continue
        if opcion == 1:
            mostrar_campers()
        elif opcion == 2:
            registros_campers()
        elif opcion == 3:
            actualiza_campers()
        elif opcion == 4:
            eliminar_campers()
        elif opcion ==5:
            break
        else:
            print("opcion incorrecta, por favor ingrese una de las opciones mostradas")

    #opciones trainer
def menu_trainer():
    while True:
        print("***********************************************")
        print(" menu trainer:")
        print("1.Mostrar los trainer:")
        print("2.Registrar un trainer:")
        print("3.Editar los datos del trainer:")
        print("4.regresar al menu principal:")
        print("***********************************************")
        try:
            opcion=int(input("ingrese la opcion deseada:"))
        except ValueError:
            print("opcion invalida, por favor ingrese una opcion valida")
            continue
        if opcion == 1:
            mostrar_trainers()
        elif opcion == 2:
            registros_trainer()
        elif opcion == 3:
            actualizar_trainer()
        elif opcion == 4:
            break
        else:
            print("opcion incorrecta,por favor ingrese una de las opciones mostradas")
def menu_coordinador():
    while True:
        print("***********************************************")
        print(" menu coordinador :)")
        print("1.menu materias-coordinador:")
        print("2.menu rutas-coordinador:")
        print("3.menu matriculas-coordinador:")
        print("4. menu notas-coordinador:")
        print("5.regresar al menu principal:")
        print("***********************************************")
        try:
            opcion=int(input("ingrese la opcion deseada:"))
        except ValueError:
            print("opcion invalida, por favor ingrese una opcion valida")
            continue
        if opcion == 1:
            menu_materias()
        elif opcion == 2:
            menu_rutas()
        elif opcion == 3:
            menu_matriculas()
        elif opcion == 4:
            menu_notas()
        elif opcion ==5:
            break
        else:
            print("opcion incorrecta, por favor ingrese una de las opciones mostradas")

#menu completo de coordinador(rutas,materias,matriculas,notas)

def menu_materias():
    while True:
        print("***********************************************")
        print(" menu materias-coordinador")
        print("1.Mostrar materias registradas:")
        print("2.Registrar una materia nueva:")
        print("3.Editar una materia existente:")
        print("4.eliminar materia:")
        print("5.regresar al menu principal:")
        print("***********************************************")
        try:
            opcion=int(input("ingrese la opcion deseada:"))
        except ValueError:
            print("opcion invalida, por favor ingrese una opcion valida")
            continue
        if opcion == 1:
            mostrar_materia()
        elif opcion == 2:
            registrar_materias()
        elif opcion == 3:
            actualizar_materia()
        elif opcion == 4:
            eliminar_materia()
        elif opcion ==5:
            break
        else:
            print("opcion incorrecta, por favor ingrese una de las opciones mostradas")

def menu_rutas():
    while True:
        print("***********************************************")
        print(" menu rutas-coordinador:")
        print("1.Mostrar rutas registradas:")
        print("2.Registrar una nueva ruta:")
        print("3.Editar una ruta existente:")
        print("4.eliminar ruta:")
        print("5.regresar al menu principal:")
        print("***********************************************")
        try:
            opcion=int(input("ingrese la opcion deseada"))
        except ValueError:
            print("opcion invalida, por favor ingrese una opcion valida")
            continue
        if opcion == 1:
            mostrar_rutas()
        elif opcion == 2:
            registrar_rutas()
        elif opcion == 3:
            actualizar_rutas()
        elif opcion == 4:
            eliminar_rutas()
        elif opcion ==5:
            break
        else:
            print("opcion incorrecta, por favor ingrese una de las opciones mostradas")

def menu_matriculas():
    while True:
        print("***********************************************")
        print(" menu matriculas-coordinador:")
        print("1.Mostrar matriculas registradas:")
        print("2.Registrar una nueva matricula:")
        print("3.Editar una matriucla existente:")
        print("4.eliminar matricula:")
        print("5.regresar al menu principal:")
        print("***********************************************")
        try:
            opcion=int(input("ingrese la opcion deseada:"))
        except ValueError:
            print("opcion invalida, por favor ingrese una opcion valida")
        if opcion == 1:
            mostrar_matriculas_registradas()
        elif opcion == 2:
            registrar_matricula()
        elif opcion == 3:
            editar_matricula()
        elif opcion == 4:
            eliminar_matricula()
        elif opcion ==5:
            break
        else:
            print("opcion incorrecta, por favor ingrese una de las opciones mostradas")
        
def menu_notas():
    while True:
        print("***********************************************")
        print(" menu notas-coordinador:")
        print("1.Mostrar notas registradas:")
        print("2.Registrar una nota nueva:")
        print("3.Editar una nota existente:")
        print("4.eliminar nota:")
        print("5.regresar al menu principal:")
        print("***********************************************")
        try:
            opcion=int(input("ingrese la opcion deseada:"))
        except ValueError:
            print("opcion invalida, por favor ingrese una opcion valida")
            continue
        if opcion == 1:
            mostrar_notas_registradas()
        if opcion == 2:
            registro_de_notas_nuevo()
        if opcion == 3:
            editar_notas_registradas()
        if opcion == 4:
            eliminar_notas_registradas()

        elif opcion ==5:
            break
        else:
            print("opcion incorrecta, por favor ingrese una de las opciones mostradas")


                






