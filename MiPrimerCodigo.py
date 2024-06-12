#importar modulo
import os

#Usando una funcion del modulo os
os.system("cls")

user="Admin"
password=12345

UserIngresado = input("Ingrese su usuario: ")
PassIngresada = int(input("Ingrese la password: "))

if user == UserIngresado or password == PassIngresada:
    print("Puede ingresar al sistema")
else:
    print("Usted no ingreso los datos correctos")
