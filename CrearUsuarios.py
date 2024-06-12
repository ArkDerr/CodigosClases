import datetime

fecha_actual = datetime.datetime.now()

UserAdmin= 'admin'
PassAdmin= 'admin'
usuariosCreados=0

user1='NULL'
user2='NULL'
user3='NULL'
pass1='NULL'
pass2='NULL'
pass3='NULL'

iterador2=True

while iterador2:

    user=input('Ingrese su Usuario:')
    password=input('Ingrese su Contraseña:')

    if user == UserAdmin and password == PassAdmin:
        iterador1=True
        while iterador1:
            print(f'Seleccione una opcion:')
            print(f'1.- Ingresar nuevo usuario')
            print(f'2.- Listar Usuarios')
            print(f'3.- Salir')
            opc1=int(input('-->>'))
            if opc1 == 1:
                print(f'Los usuarios creados son: {usuariosCreados}')
                if usuariosCreados < 4:
                    opc2=input('Desea crear un nuevo usuario [Ingrese si o no]:')
                    if opc2 == 'si':
                        if user1 == 'NULL':
                            user1=input('Ingrese el nombre del nuevo usuario: ')
                            pass1=input('Ingrese la password para el usuario: ')
                            usuariosCreados=1
                        elif user2 == 'NULL':
                            user2=input('Ingrese el nombre del nuevo usuario: ')
                            pass2=input('Ingrese la password para el usuario: ')
                            usuariosCreados=2
                        elif user3 == 'NULL':
                            user3=input('Ingrese el nombre del nuevo usuario: ')
                            pass3=input('Ingrese la password para el usuario: ')
                            usuariosCreados=3
                        else:
                            print(f'El maximo de usuarios ya estan creados')
            elif opc1 == 2:
                print(f'User1: {user1} / pass: {pass1}')
                print(f'User2: {user2} / pass: {pass2}')
                print(f'User3: {user3} / pass: {pass3}')
            elif opc1 == 3:
                iterador1 = False

    elif user == user1 and password == pass1:
        print(f'Hola {user1}, la hora es {fecha_actual} ')
    elif user == user2 and password == pass2:
        print(f'Hola {user1}, la hora es {fecha_actual} ')
    elif user == user3 and password == pass3:
        print(f'Hola {user1}, la hora es {fecha_actual} ')
    else:
        print(f'***Su usuario y/o Contraseña es incorrecta***')