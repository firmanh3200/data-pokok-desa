import streamlit as st
import requests
import pandas as pd
import lxml
from datetime import datetime

# Ambil tanggal hari ini
tanggal_hari_ini = datetime.now().strftime("%d-%m-%Y")

st.set_page_config(layout="wide")
st.title("Belanja Desa")
st.warning(f"Sumber: https://portaldatadesa.jabarprov.go.id/index-profile-desa/Ekonomi/Pendapatan-Desa, Kondisi: {tanggal_hari_ini}")
st.subheader("", divider='green')

pilihantahun = ['2024', '2023', '2022', '2021']

tahunterpilih = st.selectbox("Filter Tahun", pilihantahun, key='tahun')

if tahunterpilih:
    # Fungsi untuk mengambil data dari API dengan parameter halaman
    @st.cache_data
    def fetch_data(page, limit=25):
        url = f"https://portaldatadesa.jabarprov.go.id/api/idm/idmdataidentitas/v2?sub_name=TOTAL%20BELANJA%20APBDes&tahun={tahunterpilih}&order=asc&orderby=id_desa&page={page}&limit={limit}"
        response = requests.get(url)
        data = response.json()
        return data['data']

    # Mengambil data dari beberapa halaman
    all_data = []
    for page in range(1, 213):  # Misalnya, mengambil 4 halaman pertama
        page_data = fetch_data(page)
        all_data.extend(page_data)

    # Flatten the nested list of dictionaries
    flattened_data = []
    for entry in all_data:
        flattened_entry = {item['indikator_db']: item['value'] for item in entry}
        flattened_data.append(flattened_entry)

    # Mengonversi data menjadi DataFrame
    df = pd.DataFrame(flattened_data)
    
    del df['id']
    df['id_kab'] = df['id_kab'].astype(str)
    df['id_kec'] = df['id_kec'].astype(str)
    df['id_desa'] = df['id_desa'].astype(str)
    df['tahun'] = df['tahun'].astype(str)
    
    pilihankab = df['kabupaten'].unique()
    
    kol1, kol2 = st.columns(2)
    with kol1:
        kabterpilih = st.selectbox("Pilih Kabupaten", pilihankab, key='kab')
    with kol2:
        pilihankec = df[df['kabupaten'] == kabterpilih]['kecamatan'].unique()
        kecterpilih = st.selectbox("Pilih Kecamatan", pilihankec, key='kec')
        
    if kabterpilih and kecterpilih:
        df2 = df[(df['kabupaten'] == kabterpilih) & (df['kecamatan'] == kecterpilih)]
        
        st.dataframe(df2, hide_index=True, use_container_width=True)