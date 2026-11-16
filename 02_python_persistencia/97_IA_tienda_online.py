import streamlit as st
import json

# 1. Inicializar el carrito de compras en la memoria de la sesión si no existe
if "carrito" not in st.session_state:
    st.session_state.carrito = []

def todos_productos(producto):
    with open("productos_informatica.json", "r", encoding="utf-8") as f:
        return list(filter(lambda p: p["nombre_producto"] == producto, json.load(f)))

def productos():
    with open("productos_informatica.json", "r", encoding="utf-8") as f:
        return list(set(map(lambda p: p["nombre_producto"], json.load(f))))

st.title("🛒 Tienda de Informática - Selección y Carrito")

producto_sel = st.selectbox("**Seleccione producto:**", productos())

if producto_sel:
    articulos = todos_productos(producto_sel)
    
    # Definimos las columnas (añadimos una columna extra para los botones de acción)
    col_id, col_nombre, col_precio, col_accion = st.columns([1, 3, 2, 2])
    col_id.write("**ID**")
    col_nombre.write("**Nombre producto**")
    col_precio.write("**Precio**")
    col_accion.write("**Acción**")
    
    for produc in articulos:
        col_id, col_nombre, col_precio, col_accion = st.columns([1, 3, 2, 2])
        col_id.write(produc["idproducto"])
        col_nombre.write(produc["nombre_producto"])
        col_precio.write(produc["precio"])
        
        # Clave única obligatoria usando el ID del producto para que Streamlit distinga los botones
        prod_id = produc["idproducto"]
        
        # Usamos columnas internas para colocar los botones de "Añadir" y "Eliminar" juntos
        btn_col1, btn_col2 = col_accion.columns(2)
        
        with btn_col1:
            if st.button("➕", key=f"add_{prod_id}", help="Añadir al carrito"):
                st.session_state.carrito.append(produc)
                st.success(f"¡Añadido!")
                
        with btn_col2:
            if st.button("❌", key=f"del_{prod_id}", help="Eliminar del carrito"):
                # Si el producto está en el carrito, lo quitamos
                if produc in st.session_state.carrito:
                    st.session_state.carrito.remove(produc)
                    st.warning(f"Eliminado")

# --- SECCIÓN DEL CARRITO EN LA BARRA LATERAL ---
st.sidebar.markdown("### 🛍️ Tu Carrito de Compras")
if st.session_state.carrito:
    st.sidebar.write(f"Productos seleccionados: **{len(st.session_state.carrito)}**")
    for item in st.session_state.carrito:
        st.sidebar.text(f"- {item['nombre_producto']} ({item['precio']})")
    
    if st.sidebar.button("Vaciar carrito"):
        st.session_state.carrito = []
        st.rerun()
else:
    st.sidebar.info("El carrito está vacío.")