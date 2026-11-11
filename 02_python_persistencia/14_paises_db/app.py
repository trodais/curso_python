    #Utilizando los archivos de funciones definidos 
    #►borrara las tablas de la base de datos
    #►recuperara continentes y paises del json
    #►preparara datos obtenidos, para poder enviarlos a las funciones de la base de datos
    #►Llamará a las funciones para guardar continentes y guardar paises
     
import operaciones_bd as opbd
import operaciones_json as opjs
   
    
#Borrar las tablas de las base de datos
opbd.borrar_tablas()
    
#recuperara continentes y paises del json
continentes=opjs.continentes() #["Asia","Europe",etc]
opbd.crear_continentes(continentes)
continentes_bd=opbd.devolver_continentes() #[{"continente":"Asia","idContinente":3,....}]
paises=opjs.paises() #[{"name":"España","region":"Europe"}]
        
def obtener_idcontinente(continente):
    return [c["ideContinente"] for c in continentes_bd if c["nombre"]==continente][0]
   #Formateamos la lista de paises tal y como lo espera la función crear paises
paises_para_bd=[{"pais":p["name"],
                 "poblacion":p["population"],
                 "bandera":p["flags"]["png"],"idContinente":obtener_idcontinente(p["region"])} for p in paises]
opbd.crear_paises(paises_para_bd)
   
print("Datos almacenados!!!!")
     
   

