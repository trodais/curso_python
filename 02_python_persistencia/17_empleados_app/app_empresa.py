"""
-Alta de nuevos empleados
-Filtrar empleados: opcion por departamento o rango salarial.
Si se elige departamento, se muestra combo con departamentos y al
seleccionar uno muestra empleados. Si selige rango salarial,
aparecen dos campos de textos (min y max) y un botón que al pulsarlo
muestra empleados 
"""
import empleados_repositorio as repo
import streamlit as st

st.title("Gestión de Empleados")

tab_nuevo,tab_filtro=st.tabs(["Nuevo empleado","Busqueda de empleados"])


with tab_nuevo:
    empleado=st.text_input("Nombre del empleado: ")
    edad=st.number_input("Edad del empleado: ")
    salario=st.number_input("Salario del empleado: ")
    departamento=st.text_input("Departamento del empleado: ")
    if st.button("Alta empleado"):
        repo.nuevo_empleado(empleado,edad,salario,departamento)
        st.toast("Empleado agregado!!") 
        
        
with tab_filtro:
    
    opcion = st.radio("Elige una opción:",(['Por departamento','por rango salarial']))
    
    if opcion=="Por departamento":
        departamentos=st.selectbox("**Elije un departamento**",repo.departamentos())
        repo.empleados_por_departamento(departamentos)
        col_empleado, col_edad, col_salario, col_departamento = st.columns([2, 1, 3, 4], vertical_alignment="center")
        col_empleado.markdown("**Empleado**")
        col_edad.markdown("**edad**")
        col_salario.markdown("**Salario**")
        col_departamento.markdown("**Departamento**")
        st.table(repo.empleados_por_departamento(departamentos))  
        st.write("Esto es con dataframe")          
        st.dataframe(repo.empleados_por_departamento(departamentos))
    else:
    
        st.write("Esta es la opción de buscar por rango salarial")
    
            

        





