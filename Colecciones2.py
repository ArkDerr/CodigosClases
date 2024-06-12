""" #Lista
Lista = []

lista = [1,2,3]

#Tuplas

tupla = ()
tupla = tuple(lista)
print(tupla)

#Conjuntos
conjunto = {3,2,1,5,6,7} """

#Diccionarios

diccionario = {"nombre":"Juan Andres",
               "fonos": [988822222334,
                         9123213123,
                         92342524523],
                "activo":True}

""" print(diccionario["nombre"])
print(diccionario["fonos"])

mi_diccionario = {}

diccionario["nombre"] = "Pedro Pedro"

print(diccionario["nombre"])

del diccionario["fonos"]

print(diccionario)

print(diccionario.keys())

print(diccionario.values()) """

for clave in diccionario:
    print(clave, diccionario[clave])

for valor in diccionario.values():
    print(valor)