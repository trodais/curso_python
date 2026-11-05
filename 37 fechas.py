import datetime as dt
print(f"Fecha de hoy {dt.date.today()}")
print(f"Hora actual: {dt.datetime.now()}")
#print(f"Hora actual: {datetime.datetime.time()}")
f_posterior=dt.datetime.now()+dt.timedelta(days=20,hours=60)
print(f_posterior)

fechahora_actual=dt.datetime.now()
#para presentar formato de fecha
print(f"La fecha y hora actuales {dt.datetime.strftime(fechahora_actual,'%d/%m/%Y - %H:%M')}")

#PARSEADO para convertir texto en fechas
fecha1="10/11/2003"
fecha2="25/04/2002"

fec1=dt.datetime.strptime(fecha1,"%d/%m/%Y")
fec2=dt.datetime.strptime(fecha2,"%d/%m/%Y")
if fec1<=fec2:
    print(f"La mas antigua es: {fec1}")
else:
    print(f"La mas antigua es: {fec2}")    

