#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

# Aplicar estilo CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #201E1E; /* negro */
        color: #D8D8D8; /* blanco */
        font-size: 18px;
        font-family: 'Roboto', sans-serif;
    }
    h1 {
        color: #F2B134; /* dorado */
    }
    h2, h3, h4, h5, h6 {
        color: #CCCCCC; /* gris claro */
    }
    /* Cambiar el color del título del selectbox */
    .st-cc span {
        color: #FFFFFF !important; /* blanco */
    }
    /* Estilo para los botones del menú lateral */
    .sidebar .sidebar-content .stButton>button {
        color: #FFFFFF;
        background-color: #5C5858; /* gris oscuro */
    }
    /* Estilo para el menú lateral */
    .sidebar .sidebar-content {
        background-color: #5C5858; /* gris oscuro */
        color: #D8D8D8; /* blanco */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Función para la página de inicio
def homepage():
    st.title("WARHAMMER 40K")
    st.write("Bienvenido a la escuela de guerra y maleantería")
    st.markdown("![Warhammer40K](https://i.postimg.cc/c120Ng2f/warhammer.jpg)")

# Función para la página de cada ejército
def army_page(army_name):
    st.title(f"Ejército de {army_name}")
    if army_name == "Adeptus Custodes":
        st.markdown("![Ejercito de Adeptus Custodes](https://i.postimg.cc/HkbbpzF1/Custodes.jpg)")
        st.write("Sólo en la muerte acaba el deber")
        st.write("**Unidades clave:**")
        st.write("""- Trajann Valoris: M6 R6 Sv2+ 4++ W7 LD5 OC2
        2 Disparos de F5 FP-2 D3
                 
        6 Ataques F10 FP-3 D3""")
        st.write("**Estratagemas importantes:**")
        st.write("- Reducción de daño en cualquier fase 2CP Battle Tactic ")
        st.write("**Triquiñuelas varias:**")
        st.write("- Rapid Ingress con el campeón de filo y su unidad a 6 UM de un aliado; intervención heróica gratuita")
    elif army_name == "Devoradores de Mundos":
        st.markdown("![Ejercito de Devoradores de Mundos](https://i.postimg.cc/MKqn7wFN/Angron.jpg)")
        st.write("¡Mata! ¡Mutila! ¡Quema!")
        st.write("**Unidades clave:**")
        st.write(""""- Angron: M14 R11 Sv2+ 4++ W16 LD5 OC6
        Dos perfiles CC: 8A 2+ F16 FP-4 D1D6+2 o 18A 2+ F8 FP-2 D2
        """)
        st.write("**Estratagemas importantes:**")
        st.write("- Autoavance 6 1CP Battle Tactic")
        st.write("**Triquiñuelas varias:**")
        st.write("""- Autoavance de 6, avanza-carga con blessing of khorne. No desplegar en primera línea contra ellos lo que no quieras
        que muera.""")

# Definición del menú lateral
menu = ["Inicio", "Adeptus Custodes", "Devoradores de Mundos"]
choice = st.sidebar.selectbox("Investiga al Enemigo", menu)

# Rutas de navegación
if choice == "Inicio":
    homepage()
elif choice == "Adeptus Custodes":
    army_page("Adeptus Custodes")
elif choice == "Devoradores de Mundos":
    army_page("Devoradores de Mundos")

