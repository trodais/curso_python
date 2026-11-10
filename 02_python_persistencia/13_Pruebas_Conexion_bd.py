#Pruebas conexión bd
import mysql.connector as con 
db=con.connect(
  host="localhost", 
  user="root", 
  password="root", 
  port=3306, 
  database="universidad")

#El cursor permite enviar instrucciones SQL a la bd
cursordb=db.cursor(dictionary=True)
cursordb.execute("Select * from alumnos")
#Recorro las filas, contiene tuplas con todos los datos
for i in cursordb:
    print(i)
db.close()    
#Hay que cerrar la conexión

 