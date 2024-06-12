def sumar(numerosSumar):
    resultadoSuma=0
    for i in range(numerosSumar):
        numero = int(input(f'ingrese el numero a sumar: '))
        resultadoSuma = resultadoSuma + numero
    return(resultadoSuma)

def sumar2():
    resultadoSuma=0
    cantnumSumar = int(input('Cuantos numeros desea sumar: '))
    for i in range(cantnumSumar):
        numero = int(input(f'ingrese el numero a sumar: '))
        resultadoSuma = resultadoSuma + numero
    print(f'La suma total de sus numeros es: {resultadoSuma}')

def Restar(numerosRestar):
    resultadoResta=0
    for i in range(numerosRestar):
        numero = int(input(f'ingrese el numero a Restar: '))
        if i == 0:
            resultadoResta = numero
        else:
            resultadoResta = resultadoResta - numero
    return(resultadoResta)

def Multiplicar():
    resultadoMulti = 1
    cantnumMulti = int(input('Cuantos numeros desea Multiplicar: '))
    for i in range(cantnumMulti):
        numero = int(input(f'ingrese el numero a multiplicar: '))
        resultadoMulti = resultadoMulti * numero
    return(resultadoMulti)

def Dividir(num1,num2):
    resultadodiv = float(num1 / num2)
    return(resultadodiv)
    

menu1=True

while menu1:
    print('##############Caluladora##############')
    print('Seleccion una de las siguientes opciones:')
    print('[1] Sumar')
    print('[2] Restar')
    print('[3] Multiplicar')
    print('[4] Dividir')
    print('[5] Salir')
    try:
        opc1 = int(input('--->>>'))

        if opc1 < 1 or opc1 > 5:
            print('Ingrese una opcion entre 1 y 5')

    except:
        print('Ingrese una opción valida')
    
    
    else:
        if opc1 == 1:
            #cantnumSumar = int(input('Cuantos numeros desea sumar: '))
            #print(f'La suma total de sus numeros es: {sumar(cantnumSumar)}')
            sumar2()
        elif opc1 == 2:
            print('Resta')
            cantnumRestar = int(input('Cuantos numeros desea restar: '))
            print(f'La resta total de sus numeros es: {Restar(cantnumRestar)}')
        elif opc1 == 3:
            print(f'La Multiplicación total de sus numeros es: {Multiplicar()}')
        elif opc1 == 4:
            num1=float(input('Ingrese el primer numero a dividir: '))
            num2=float(input('Ingrese el Segundo numero a dividir: '))
            if num2 == 0 or num1 == 0:
                print('No puede ingresar el valor cero.')
            else:
                print(f'La división es: {Dividir(num1,num2)}')
        elif opc1 == 5:
            print('Saliedo....')
            menu1 = False
 
