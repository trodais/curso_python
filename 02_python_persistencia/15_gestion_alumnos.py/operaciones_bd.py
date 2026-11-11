#Solo vamos a construir funciones con acceso a BD
import mysql.connector as con
def crear_conexion():
    return con.connect(host="localhost",
               user="root",
               password="root",
               port=3306,
               database="universidad")
def alta_alumnos(dni,nombre,email,curso,nota):
    sql_insert="insert into alumnos(dni,nombre,email,curso,nota) values(%s,%s,%s,%s,%s)"
    db=crear_conexion()
    cursor=db.cursor()
    valores=(dni,nombre,email,curso,nota)
    cursor.execute(sql_insert,valores)
    db.commit()
    db.close()
    print(f"Has introducido correctamente al alumno: D-{dni} N-{nombre} E-{email} C-{curso} N-{nota}")
    
    
    
    
    
    
    
        