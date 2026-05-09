import streamlit as st
from PIL import Image

st.title("Aplicaciones de Inteligencia Artificial")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial")
    parrafo = (
        "Explora diferentes aplicaciones desarrolladas con Inteligencia Artificial: "
        "procesamiento de lenguaje natural, visión computacional, reconocimiento de voz, "
        "realidad aumentada, análisis de sentimientos y más."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

col1, col2, col3 = st.columns(3)

# ---------------- COLUMNA 1 ----------------
with col1:

    st.subheader("Chat con PDF")
    image = Image.open('chatpdf.png')
    st.image(image, width=200)
    st.write("Consulta documentos PDF usando IA.")
    url = "https://chatpdf-2gkgpbmd3vnq2htowffrjt.streamlit.app/"
    st.write(f"ChatPDF: [Enlace]({url})")

    st.subheader("Control por Voz")
    image = Image.open('voice.png')
    st.image(image, width=200)
    st.write("Aplicación de interacción y comandos por voz.")
    url = "https://ctrlvoicecami-mmg9ws7pd9c3hscakyzric.streamlit.app/"
    st.write(f"Ctrl Voice: [Enlace]({url})")

    st.subheader("Reconocimiento de Dibujos")
    image = Image.open('draw.png')
    st.image(image, width=200)
    st.write("Identificación de dibujos usando IA.")
    url = "https://drawrecogcami-sxnfafy6yaqknjdbfbttqi.streamlit.app/"
    st.write(f"Draw Recognition: [Enlace]({url})")


# ---------------- COLUMNA 2 ----------------
with col2:

    st.subheader("Reconocimiento de Manos")
    image = Image.open('hand.png')
    st.image(image, width=200)
    st.write("Detección de manos y gestos.")
    url = "https://handwcami-xpercucorqt4dnsyxfzyk3.streamlit.app/"
    st.write(f"Hand Recognition: [Enlace]({url})")

    st.subheader("OCR + Audio")
    image = Image.open('ocr_audio.png')
    st.image(image, width=200)
    st.write("Convierte texto detectado en audio.")
    url = "https://ocr-audio-6qzk6uxjmquvissgzvk3qx.streamlit.app/"
    st.write(f"OCR Audio: [Enlace]({url})")

    st.subheader("Traductor Inteligente")
    image = Image.open('translator.png')
    st.image(image, width=200)
    st.write("Traducción automática de texto.")
    url = "https://traductor-nfcdymsozk7uqmxg5hjxm7.streamlit.app/"
    st.write(f"Traductor: [Enlace]({url})")


# ---------------- COLUMNA 3 ----------------
with col3:

    st.subheader("Análisis de Sentimientos")
    image = Image.open('sentiment.png')
    st.image(image, width=200)
    st.write("Analiza emociones y sentimientos en texto.")
    url = "https://sentimenta-lykwxe4dt5bwazjg78k4vw.streamlit.app/"
    st.write(f"Sentiment Analysis: [Enlace]({url})")

    st.subheader("WordCloud")
    image = Image.open('wordcloud.png')
    st.image(image, width=200)
    st.write("Generación de nubes de palabras.")
    url = "https://wordcloud-kr76bil48arglsjsm3yqmz.streamlit.app/"
    st.write(f"WordCloud: [Enlace]({url})")

    st.subheader("Detección de Objetos (YOLOv5)")
    image = Image.open('yolo.png')
    st.image(image, width=200)
    st.write("Detección automática de objetos en imágenes.")
    url = "https://yolov5-jcz3x2ubaashsectv3advq.streamlit.app/"
    st.write(f"YOLOv5: [Enlace]({url})")
