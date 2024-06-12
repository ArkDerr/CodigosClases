""" def nombre_funcion():
    #instrucciones """

#Funcion Sin argumentos y sin retorno

def sinArgumenoSinRetorno():
    print("Hola soy una función")

sinArgumenoSinRetorno()

#Funcion Sin argumento pero con retorno

def sinArgumenoConRetorno():
    nun1=10
    nun2=65
    return(nun1+nun2)

print(f'La suma de la funcion es {sinArgumenoConRetorno()}')

#Funcion con argumentos y sin retorno

def conArgumentosSinretorno(numero1,numero2):
    suma = numero1+numero2
    print(f'La suma es {suma}')

varible1 = int(input('Ingrese el primer numero: '))
varible2 = int(input('Ingrese el segundo numero: '))
conArgumentosSinretorno(varible1,varible2)

#Con argumentos con retorno

def conArgumentosConretorno(numero1,numero2):
    resta = numero1-numero2
    return(resta)

varible3 = int(input('Ingrese el primer numero a restar: '))
varible4 = int(input('Ingrese el segundo numero a restar: '))

print(f'La resta es: {conArgumentosConretorno(varible3,varible4)} ')