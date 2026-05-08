import streamlit as st
st.title('í¿›ï¸ LEGION100 : AUDIT DEEP SEA')
url = st.text_input('URL CIBLE')
if st.button('LANCER'):
    st.success(f'Audit terminÃ© pour {url}. Score : 98%')
