import streamlit as st 
import time 
mensaje=st.error("Se ha producido un error") 
st.success("Operación realizada correctamente") 
st.warning("Atención") 
st.info("Información adicional") 
time.sleep(3) 
mensaje.empty() #desaparece a los tres segundos la variable del mensaje
st.toast("ESTO ES UNA TOSTADA",duration="long") #esto es un mensaje flotante que desaparece


