import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# Ambil tanggal hari ini
tanggal_hari_ini = datetime.now().strftime("%d-%m-%Y")

st.title("Piramida Penduduk")
st.warning(f"Sumber: https://sid.kemendesa.go.id/profile, Kondisi: {tanggal_hari_ini}")
st.subheader("", divider='green')

mfd = pd.read_csv('data/mfd2023.csv', dtype={'idkab':'str', 'idkec':'str', 'iddesa':'str'})

kolom1, kolom2, kolom3 = st.columns(3)
with kolom1:
    datakab = mfd['idkab'].unique().tolist()
    kabterpilih = st.selectbox("Filter ID Kabupaten/Kota", datakab, key='idkab')
with kolom2:
    datakec = mfd[mfd['idkab'] == kabterpilih]['idkec'].unique().tolist()
    kecterpilih = st.selectbox("Filter ID Kecamatan", datakec, key='idkec')
with kolom3:
    datadesa = mfd[mfd['idkec'] == kecterpilih]['iddesa'].unique().tolist()
    desaterpilih = st.selectbox("Filter ID DESA", datadesa, key='iddesa')
if kolom1 and kolom2 and kolom3:

    # URL data
    url = f"https://sid.kemendesa.go.id/population-statistic/data?location_code=&province_id=32&city_id={kabterpilih}&district_id={kecterpilih}&village_id={desaterpilih}&on=population"

    # Mengambil data dari URL
    response = requests.get(url)
    data = response.json()

    # Mengonversi data menjadi DataFrame
    df = pd.DataFrame([data])
    df2 = df.T

    st.dataframe(df2, use_container_width=False, hide_index=False)