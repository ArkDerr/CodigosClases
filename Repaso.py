#Tipos de datos en variables:
#Entero:
entero=18

#Flotante
flotante=3.1

#Boleano
boleano1=True
boleano1=False

#String
caracter='Juan'

#Mostrar en pantalla / imprimir / Listar
print('Hola mundo')
print(entero)
print(caracter)
print(boleano1)
print(1234)

#saltos de linea
print('Hola,\nJuan.')

print("""Hola,
      Juan.""")

#Concatenar
print("Tu nombre es ",caracter)
print("Tu nombre es "+caracter)
print("Tu edad es ",entero)
print("Tu edad es "+str(entero))
print(f'Tu nombre es {caracter}')

#tabular
print('Hola,\tJuan.')

#Redondear
redondear1=round(3.615)
print(redondear1)

redondear2=round(3.6156,3)
print(redondear2)

#If (SI) ELIF ELSE
variableif=15

if (variableif==14):
    print("Igual a 14")
elif (variableif==15):
    print("Primer elif")
elif (variableif<16):
    print("Segundo elif")
else:
   print("No se cumple") 

if (variableif==14):
    print("X Igual a 14")
if (variableif==15):
    print("X Primer elif")
if (variableif<16):
    print("X Segundo elif")

#Capturar datos por teclado (str)
""" variablecaptura=input('Ingrese el texto: ')
print(variablecaptura) """

#Convertir a int
""" variablecaptura2=int(input('Ingrese el numero: '))
print(variablecaptura2) """

#try/except While
""" iterador=1

while iterador<3:
    try:
        variablecaptura3=int(input('Ingrese el numero: '))
        print(variablecaptura3)
        iterador=10
    except:
        print('El valor ingresado no es un numero') """

#for
for i in range(10):
    print(i)

for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

for i in range(11,1,-1):
    print(i)