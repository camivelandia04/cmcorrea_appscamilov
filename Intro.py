import streamlit as st
from PIL import Image

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="Portafolio Camilo Velandia 2026-1",
    page_icon="🚀",
    layout="wide"
)

# ---------------- ESTILOS ----------------
st.markdown("""
<style>

/* Fondo general */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e3a8a, #2563eb);
}

/* Header */
.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: bold;
    color: white;
    margin-bottom: 10px;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #dbeafe;
    margin-bottom: 40px;
}

/* Cards */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 15px;
    backdrop-filter: blur(8px);
    min-height: 420px;
}

/* Títulos de apps */
.app-title {
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: white;
    margin-top: 10px;
}

/* Descripción */
.app-description {
    text-align: center;
    color: #dbeafe;
    min-height: 60px;
}

/* Botones */
.stLinkButton a {
    background-color: #2563eb !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 10px !important;
    text-align: center !important;
    width: 100% !important;
    font-weight: bold !important;
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

# ---------------- FUNCIÓN IMÁGENES ----------------
def resize_image(image_path, size=(260, 180)):
    try:
        img = Image.open(image_path)
        img = img.resize(size)
        return img
    except:
        return None

# ---------------- APPS ----------------
apps = [
    ("Asistente Inteligente de Documentos",
     "Consulta documentos PDF usando IA",
     "chatpdf.png",
     "https://chatpdf-2gkgpbmd3vnq2htowffrjt.streamlit.app/"),

    ("Mi Primera App",
     "Aplicación inicial de aprendizaje",
     "profe.png",
     "https://copia-del-profe-45dzzg9ogs5atek9wptrca.streamlit.app/"),

    ("Ctrl Voice",
     "Control e interacción por voz",
     "voice.png",
     "https://ctrlvoicecami-mmg9ws7pd9c3hscakyzric.streamlit.app/"),

    ("Draw Recognition",
     "Reconocimiento de dibujos",
     "draw.png",
     "https://drawrecogcami-sxnfafy6yaqknjdbfbttqi.streamlit.app/"),

    ("Asistente de lectura para estudiantes",
     "Convierte texto en audio para estudio",
     "gato_raton.png",
     "https://gato-raton-66mnqsriudsabcz6wkyfhs.streamlit.app/"),

    ("Reconocimiento de Dígitos escritos a mano",
     "Identificación automática de números escritos",
     "hand.png",
     "https://handwcami-xpercucorqt4dnsyxfzyk3.streamlit.app/"),

    ("Tablero Inteligente",
     "Sistema interactivo de información",
     "history.png",
     "https://histinfcami-enq3rqjnitnmlldanuzuch.streamlit.app/"),

    ("Reconocimiento Óptico de Caracteres",
     "Extracción de texto desde imágenes",
     "experimental1.png",
     "https://dzfgja2nmy52vg7ja2uqre.streamlit.app/"),

    ("OCR Audio",
     "Convierte texto detectado a audio",
     "ocr_audio.png",
     "https://ocr-audio-6qzk6uxjmquvissgzvk3qx.streamlit.app/"),

    ("Mi Segunda App con Modificaciones",
     "Versión mejorada de la app inicial",
     "firstapp.png",
     "https://miprimeraappcamilovelandia.streamlit.app/"),

    ("Panel de Control IoT",
     "Control y monitoreo de dispositivos",
     "mqtt.png",
     "https://sendcmqttcami-bvdehbjosmxypd5laz7tnm.streamlit.app/"),

    ("Sentiment Analysis",
     "Análisis de sentimientos",
     "sentiment.png",
     "https://sentimenta-lykwxe4dt5bwazjg78k4vw.streamlit.app/"),

    ("TDF Español",
     "Procesamiento de texto",
     "textdata.png",
     "https://tdfesp-vzoecrnaegz85hg77p7tzc.streamlit.app/"),

    ("Pregunta sobre el tema que quieras",
     "Responde preguntas de cualquier tema",
     "experimental2.png",
     "https://muu68oed9dwj3bmabak4xs.streamlit.app/"),

    ("Reconocimiento de Imágenes",
     "Clasificación y análisis visual",
     "experimental3.png",
     "https://auu7poryybbpcjjp75lvjp.streamlit.app/"),

    ("Traductor",
     "Traducción automática",
     "translator.png",
     "https://traductor-nfcdymsozk7uqmxg5hjxm7.streamlit.app/"),

    ("Vision App",
     "Análisis inteligente de imágenes",
     "vision.png",
     "https://visionapp-hbcz5lwm9kf8p9had9baye.streamlit.app/"),

    ("WordCloud",
     "Nube de palabras",
     "wordcloud.png",
     "https://wordcloud-kr76bil48arglsjsm3yqmz.streamlit.app/"),

    ("YOLOv5",
     "Detección de objetos",
     "yolo.png",
     "https://yolov5-jcz3x2ubaashsectv3advq.streamlit.app/")
]

# ---------------- GRID ----------------
for fila in range(0, len(apps), 4):
    cols = st.columns(4)

    for col, app in zip(cols, apps[fila:fila+4]):
        nombre, descripcion, imagen, url = app

        with col:
            with st.container(border=True):

                img = resize_image(imagen)

                if img:
                    st.image(img)

                st.markdown(
                    f'<div class="app-title">{nombre}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="app-description">{descripcion}</div>',
                    unsafe_allow_html=True
                )

                st.link_button("🚀 Abrir aplicación", url)
