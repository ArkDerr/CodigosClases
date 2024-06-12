import datetime

dia = datetime.datetime.now().weekday()

match dia:
    case 0:
        dia='Lunes'
    case 1:
        dia='Martes'
    case 2:
        dia='Miercoles'
    case 3:
        dia='Jueves'
    case 4:
        dia='Viernes'
    case 5:
        dia='Sabado'
    case 6:
        dia='Domingo'

print(dia)