import os
os.system("cls")

# cine
def menu_general():
    os.system("cls")
    print("== MENU ==")
    print("1. Mostrar Sala")
    print("2. Comprar Entrada")
    print("3. Eliminar Entrada")
    print("4. Mostrar Ventas")
    print("5. Salir")

def elegir_opcion(max_opciones):
    while True:
        opcion = 0
        try:
            opcion = int(input("Seleccione una de las opciones disponibles >>"))
        except:
            pass
        if opcion < 1 or opcion > max_opciones:
            print("Opción no válida \n")
        else:
            return opcion

sala = [
    ['A1','A2','A3','A4','A5'],
    ['B1','B2','B3','B4','B5'],
    ['C1','C2','C3','C4','C5'],
    ['D1','D2','D3','D4','D5'],
    ['E1','E2','E3','E4','E5'],
]

todas_las_entradas = []
entradas_ocupadas = []

def imprimir_sala():
    print("\n== SALA 7 ==\n")
   
    print(f"ENTRADAS OCUPADAS : {entradas_ocupadas}")

    imprimir = ""

    for fila in sala:
        for asiento in fila:
            todas_las_entradas.append(asiento) # acá dejamos dentro del array todas las entradas

            imprimir += f"| {asiento} "
        imprimir += "|\n"    

    print(imprimir)

def comprar_entrada():
    entrada = input("Selecciona una de las entradas disponibles >> ")

    if entrada in todas_las_entradas and entrada not in entradas_ocupadas:
        print("ENTRADA ESTA DISPONIBLE")
        entradas_ocupadas.append(entrada)
    else:
        print("No es un asiento válido ")



salir = False
while not salir:
    menu_general()
    opcion = elegir_opcion(5)

    if opcion == 1:
        print("== SALA ==")
        imprimir_sala()
    elif opcion == 2:
        print("== Comprar entrada ==")
        imprimir_sala()
        comprar_entrada()
    elif opcion == 3:
        print("== Eliminar entrada ==")
    elif opcion == 4:
        print("== Mostrar Ventas ==")
    elif opcion == 5:
        print("== SALIR ==")
        salir = True
    else:
        print("Opción no disponible")

    input()