import streamlit as st

# Título
st.title("Mi primera aplicación Streamlit")

# Texto
st.write("Hola, esta es mi primera aplicación web en Python.")

# Entrada de texto
nombre = st.text_input("Ingrese su nombre")

# Botón
if st.button("Saludar"):
    st.success(f"Hola {nombre}")

