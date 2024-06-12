import os
import math

menu1=True
while menu1:
    print(f'[1] Ingresar cotización')
    print(f'[2] Cerrar programa')
    try:
        opc1=int(input('Ingrese la opción-->>'))
        if opc1==1:
            os.system('cls')
            validarnombre=True
            while validarnombre:
                nombre=input('Ingrese el nombre del cliente: ')
                largo_nombre=len(nombre)
                if largo_nombre < 3:
                    print(f'El nombre debe contener minimo 3 caracteres')
                else:
                    validarnombre=False
            validarTelefono=True
            while validarTelefono:
                fono=input('Ingrese el Fono del cliente: ')
                largo_fono=len(fono)
                if largo_fono < 8 or largo_fono > 9:
                    print(f'El fono debe contener entre 8 y 9 digitos')
                else:
                    validarTelefono=False
            validarDimensiones=True
            while validarDimensiones:
                alto=int(input('Ingrese el alto de la caja [cm]: '))
                ancho=int(input('Ingrese el ancho de la caja [cm]: '))
                largo=int(input('Ingrese el largo de la caja [cm]: '))
                if alto == 0 or ancho == 0 or largo == 0:
                    print(f'Las dimensiones deben ser mayor a cero')
                else:
                    validarDimensiones=False
            validarCaja=True
            while validarCaja:
                qcajas=int(input('Ingrese el numero de cajas: '))
                if qcajas <= 0:
                    print(f'Las cajas deben ser mayor a cero')
                else:
                    validarCaja=False
            
            volumencaja=(alto/100)*(ancho/100)*(largo/100)
            volumentotal=volumencaja*qcajas
            numerocamiones=math.ceil(volumentotal/29)
            preciotransporte=numerocamiones*150000

            print(f'Cliente: “{nombre}”.')
            print(f'Teléfono: {fono}')
            print(f'Cantidad de cajas transportadas {qcajas}')
            print(f'Camiones: {numerocamiones}')
            print(f'Valor total: ${preciotransporte:,}')

        elif opc1==2:
            menu1=False
            print(f'Gracias por usar el programa')
        else:
            os.system('cls')
            print(f'La opción ingresada no es valida. Ingrese la opción correcta.')
    except:
        os.system('cls')
        print(f'La opción ingresada no es valida. Ingrese la opción correcta.')