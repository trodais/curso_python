import streamlit as st
import json

def todos_productos(producto):
    with open("productos_informatica.json", "r", encoding="utf-8") as f:
        return list(filter(lambda p: p["nombre_producto"] == producto, json.load(f)))

def productos():
    with open("productos_informatica.json", "r", encoding="utf-8") as f:
        return list(set(map(lambda p: p["nombre_producto"], json.load(f))))

# Inicializar el carrito en la memoria de la sesión
if "carrito" not in st.session_state:
    st.session_state.carrito = []    

st.title("TIENDA ONLINE")

st.markdown("### 🏷️ OFERTA DEL DÍA")
st.metric(
    label="Teclado Inalámbrico Extraplano", 
    value="19.95 €", 
    delta="¡Ahorro de 10 €!")

st.header("Productos disponibles")

lista_productos = productos()
if lista_productos:
    producto_seleccionado = st.selectbox("**Seleccione producto:**", lista_productos)
else:
    st.warning("No se encontraron productos en el archivo JSON.")
    producto_seleccionado = None

if producto_seleccionado:
    articulos = todos_productos(producto_seleccionado)
    
    # Cabeceras
    col_idproducto, col_nombre_producto, col_precio, col_unidades, col_accion = st.columns(5)
    col_idproducto.write("**id Producto**")
    col_nombre_producto.write("**Nombre producto**")
    col_precio.write("**Precio**")
    col_unidades.write("**Unidades**")
    
    # Detalle de los productos disponibles usando enumerate para asegurar claves únicas
    for index, produc in enumerate(articulos):
        col_idproducto, col_nombre_producto, col_precio, col_unidades, col_accion = st.columns(5)
        col_idproducto.write(str(produc["idproducto"]))
        col_nombre_producto.write(produc["nombre_producto"])
        col_precio.write(f"{produc['precio']} €")
        
        prod_id = produc["idproducto"]
        
        btn_col1, btn_col2 = col_accion.columns(2)
             
        with btn_col1:
            # Clave única combinando el id del producto y el índice del bucle
            if st.button("➕", key=f"add_{prod_id}_{index}", help="Añadir al carrito"):
                st.session_state.carrito.append(produc)
                st.success("¡Añadido!")
                st.rerun()

        with btn_col2:
            if st.button("❌", key=f"del_{prod_id}_{index}", help="Eliminar del carrito"):
                for i, item in enumerate(st.session_state.carrito):
                    if item["idproducto"] == prod_id:
                        st.session_state.carrito.pop(i)
                        break
                st.rerun()

# --- SECCIÓN DEL CARRITO EN LA BARRA LATERAL ---
st.sidebar.markdown("### 🛍️ Tu Carrito de Compras")

if st.session_state.carrito:
    # 1. Total de unidades (número de elementos en la lista)
    total_unidades = len(st.session_state.carrito)
    
    
    # 2. Precio total (limpiando el símbolo '€' y espacios antes de convertir a float)
    precio_total = sum(float(str(item["precio"]).replace("€", "").strip()) for item in st.session_state.carrito)
    
    # Mostrar métricas en la barra lateral
    st.sidebar.write(f"📦 Total de unidades: **{total_unidades}**")
    st.sidebar.write(f"💰 Precio total: **{precio_total:.2f} €**")
    
    st.sidebar.markdown("---")
    
    # Listado de productos en el carrito
    for item in st.session_state.carrito:
        st.sidebar.text(f"- {item['nombre_producto']} ({item['precio']} €)")
    
    # Botón para vaciar
    if st.sidebar.button("Vaciar carrito", key="btn_vaciar"):
        st.session_state.carrito = []
        st.rerun()
else:
    st.sidebar.info("El carrito está vacío.")