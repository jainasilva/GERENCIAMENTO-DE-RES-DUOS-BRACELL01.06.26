from pathlib import Path
from PIL import Image
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
PASTA_IMAGENS = BASE_DIR / "assets" / "images"


def mostrar_imagem(nome_arquivo: str, legenda: str = "") -> None:
    caminho = PASTA_IMAGENS / nome_arquivo
    if caminho.exists():
        imagem = Image.open(caminho)
        st.image(imagem, caption=legenda, use_container_width=True)
    else:
        st.error(f"Imagem não encontrada: {nome_arquivo}")
        st.info(f"Coloque o arquivo em: {PASTA_IMAGENS / nome_arquivo}")
