import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

st.title("Aplicaciones de Inteligencia Artificial")

with st.sidebar:
    st.subheader("Portafolio de Aplicaciones IA")
    st.write(
        "Explora aplicaciones de inteligencia artificial, visión computacional, "
        "procesamiento de lenguaje natural, IoT, realidad aumentada y juegos interactivos."
    )

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("Repositorio de ejercicios y aplicaciones")
st.write(f"Acceso: [Enlace]({url_ia})")

# -------- LISTA DE APPS --------
apps = [
    ("ChatPDF", "Consulta PDFs con IA", "chatpdf.png",
     "https://chatpdf-2gkgpbmd3vnq2htowffrjt.streamlit.app/"),

    ("Copia del Profe", "Apoyo académico", "profe.png",
     "https://copia-del-profe-45dzzg9ogs5atek9wptrca.streamlit.app/"),

    ("Ctrl Voice", "Control e interacción por voz", "voice.png",
     "https://ctrlvoicecami-mmg9ws7pd9c3hscakyzric.streamlit.app/"),

    ("Draw Recognition", "Reconocimiento de dibujos", "draw.png",
     "https://drawrecogcami-sxnfafy6yaqknjdbfbttqi.streamlit.app/"),

    ("Gato y Ratón", "Juego interactivo", "gato_raton.png",
     "https://gato-raton-66mnqsriudsabcz6wkyfhs.streamlit.app/"),

    ("Hand Recognition", "Reconocimiento de manos", "hand.png",
     "https://handwcami-xpercucorqt4dnsyxfzyk3.streamlit.app/"),

    ("Historia Interactiva", "Contenido histórico", "history.png",
     "https://histinfcami-enq3rqjnitnmlldanuzuch.streamlit.app/"),

    ("App Experimental 1", "Aplicación IA experimental", "experimental1.png",
     "https://dzfgja2nmy52vg7ja2uqre.streamlit.app/"),

    ("OCR Audio", "OCR + Texto a audio", "ocr_audio.png",
     "https://ocr-audio-6qzk6uxjmquvissgzvk3qx.streamlit.app/"),

    ("AR Foundation", "Realidad aumentada", "ar.png",
     "https://arfoundation-samples-rz5h29jirzc5tdwxxx5dyz.streamlit.app/"),

    ("Mi Primera App", "Proyecto inicial", "firstapp.png",
     "https://miprimeraappcamilovelandia.streamlit.app/"),

    ("MQTT Sender", "Comunicación IoT", "mqtt.png",
     "https://sendcmqttcami-bvdehbjosmxypd5laz7tnm.streamlit.app/"),

    ("Sentiment Analysis", "Análisis de sentimientos", "sentiment.png",
     "https://sentimenta-lykwxe4dt5bwazjg78k4vw.streamlit.app/"),

    ("TDF Español", "Procesamiento de texto", "textdata.png",
     "https://tdfesp-vzoecrnaegz85hg77p7tzc.streamlit.app/"),

    ("App Experimental 2", "Aplicación IA experimental", "experimental2.png",
     "https://muu68oed9dwj3bmabak4xs.streamlit.app/"),

    ("App Experimental 3", "Aplicación IA experimental", "experimental3.png",
     "https://auu7poryybbpcjjp75lvjp.streamlit.app/"),

    ("Traductor", "Traducción automática", "translator.png",
     "https://traductor-nfcdymsozk7uqmxg5hjxm7.streamlit.app/"),

    ("Vision App", "Análisis de imágenes", "vision.png",
     "https://visionapp-hbcz5lwm9kf8p9had9baye.streamlit.app/"),

    ("WordCloud", "Nube de palabras", "wordcloud.png",
     "https://wordcloud-kr76bil48arglsjsm3yqmz.streamlit.app/"),

    ("YOLOv5", "Detección de objetos", "yolo.png",
     "https://yolov5-jcz3x2ubaashsectv3advq.streamlit.app/")
]

# -------- GRID DINÁMICO 4 COLUMNAS --------
cols = st.columns(4)

for i, app in enumerate(apps):
    nombre, descripcion, imagen, url = app

    with cols[i % 4]:
        image = Image.open(imagen)
        st.subheader(nombre)
        st.image(image, width=180)
        st.write(descripcion)
        st.write(f"[Abrir aplicación]({url})")
