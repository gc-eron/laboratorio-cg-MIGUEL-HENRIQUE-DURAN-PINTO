import cv2
import numpy as np
from numpy.random.mtrand import negative_binomial
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")
foto = Image.open("imagens/miguel.jpg")
img = np.array(foto)

st.header("1. Saturação")
col1, col2 = st.columns(2)
fator = col1.slider("Saturação", 0.0, 2.0, 1.5)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
s = hsv[:, :, 1].astype(float)
s = s * fator
s = np.clip(s, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB))

st.header("2. Brilho")
col1, col2 = st.columns(2)
fator = col1.slider("Brilho", 0.0, 2.0, 1.5)
b = hsv[:, :, 2].astype(float)
b = b * fator
b = np.clip(b, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 2] = b
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB))

st.header("3. Matiz girada")
col1, col2 = st.columns(2)
giro = col1.slider("Giro (graus)", 0, 360, 120)
h = hsv[:, :, 0].astype(int)
h = h + giro // 2
h = h % 180
hsv3 = hsv.copy()
hsv3[:, :, 0] = h
girada = cv2.cvtColor(hsv3, cv2.COLOR_HSV2RGB)
col1.image(girada)

st.header("5. Canais")
col1, col2 = st.columns(2)
col1.image(img[:, :, 0], caption="R")
col1.image(img[:, :, 1], caption="G")
col1.image(img[:, :, 2], caption="B")

so_r = img.copy()
so_r[:, :, 1] = 0
so_r[:, :, 2] = 0

so_g = img.copy()
so_g[:, :, 0] = 0
so_g[:, :, 2] = 0

so_b = img.copy()
so_b[:, :, 0] = 0
so_b[:, :, 1] = 0

imagens = [so_r, so_g, so_b]
rgb_index = col2.slider("Canal", 0, 2, 0)
col2.image(imagens[rgb_index], caption=f"só {['R', 'G', 'B'][rgb_index]}")

st.header("10. Negativo numa região")
col1, col2 = st.columns(2)
col1.image(img, caption="Imagem original")

negativo = img.copy()
negativo[:] = 255 - negativo[:]
col2.image(negativo, caption="Negativo")
