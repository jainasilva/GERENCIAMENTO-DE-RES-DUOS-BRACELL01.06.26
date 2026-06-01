import streamlit as st
from pathlib import Path
from PIL import Image

st.set_page_config(page_title="Galeria T?cnica Bracell", layout="wide")
st.title("Galeria T?cnica da Apresenta??o")
st.write("Imagens dos slides carregadas pela pasta `assets/images`, compat?vel com GitHub e Streamlit Cloud.")

BASE_DIR = Path(__file__).parent
IMG_DIR = BASE_DIR / "assets" / "images"

SLIDES = [
    (1, 'ENGENHARIA & SUSTENTABILIDADE', 'slide01.png'),
    (2, 'Introdução', 'slide2.png'),
    (3, 'Política Ambiental (Sustentabilidade) e Programas Ambientais', 'slide03.png'),
    (4, 'Caracterização da Empresa', 'slide04.png'),
    (5, 'Gestão de Resíduos Industriais', 'slide05.png'),
    (6, 'Tratamento e Destinação de Resíduos', 'slide06.png'),
    (7, 'Gestão dos Recursos Hídricos', 'slide07.png'),
    (8, 'Gestão de Agua / Efluentes / Resíduos - Dados 2025', 'slide08.png'),
    (9, 'Captação Hídrica para Apoio às Operações Florestais', 'slide09.png'),
    (10, 'Uso da Água e Estruturas de Captação', 'slide10.png'),
    (11, 'Geração de Energia por Biomassa e Licor Negro', 'slide11.png'),
    (12, 'Excedente de Energia e Contribuição ao SIN', 'slide12.png'),
    (13, 'Manejo Florestal Sustentável', 'slide13.png'),
    (14, 'Licenciamento Ambiental', 'slide14.png'),
    (15, 'Responsabilidade Socioambiental', 'slide15.png'),
    (16, 'Benefícios da Gestão Ambiental', 'slide16.png'),
    (17, 'Passivo Ambiental Identificado', 'slide17.png'),
    (18, 'Plano de Ação PRAD', 'slide18.png'),
    (19, 'Acidente Ambiental - Vazamento de Óleo', 'slide19.png'),
    (20, 'Plano de Ação / Cronograma – Passivos Ambientais', 'slide20.png'),
    (21, 'CRONOGRAMA DE EXECUÇÃO DOS PASSIVOS AMBIENTAIS', 'slide21.png'),
    (22, 'Relatório 2025 - Clima e Carbono', 'slide22.png'),
    (23, 'Perfil Territorial e Operações', 'slide23.png'),
    (24, 'Distribuicao de Áreas e Localidades Principais', 'slide24.png'),
    (25, 'Biodiversidade e Paisagens Sustentáveis', 'slide25.png'),
    (26, 'Clima, Incêndios e Inovação', 'slide26.png'),
    (27, 'Conformidade, Certificações e Dados-Chave', 'slide27.png'),
    (28, 'Consumo Hídrico e Efluentes', 'slide28.png'),
    (29, 'Sistema de Gestão Ambiental e Monitoramento', 'slide29.png'),
    (30, 'Soluções de Mitigação de Riscos Ambientais', 'slide30.png'),
    (31, 'Conclusão', 'slide31.png'),
    (32, 'Referências Bibliográficas', ''),
]

cols = st.columns(2)
for idx, (numero, titulo, arquivo) in enumerate(SLIDES):
    with cols[idx % 2]:
        st.subheader(f"Slide {numero}: {titulo}")
        caminho = IMG_DIR / arquivo
        if caminho.exists():
            st.image(Image.open(caminho), use_container_width=True)
        else:
            st.warning(f"Imagem n?o encontrada: {arquivo}")
