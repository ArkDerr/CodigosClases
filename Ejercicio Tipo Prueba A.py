valorentradamenores=2500
valorentradaadultos=5000
valorentradaadultomayor=1000

qentradamenores=0
qentradaadultos=0
qentradaadultomayor=0


menu1=True

while menu1:
    print('Seleccione una opción: ')
    print('[1] Iniciar compra')
    print('[2] Salir')
    compra=int(input('-->>'))

    if compra == 1:
        menu2=True
        diadescuento=int(input('Es viernes? Ingrese 1 [SI] / 2 [NO]'))
        while menu2:
            print('Seleccione el tipo de entrada: ')
            print(f'[1] Menores: 2500 / Cantidad: {qentradamenores}')
            print(f'[2] Adultos: 5000 / Cantidad: {qentradaadultos}')
            print(f'[3] Adulto Mayores: 1000 / Cantidad: {qentradaadultomayor}')
            print('[4] Pagar')
            print('[5] Anular Compra')
            print('[6] Salir')
            opcmenu2=int(input('-->>'))

            if opcmenu2 == 1:
                qentradamenores=int(input('Ingrese la cantidad de entradas: '))
            elif opcmenu2 == 2:
                qentradaadultos=int(input('Ingrese la cantidad de entradas: '))
            elif opcmenu2 == 3:
                qentradaadultomayor=int(input('Ingrese la cantidad de entradas: '))
            elif opcmenu2 == 4:
                if diadescuento == 1:
                    print('DESCUENTO')
                    totalpagar=(qentradamenores*valorentradamenores)+(qentradaadultos*valorentradaadultos)+(qentradaadultomayor*valorentradaadultomayor)
                    totalmenores=(qentradamenores*valorentradamenores)-((qentradamenores*valorentradamenores)*0.1)
                    totaladultos=qentradaadultos*valorentradaadultos
                    totaladultomayor=qentradaadultomayor*valorentradaadultomayor
                    totaldescuento=0
                    print('ENTRADAS')
                    print('--------------------------------')
                    print(f'{qentradamenores} entradas menores: ${totalmenores}')
                    print(f'{qentradaadultos} entradas menores: ${totaladultos}')
                    print(f'{qentradaadultomayor} entradas menores: ${totaladultomayor}')
                    print('--------------------------------')
                    print(f'Subtotal ${totalpagar}')
                    print(f'Descuento ${totaldescuento}')
                    print('--------------------------------')
                    print(f'Total a pagar ${totalpagar}')
                    print(f'Gracias por su compra')

                    qentradamenores=0
                    qentradaadultos=0
                    qentradaadultomayor=0
                else:
                    totalpagar=(qentradamenores*valorentradamenores)+(qentradaadultos*valorentradaadultos)+(qentradaadultomayor*valorentradaadultomayor)
                    totalmenores=qentradamenores*valorentradamenores
                    totaladultos=qentradaadultos*valorentradaadultos
                    totaladultomayor=qentradaadultomayor*valorentradaadultomayor
                    totaldescuento=0
                    print('ENTRADAS')
                    print('--------------------------------')
                    print(f'{qentradamenores} entradas menores: ${totalmenores}')
                    print(f'{qentradaadultos} entradas menores: ${totaladultos}')
                    print(f'{qentradaadultomayor} entradas menores: ${totaladultomayor}')
                    print('--------------------------------')
                    print(f'Subtotal ${totalpagar}')
                    print(f'Descuento ${totaldescuento}')
                    print('--------------------------------')
                    print(f'Total a pagar ${totalpagar}')
                    print(f'Gracias por su compra')

                    qentradamenores=0
                    qentradaadultos=0
                    qentradaadultomayor=0

            elif opcmenu2 == 5:
                qentradamenores=0
                qentradaadultos=0
                qentradaadultomayor=0
            else:
                menu2=False  
    else:
        menu1=False
