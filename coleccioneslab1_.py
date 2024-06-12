import os
import time

alumnos = []
rut = 0
nombre = ""
direccion = ""
fono = 0
cant_alumnos = 0
mantenedor = True

while mantenedor:
    print("-----Mantenedor de Alumnos-----")
    print("[1] Ingresar Alumno")
    print("[2] Listar Alumnos")
    print("[3] Buscar Alumno")
    print("[4] Eliminar Alumno")
    print("[5] Salir")
    opc1=0

    try:
        opc1 = int(input("-->> "))
    except:
        os.system('cls')
        print("Ingrese una opción valida")
    
    if opc1 == 1:
        cant_alumnos = len(alumnos)
        if cant_alumnos <= 30:
            try:
                rut = int(input("Ingrese el rut del alumno: "))
            except:
                os.system('cls')
                print("Ingrese una opción valida")
                print("")
                print("")
                time.sleep(2)
            try:
                nombre = input("Ingrese el Nombre del alumno: ")
            except:
                os.system('cls')
                print("Ingrese una opción valida")
                print("")
                print("")
                time.sleep(2)
            try:
                direccion = input("Ingrese la dirección del alumno: ")
            except:
                os.system('cls')
                print("Ingrese una opción valida")
                print("")
                print("")
                time.sleep(2)
            try:
                fono = int(input("Ingrese el Fono del alumno: "))
            except:
                os.system('cls')
                print("Ingrese una opción valida")
                print("")
                print("")
                time.sleep(2)

            alumno = [rut, nombre, direccion, fono]
            alumnos.append(alumno)
            os.system('cls')
            print("")
            print("")
            print("Se agrego el alumno")
            time.sleep(2)
            os.system('cls')
        else:
            print("Curso Completo")
    elif opc1 == 2:
        os.system("cls")
        print("")
        print("")
        if len(alumnos) > 0:
            for alumno in alumnos:
                print(f'Rut: {alumno[0]}, Nombre: {alumno[1]}, Dirección: {alumno[2]}, Fono: {alumno[3]}')
        else:
            os.system('cls')
            print("")
            print("")
            print("No se tienen datos de alumnos")
            time.sleep(2)
            os.system('cls')
        print("")
        print("")
        time.sleep(2)
    elif opc1 == 3:
        rut = int(input("Ingrese el rut del alumno que busca: "))
        encontrado = 0
        for alumno in alumnos:
            if alumno[0] == rut:
                print(f'Rut: {alumno[0]}, Nombre: {alumno[1]}, Dirección: {alumno[2]}, Fono: {alumno[3]}')
                encontrado = 1
                break
        if encontrado == 0:
            print("No hay un alumno con ese rut")
            print("")
            print("")
            time.sleep(2)
    elif opc1 == 4:
        rut = int(input("Ingrese el rut del alumno que quiere eliminar: "))
        indice = 0
        encontrado = 0
        for alumno in alumnos:
            if alumno[0] == rut:
                del alumnos[indice]
                encontrado = 1
                print("Alumno Eliminado")
                break
            indice += 1
        if encontrado == 0:
            print("No hay un alumno con ese rut para eliminar")
            print("")
            print("")
            time.sleep(2)
    elif opc1 == 5:
        mantenedor = False
        os.system('cls')
        print("")
        print("")
        print("Hasta Luego!!!")
        time.sleep(2)
        os.system('cls')





