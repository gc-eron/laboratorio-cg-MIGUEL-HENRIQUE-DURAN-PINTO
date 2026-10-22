import numpy as np
import streamlit as st

def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)

st.title("Imagem como matriz")

bandeira = np.zeros((12, 18, 3), dtype=np.uint8)

bandeira[:, 0:6] = (0, 146, 73)
bandeira[:, 6:12] = (255, 255, 255)
bandeira[:, 12:18] = (207, 43, 54)

st.image(ampliar(bandeira))
st.dataframe([[tuple(pixel) for pixel in linha] for linha in bandeira])