import os
import time
os.system('cls')

#Cantidad de productos 
can_tarta_manzana=0
can_cheesecake_frambuesa=0
can_pastel_chocolate=0
can_galleta_avena=0
can_macarons=0

#impresion boleta y descuentos 
total_productos=0
descuento=0
des_adicional=0
subtotal=0
total=0
anular=0
nom_descuento=''

menu_general=True
while menu_general:
    print('==========Dulces Encantos==========')
    print (f'[1] Tarta manzana \t\t$ 8000 [{can_tarta_manzana}]')
    print (f'[2] cheesecake frambuesa \t$ 9000 [{can_cheesecake_frambuesa}]')
    print (f'[3] Paste chocolate \t\t$ 7500 [{can_pastel_chocolate}]')
    print (f'[4] Galletas avena \t\t$ 5000 [{can_galleta_avena}]')
    print (f'[5] Macarons docena \t\t$ 12000 [{can_macarons}]')
    print ('[6] Anular pedido')
    print ('[7] Pagar')
    opc_general=0
    try:
        opc_general = int(input('Ingrese las opciones que desee levar >>>:'))
    except:
        print('La opción debe ser numerica')
    if opc_general <1 or opc_general >7:
        print('La opcion ingresada no es correcta. Intente nuevamente')
        time.sleep (3)
        os.system ('cls')
    else: 
        if opc_general==1:
            try:
                can_tarta_manzana += int(input('Ingrese la cantidad tartas de manzana que desea llevar'))
            except:
                print('La opción debe ser numerica')
        elif opc_general==2:
            try:
                can_cheesecake_frambuesa += int(input('Ingrese la cantidad de cheescake de frambuesa que desea llevar'))
            except:
                print('La opción debe ser numerica')
        elif opc_general==3:
            try:
                can_pastel_chocolate += int(input('Ingrese la cantidad de Pastel chocolate que desea llevar'))
            except:
                print('La opción debe ser numerica')
        elif opc_general==4:
            try:
                can_galleta_avena += int(input('Ingrese la cantidad de Galletas de avena que desea llevar'))
            except:
                print('La opción debe ser numerica')
        elif opc_general==5:
            try:
                can_macarons += int(input('Ingrese la cantidad de docenas de macarons que desea llevar'))
            except:
                print('La opción debe ser numerica')
        elif opc_general==6:
            try:
                anular = int(input('¿Esta seguro que quiere anular compra \n [1] si \n[2] no \n >>>:'))
                if anular:
                    print('Su pedido ha sido anulado')
                    time.sleep(3)
                    os.system('cls')
                    menu_general=False
            except:
                print('La opción debe ser numerica')
                
        elif opc_general==7:
            total_productos= can_cheesecake_frambuesa + can_galleta_avena + can_macarons + can_pastel_chocolate + can_tarta_manzana
            if total_productos==0:
                print('Si no ha comprado no puede realizar el pago')
                time.sleep(3)
                os.system("cls")
            else:
                menu_descuento=True
                while menu_descuento:
                    os.system('cls')
                    print('==========MENU DESCUENTO==========')
                    print('[1] Cliente premium \t% 20')
                    print('[2] Estudiante \t\t% 15')
                    print('[3] No posee descuentos')
                    opc_descuento=0
                    try:
                        opc_descuento = int(input('Elija la opción correspondiente >>>:'))
                    except:
                        print('La opción debe ser numerica')
                    if opc_descuento < 1 or opc_descuento > 3:
                        print('La opción ingresada no correcta. Intente nuevamente')
                        time.sleep(3)
                        os.system('cls')
                    else: 
                        if opc_descuento == 1:
                            nom_descuento='Cliente premium'
                            descuento = 20
                        elif opc_descuento==2:
                            nom_descuento='Estudiante'
                            descuento= 15  
                        else:
                            nom_descuento= 'No posee descuento'
                            descuento = 0

                        subtotal= can_tarta_manzana*8000 + can_cheesecake_frambuesa*9000 + can_pastel_chocolate*7500 + can_galleta_avena*5000 + can_macarons*12000


                        if subtotal > 20000:
                            des_adicional=10
                            print('Descuento adicional \t% 10')
                        else: 
                            print('Opcion no disponible')

                        porcentaje_descuento=round(subtotal*descuento/100)
                        porcentaje_descuento_adicional=round(subtotal*des_adicional/100)

                        print('===================================================')
                        print(f'Total productos \t {total_productos}')
                        print('===================================================')
                        if can_tarta_manzana >0:
                            print(f'{can_tarta_manzana} Tarta manzana \t\t$ {can_tarta_manzana*8000}')
                        if can_cheesecake_frambuesa >0:
                            print(f'{can_cheesecake_frambuesa} Cheesecake frambuesa\t$ {can_cheesecake_frambuesa*9000}')
                        if can_pastel_chocolate >0:
                            print(f'{can_pastel_chocolate} Pastel chocolate \t\t$ {can_pastel_chocolate*7500}')
                        if can_galleta_avena >0:
                            print(f'{can_galleta_avena} Galleta avena\t\t$ {can_galleta_avena*5000}')
                        if  can_macarons >0:
                            print(f'{can_macarons} Docena macarons\t\t$ {can_macarons*12000}')
                            print('===================================================')
                            print(f'SUBTOTAL: \t\t\t\t$ {subtotal}')
                            print(f'Descuento: {descuento} % {nom_descuento} \t$ {int(subtotal*descuento/100)}') 
                            print(f'Descuento adicional 10% \t\t {subtotal*des_adicional/100} ')
                            print('===================================================')
                        total = (subtotal-(porcentaje_descuento))-(porcentaje_descuento_adicional)
                        print(f'Total \t\t\t$ {total}')
                        print('====================================================')
                        print('Gracias por su compra :D')
                        time.sleep(3)
                        menu_general=False
                        menu_descuento=False
                   
                                                




