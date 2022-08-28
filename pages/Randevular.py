import streamlit as st
st.header("Randevular")
from functions import *
with st.expander("Randevu Ekle"):
    with st.form("randevuekle",clear_on_submit=True):
        isim=st.text_input("İsim Giriniz")
        soyisim=st.text_input("Soyisim Giriniz")
        model=st.selectbox("Model Girini",listele("modeller"))
        plaka=st.text_input("Plaka Giriniz")
        tarih=st.date_input("Randevu Tarihi")
        telefon=st.text_input("Telefon")
        urunler=st.multiselect("Kullanılacak Ürünler",listele('urunler'))
        submitted=st.form_submit_button("Randevu Ekle")
        if submitted:
            fiyat=0
            detay=""
            model=str(model)
            for a in urunler:
                ara=a[2]
                fiyat=fiyat+ara
                urun=a[0]
                modelbul=a[1].split(",")[1]
                detay=detay+"###"+urun+str(ara)+" "+str(model)
            randevuekle(isim, soyisim, model, plaka, tarih, fiyat, detay, telefon)
tabloyap("randevular", ["İsim", "Soyisim","Model", "Plaka", "Tarih",
                                    "Fiyat", "Detay", "Telefon"])
