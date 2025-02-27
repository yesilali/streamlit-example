import streamlit as st
st.header("Ürünler")
st.set_page_config(layout="wide")
from functions import *
with st.expander("Ürün Ekle"):
    with st.form("Ürünekle",clear_on_submit=True):
        isim=st.text_input("Ürün ismi")
        model=st.selectbox("Model Seç",listele('modeller'))
        model=str(model)
        fiyat=st.number_input("Fiyat Giriniz")
        submitted=st.form_submit_button("Ürün Ekle")
        if submitted:
            urunekle(isim,model,fiyat)

tabloyap("urunler",["İsim","Model","Fiyat"])