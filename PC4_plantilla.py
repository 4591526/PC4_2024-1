# Este código sirve para instalar Streamlit en tu computadora y hacer un primer programa en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# pip install Streamlit

# Este código sirve para acceder una página web en tu navegador que te brinda información sobre Streamlit.
# Pero se ejecuta en la terminal Python de tu computadora, no en Jupyter Notebook.
# streamlit hello

# Antes de ejecutar un script de Python en Streamlit debes definir la carpeta donde se encuentra tus archivos
# cd ruta_de_tu_carpeta

# Este comando sirve para ejecutar un script de Python en Streamlit.
# Pero se ejecuta en la terminal de tu computadora, no en Jupyter Notebook.
# OJO: Debes antes tener instalado Streamlit en tu computadora, debes antes definir la ruta de tus archivos y 
##     tener un script de Python (your_script.py) que quieras ejecutar en Streamlit.
#  streamlit run your_script.py

# Este código sirve para hacer un primer programa en Streamlit.
import streamlit as st

# Creamos una barra lateral
sidebar = st.sidebar

# Si usas el siguiente código mostrará un título en la aplicación Streamlit. 
# st.title("Nombre de tu blog"): Esta línea está creando un título en la aplicación web.
# Pero, a diferencia de st.markdown, el texto estará alineado a la izquierda y no podrás cambiar el color del texto.

# La función st.markdown permite centrar y agrandar la letra del título de la web en Streamlit.
st.markdown("<h1 style='text-align: center;'>Blog de despedida 2024-I</h1>", unsafe_allow_html=True)


# <h1 style='text-align: center;'>Nombre de tu blog</h1>: Esto es una cadena de código HTML. 
# La etiqueta <h1> se utiliza para el encabezado principal de una página web, y 
# el atributo style se utiliza para agregar estilos CSS. 
# En este caso, el texto está alineado al centro (text-align: center;). 
# El texto dentro de las etiquetas <h1> ("Aquí escribe un nombre creativo para tu blog") es el contenido del encabezado.

# unsafe_allow_html=True: Este es un argumento opcional en la función markdown. 
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad. 
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.



# col1, col2 = st.columns(2): Esta línea está creando dos columnas en la interfaz de usuario de la aplicación web. 
# La función st.columns toma un número entero como argumento que especifica el número de columnas que se deben crear. 
# Las columnas creadas se asignan a las variables col1 y col2.

# En la primera columna colocamos la imagen
st.video("ppc-2024-1.mp4")

# col1.image("ellie.png", caption='Ellie', width=300): Esta línea está colocando una imagen en la primera columna (col1). 
# La función image toma como primer argumento la ruta de la imagen que se va a mostrar. 
# En este caso, la imagen es "ellie.png". 
# El argumento caption se utiliza para proporcionar un pie de foto a la imagen, en este caso 'Ellie'. 
# El argumento width se utiliza para especificar el ancho de la imagen, en este caso 300 píxeles.

# En la segunda columna colocamos el texto: Debe contener una presentación de ustedes
# Deben presentarse: ¿Quién eres?, ¿De dónde eres?, ¿Qué estudias?, ¿Qué te gusta de tu carrera?, 
# ¿Qué te gustaría hacer en el futuro?, ¿Qué te gusta hacer en tu tiempo libre?



# <div style='text-align: justify; font-size: 15px;'>{texto}</div>: Esta es una cadena de código HTML. 
# La etiqueta <div> se utiliza para agrupar contenido en HTML. 
# En este caso, el texto está justificado (text-align: justify;). 
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto.

# f"": Esta es una cadena de formato en Python. 
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena. 
# En este caso, {texto} se reemplaza por el valor de la variable texto.


# Debajo de las columnas colocamos un subtítulo que describa tu experiencia aprendiendo a programar
# Deben presentar tu experiencia aprendiendo a programar: ¿Cómo te sentiste al principio?, 
# ¿Qué te ha enseñado la programación?, ¿Qué te gusta de programar?, 
# ¿Qué te gustaría hacer con la programación en el futuro? 

# Agregamos un subtítulo
st.markdown("<h2 style='text-align: center;'> Buscador de blogs 💻</h2>", unsafe_allow_html=True)

