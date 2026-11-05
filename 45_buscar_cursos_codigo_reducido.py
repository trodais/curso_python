#PARA CASA
# #Realizar una nueva versión del ejercicio 38_buscar_cursos 
#Lo mas reducido posible
 #### EJERCICIO DEL PROFESOR 
cursos=[
    {"denominacion":"Python y datos","calificaciones":[5.6,7.8,3.3,7.2],"fecha_fin":"10/03/2026"},
    {"denominacion":"Inglés científico","calificaciones":[8.2,7.8,6.3,4.2,9.0],"fecha_fin":"22/07/2026"},
    {"denominacion":"Spring e hibernate","calificaciones":[5.8,4.3,7.5],"fecha_fin":"04/12/2025"},
    {"denominacion":"Programador cerficado","calificaciones":[7.8,6.6,4.8,5.3,7.7],"fecha_fin":"30/09/2025"}  
]
#Nombre del curso con la nota media más alta
#Nombre del curso que finalizó antes
def media(numeros):
    suma=0
    for n in numeros:
        suma+=n
    return suma/len(numeros)
#Calcular la media con la función lambda
media_avg=lambda numeros:sum(numeros)/len(numeros)

def convertir_a_fecha(texto):
    return dt.datetime.strptime(texto,"%d/%m/%Y")
def curso_antes():
    nombre_curso=""
    fecha_antes=convertir_a_fecha(cursos[0]["fecha_fin"])
    for c in cursos:
        f=convertir_a_fecha(c["fecha_fin"])
        if f<fecha_antes:
            fecha_antes=f
            nombre_curso=c["denominacion"]
    
    return f"El curso más antiguo es {nombre_curso}"
    
def curso_media_mayor():
    nombre_curso=""
    media_alta=media(cursos[0]["calificaciones"])
    for c in cursos:
        m=media(c["calificaciones"])
        if m>media_alta:
            #actualizamos variables
            media_alta=m
            nombre_curso=c["denominacion"]
    
    return f"El curso con la media más alta es {nombre_curso}"
    
#llamadas a las funciones
st.write(curso_antes())
st.write(curso_media_mayor())
    
    
