import streamlit as st
from PIL import Image

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Portafolio Camilo Velandia 2026-1",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: #9e9e9e;
    margin-bottom: 40px;
}

.card {
    background-color: #1f1f1f;
    border-radius: 18px;
    padding: 20px;
    height: 500px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-bottom: 25px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
}

.card-title {
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    margin-top: 15px;
    margin-bottom: 10px;
}

.card-description {
    text-align: center;
    color: #d0d0d0;
    min-height: 60px;
    margin-bottom: 20px;
}

.image-container {
    display: flex;
    justify-content: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    '<div class="main-title">🚀 Portafolio Camilo Velandia 2026-1</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Repositorio de ejercicios y aplicaciones</div>',
    unsafe_allow_html=True
)

# ---------------- FUNCIÓN PARA UNIFORMAR IMÁGENES ----------------
def resize_image(image_path, size=(250, 180)):
    try:
        image = Image.open(image_path)
        image = image.resize(size)
        return image
    except:
        return None

# ---------------- APPS ----------------
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

# ---------------- GRID UNIFORME ----------------
cols = st.columns(4)

for i, app in enumerate(apps):
    nombre, descripcion, imagen, url = app

    with cols[i % 4]:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)

            img = resize_image(imagen)

            if img:
                st.image(img)
            else:
                st.warning(f"Imagen faltante: {imagen}")

            st.markdown(
                f'<div class="card-title">{nombre}</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                f'<div class="card-description">{descripcion}</div>',
                unsafe_allow_html=True
            )

            st.link_button("🚀 Abrir aplicación", url)

            st.markdown('</div>', unsafe_allow_html=True)
