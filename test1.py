miLista = [1,2,3,4]
miLista.append("Dani")
miLista.insert(8,"Alan")
miLista.insert(9,"Ana")
miLista.append("Daniel")

for i in miLista:
    print(i)

matriz_sencilla = [
[1, 2, 3],
[4, 5, 6]
]
for elemento in matriz_sencilla:
	print(elemento)

arreglo_3D = [
[
[1, 2, 3],
[4, 5, 6],
],
[
[7, 8, 9],
[10, 11, 12],
],
[
[13, 14, 15],
[16, 17, 18],
]
]

for capa in arreglo_3D:
    for fila in capa:
        for elemento in fila:
	        print(elemento, end=' ')
        print()
    print()
