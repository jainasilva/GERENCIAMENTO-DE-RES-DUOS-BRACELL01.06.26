# Publicação no Streamlit Cloud - pacote correto

Envie para o GitHub/Streamlit Cloud o CONTEÚDO desta pasta:

PACOTE_STREAMLIT_CLOUD

Estrutura correta:

streamlit_app.py
requirements.txt
data/
  slides.json
  slides-data.js
  imagens_manifest.json
assets/
  images/
    slide01.png
    slide02.png
    ...
    slide31.png
    slide10_agua.png

Importante:
- A pasta certa das imagens é assets/images.
- Não use as pastas antigas assets/images/apresentacao ou assets/images/pptx.
- Não publique apenas streamlit_app.py; publique também data e assets.
- No Streamlit Cloud/GitHub, mantenha letras minúsculas exatamente como assets/images.
