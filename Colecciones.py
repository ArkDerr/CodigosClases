listaNombres = []
menu1 = True
while menu1:
    print('[1]. Ingrese Nombre: ')
    print('[2]. salir')
    try:
        opc=int(input('--->>>'))
    except:
        print('la opcion ingresada no es valida')
    if opc == 1:
        nombre = input('Ingrese el nombre: ')
        listaNombres.append(nombre)
        print(listaNombres)
    else:
        menu1 = False



