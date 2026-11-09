import streamlit as st

tab1,tab2=st.tabs("[Alta,"Consulta]")

with tab1:
nombre=st.text_input("introduce tu nombre")
edad=st.number_input("introduce tu edad",value=0)
afiliados=st.checkbox("Afiliado")
curso=st.radio("Elije curso:",["Python","C++","Java"])
centro=st.selectbox("centro: ",["Leganés","Getafe","Alcorcón"])

if st.button("ACEPTAR"):
    st.success(f"Has aceptado una clausula infinita: nombre: {nombre} edad: {edad} curso: {curso} centro: {centro}")
    
wiht tab2:
import streamlit as st 
aula = [ 
    {"id": 1, "nombre": "Juan", "edad": 25}, 
    {"id": 2, "nombre": "Ana", "edad": 30}, 
    {"id": 3, "nombre": "Pedro", "edad": 22} 
] 
st.table(aula) 
    
