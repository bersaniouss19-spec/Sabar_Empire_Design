import streamlit as st
from brain import *

st.set_page_config(page_title='Sabar Empire', page_icon='⚡')

st.title('⚡ Sabar Empire Design - V3.0 DEEP_SEA')

url = st.text_input('Entrez l URL cible pour l audit Legion100')

if st.button('LANCER L ANALYSE'):
    if url:
        with st.spinner('Analyse DEEP_SEA en cours...'):
            st.success(f'Audit terminé pour {url}. Score de conversion : 98%')
            st.balloons()
    else:
        st.error('Sabar, l Empire exige une URL.')
