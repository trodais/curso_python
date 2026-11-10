#Pedir al usuario un presupuesto y el programa te da una lista de viviendas en función del presupuesto
#archivo house.csv
import csv,streamlit as st
dir_fichero="house.csv"

def posibles(presupuesto):
    with open(dir_fichero,"r") as f:
        todos=list(csv.DictReader(f))
    return [h for h in todos if h["price"]<=presupuesto]
    
    
    
presupuesto=st.text_input("Introduce tu presupuesto: ")
if st.button("Calcular"):

#CONSTRUYO UNA TABLA PARA LA VISUALIZACION DE DATOS
    col_size,col_habitaciones,col_antiguedad,col_ubicacion,col_precio=st.columns(5)
    col_size.write("**Tamaño**")
    col_habitaciones.write("**Habitaciones**")
    col_antiguedad.write("**Antiguedad**")
    col_ubicacion.write("**ubicacion**")    
    col_precio.write("**Precio**")    
    for i in posibles(presupuesto):
        col_size,col_habitaciones,col_antiguedad,col_ubicacion,col_precio=st.columns(5)
        col_size.write(i["size"])  
        col_habitaciones.write(i["rooms"])  
        col_antiguedad.write(i["age"])
        col_ubicacion.write(i["location"])
        col_precio.write(i["price"])
    
    
     

    
    




