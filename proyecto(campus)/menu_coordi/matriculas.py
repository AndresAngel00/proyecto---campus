
def mostrar_matriculas_registradas(matriculas):
    if not matriculas:  # Verifica si la lista de matrículas está vacía
        print("No hay matrículas registradas.")
    else:
        print("Matrículas registradas:")
    for matricula in matriculas:
        print(matricula)

def registrar_matricula(matriculas):
    nueva_matricula = input("Ingresa la nueva matrícula: ")
    matriculas.append(nueva_matricula)
    print("¡Matrícula registrada con éxito!")

def editar_matricula(matriculas):
    if not matriculas:
        print("No hay matrículas registradas para editar.")
        return

    print("Matrículas registradas:")
    for i, matricula in enumerate(matriculas):
        print(f"{i + 1}. {matricula}")

    opcion = input("Selecciona el número de la matrícula que deseas editar: ")
    try:
        indice = int(opcion) - 1
        if 0 <= indice < len(matriculas):
            nueva_matricula = input("Ingresa la nueva matrícula: ")
            matriculas[indice] = nueva_matricula
            print("¡Matrícula editada con éxito!")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Opción inválida.")

def eliminar_matricula(matriculas):
    if not matriculas:
        print("No hay matrículas registradas para eliminar.")
        return

    print("Matrículas registradas:")
    for i, matricula in enumerate(matriculas):
        print(f"{i + 1}. {matricula}")

    opcion = input("Selecciona el número de la matrícula que deseas eliminar: ")
    try:
        indice = int(opcion) - 1
        if 0 <= indice < len(matriculas):
            matricula_eliminada = matriculas.pop(indice)
            print(f"¡Matrícula {matricula_eliminada} eliminada con éxito!")
        else:
            print("Opción inválida.")
    except ValueError:
        print("Opción inválida.")




    








