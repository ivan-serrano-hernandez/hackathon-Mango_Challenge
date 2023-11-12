import streamlit as st
import time 
from PIL import Image

# Página principal
def home_page():
    # Estilos CSS para el título
    title_style = """
        <style>
            .custom-title {
                font-size: 69px;  /* Tamaño de fuente grande, ajusta según sea necesario */
                font-weight: bold;  /* Texto en negrita */
                text-align: left;  /* Centro de texto */
            }
        </style>
    """

    # Aplicar estilos al título
    st.markdown(title_style, unsafe_allow_html=True)

    # Título centrado
    st.markdown("<h1 class='custom-title'>Mango Datathon Challenge</h1>", unsafe_allow_html=True)

    # Estilos CSS para la descripción con animación
    description_animation_style = """
        <style>
            @keyframes typing {
                from { width: 0; }
                to { width: 100%; }
            }

            .custom-description {
                font-size: 20px;  /* Tamaño de fuente predeterminado */
                font-weight: bold;  /* Texto en negrita */
                text-align: left;  /* Centro de texto */
                white-space: nowrap;  /* Evita el salto de línea */
                overflow: hidden;  /* Oculta el exceso de texto */
                animation: typing 1.5s steps(200) 0.5s 1 normal both;  /* Duración, pasos, retraso y repetición de la animación */
            }

            .large-font {
                font-size: 24px;  /* Tamaño de fuente grande para el primer párrafo */
            }

            .fade-in {
                animation: fade-in 3s ease-in-out 3.5s 1 normal both; /* Duración, retraso y repetición de la animación */
            }

            @keyframes fade-in {
                from { opacity: 0; }
                to { opacity: 1; }
            }
        </style>
    """

    # Aplicar estilos a la descripción con animación
    st.markdown(description_animation_style, unsafe_allow_html=True)

    # Descripción con animación de escritura
    st.markdown("<p class='custom-description large-font'>Bienvenido a nuestro generador de outfits para Mango.</p>"
                "<p class='custom-description' style='animation-delay: 2s;'>Añade tus prendas de ropa y genera un nuevo outfit para ti en 1 click!</p>",
                unsafe_allow_html=True)
    
    time.sleep(3.5)

    # Coloca el botón en la columna central
    if st.button("¡Empezar!"):
        st.session_state.page = "outfit"

# Página de selección de outfit
def outfit_page():
    # Diccionario para almacenar las imágenes cargadas por tipo
    uploaded_images = {'torso': None, 'piernas': None, 'pies': None}

    # Función para mostrar la imagen cargada y la información de éxito
    def show_uploaded_image(image_type):
        st.image(uploaded_images[image_type], use_column_width=True)
 

    # Estilos CSS para la descripción con animación
    description_animation_style = """
        <style>
            @keyframes typing {
                from { width: 0; }
                to { width: 100%; }
            }

            .custom-description {
                font-size: 26px;  /* Tamaño de fuente predeterminado */
                font-weight: bold;  /* Texto en negrita */
                text-align: left;  /* Centro de texto */
                white-space: nowrap;  /* Evita el salto de línea */
                overflow: hidden;  /* Oculta el exceso de texto */
                animation: typing 1s steps(200) 0.5s 1 normal both;  /* Duración, pasos, retraso y repetición de la animación */
            }
        </style>
    """

    # Aplicar estilos a la descripción con animación
    st.markdown(description_animation_style, unsafe_allow_html=True)

    # Descripción con animación de escritura
    st.markdown("<p class='custom-description'>Sube tus prendas de ropa para generar tu nuevo outfit!</p>",
                unsafe_allow_html=True)

    time.sleep(1)
    # File uploaders para Torso, Piernas y Pies
    torso_image = st.file_uploader("Sube tu prenda para la parte del torso aquí (Camiseta, Sudadera, Top, etc.)", type=["jpg", "jpeg", "png"])
    piernas_image = st.file_uploader("Sube tu prenda para la parte de las piernas aquí (Vaqueros, Shorts, Falda, etc.)", type=["jpg", "jpeg", "png"])
    pies_image = st.file_uploader("Sube tu prenda para la parte de los pies aquí (Zapatos, Bambas, Sandalias, etc.)", type=["jpg", "jpeg", "png"])

    # Mostrar la imagen cargada debajo de cada File Uploader correspondiente
    if torso_image is not None:
        uploaded_images['torso'] = Image.open(torso_image)
        #st.image(uploaded_images['torso'], use_column_width=True)
        st.success("Imagen de la prenda del torso cargada correctamente.")

    if piernas_image is not None:
        uploaded_images['piernas'] = Image.open(piernas_image)
        #st.image(uploaded_images['piernas'], use_column_width=True)
        st.success(f"Imagen de la prenda de las piernas cargada correctamente.") 

    if pies_image is not None:
        uploaded_images['pies'] = Image.open(pies_image)
        #   st.image(uploaded_images['pies'], use_column_width=True)
        st.success(f"Imagen de la prenda de los pies cargada correctamente.")  

    # Botón para generar el outfit final
    if any(uploaded_images.values()):
        if st.button("Generar Outfit!"):
            st.session_state.page = "result"
            st.session_state.uploaded_images = uploaded_images  # Actualiza las imágenes cargadas


def generate_outfit(uploaded_images):
    torso = uploaded_images['torso']
    piernas = uploaded_images['piernas']
    pies = uploaded_images['pies']

    # Combina las imágenes verticalmente
    outfit_final = Image.new('RGB', (max(torso.width, piernas.width, pies.width), torso.height + piernas.height + pies.height))
    outfit_final.paste(torso, (0, 0))
    outfit_final.paste(piernas, (0, torso.height))
    outfit_final.paste(pies, (0, torso.height + piernas.height))

    return outfit_final

def result_page(uploaded_images):
    st.title("¡Resultado del Outfit!")

    # Verifica si uploaded_images está en st.session_state
    if "uploaded_images" not in st.session_state:
        st.warning("No se han cargado imágenes. Por favor, vuelve a la página de selección de outfit.")
        return
    
    # Genera el outfit final (aquí necesitarás tu lógica específica)
    outfit_final = generate_outfit(st.session_state.uploaded_images)

    # Muestra el outfit final
    st.image(outfit_final, use_column_width=True)

            
# Lógica principal
if __name__ == "__main__":
    # Página principal
    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        home_page()

    # Página de selección de outfit
    elif st.session_state.page == "outfit":
        outfit_page()

    # Página de resultado del outfit
    elif st.session_state.page == "result":
        result_page(st.session_state.upload_images)