# <h2 style='text-align: center;'>Mi experiencia aprendiendo a programar 💻</h2>: Esta es una cadena de código HTML.
# La etiqueta <h2> se utiliza para el encabezado secundario de una página web.
# El texto está centrado (text-align: center;).
# El texto dentro de las etiquetas <h2> ("Mi experiencia aprendiendo a programar 💻") es el contenido del encabezado
# unsafe_allow_html=True: Este es un argumento opcional en la función markdown.
# Por defecto, streamlit no permite HTML en el texto de Markdown por razones de seguridad.
# Sin embargo, establecer unsafe_allow_html en True permite el uso de HTML.
# Puedes agregar emojis en el texto de Markdown utilizando códigos de emoji.


codigo = st.text_input("Escribe tu código")
if codigo:
    if codigo == '20190378':
        st.markdown("<a href='https://pc4lucia.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20191384':
        st.markdown("<a href='https://pensamiento-pc4.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20196389':
        st.markdown("<a href='https://miblog.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20196400':
        st.markdown("<a href='https://miblogandrea.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20197090':
        st.markdown("<a href='https://samantapc4.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20201526':
        st.markdown("<a href='https://blog-programando-mar-casabonne-pc4.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20201750':
        st.markdown("<a href='https://mi-experiencia-como-desarrollera-aprendiendo-a-programar.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20206004':
        st.markdown("<a href='https://github.com/Panccho23710/LuisDiaz' target='_blank'>Haz clic aquí para visitar el repositorio de GitHub</a>", unsafe_allow_html=True)
    elif codigo == '20211427':
        st.markdown("<a href='https://lucianita080504.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20211974':
        st.markdown("<a href='https://experiencia-de-programacion.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20212192':
        st.markdown("<a href='https://pc4linknose.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20212370':
        st.markdown("<a href='https://valenhuaroc-pc4-amorodioconpython.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20216214':
        st.markdown("<a href='https://casiiita-uwu.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20216435':
        st.markdown("<a href='https://rorito-pc4.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20216736':
        st.markdown("<a href='https://tratandodeprogramarsindesprogramarteelcerebro.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20216824':
        st.markdown("<a href='https://camilavalderramapc4.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20220276':
        st.markdown("<a href='https://pc4alvacciara.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20220407':
        st.markdown("<a href='https://apublicistcodingjourney.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20220951':
        st.markdown("<a href='https://pensamiento-computacional-pc4.streamlit.app' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20221285':
        st.markdown("<a href='https://las-pythonventuras-con-ainhoa-pc4.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20221338':
        st.markdown("<a href='https://github.com/fefeporras/PorrasPC4/tree/main' target='_blank'>Haz clic aquí para visitar el repositorio de GitHub</a>", unsafe_allow_html=True)
    elif codigo == '20221531':
        st.markdown("<a href='https://unpocodelavidadepaula.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20223396':
        st.markdown("<a href='https://v-log-python-monica.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20224944':
        st.markdown("<a href='https://blogcito-sweet-de-programacion-harooo.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    elif codigo == '20224983':
        st.markdown("<a href='https://practica-para-la-practicante-wavi.streamlit.app/' target='_blank'>Haz clic aquí para visitar el blog</a>", unsafe_allow_html=True)
    else:
        st.write("Código incorrecto")


# <div style='text-align: justify; font-size: 15px;'>{texto_2}</div>: Esta es una cadena de código HTML.
# La etiqueta <div> se utiliza para agrupar contenido en HTML.
# En este caso, el texto está justificado (text-align: justify;).
# El tamaño de la fuente se establece en 15 píxeles (font-size: 15px;).
# El texto dentro de las etiquetas <div> es la variable texto_2.
# f"": Esta es una cadena de formato en Python.
# Permite la interpolación de variables, lo que significa que puedes insertar el valor de una variable directamente en la cadena.
# En este caso, {texto_2} se reemplaza por el valor de la variable texto_2.

# Agregamos un subtítulo en la barra lateral
sidebar.markdown("<h1 style='text-align: center;'>Repositorio del curso y páginas de las librerías importantes</h1>", unsafe_allow_html=True)

st.sidebar.button("Repositorio del curso" ,"https://github.com/4591526/1CCO19-2024-I")

st.sidebar.button("Matplotlib" ,"https://matplotlib.org/stable/gallery/index.html")

st.sidebar.button("Geopandas" ,"https://geopandas.org/en/stable/gallery/index.html")

st.sidebar.button("Plotly express" ,"https://plotly.com/python/plotly-express/")

st.sidebar.button("Seaborn" ,"https://seaborn.pydata.org/examples/index.html")

st.sidebar.button("Folium" ,"https://python-visualization.github.io/folium/latest/getting_started.html")


