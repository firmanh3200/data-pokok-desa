import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Ambil tanggal hari ini
tanggal_hari_ini = datetime.now().strftime("%d-%m-%Y")

st.header("Jumlah Peserta Didik")
st.warning(f"Sumber: dapo.kemdikbud.go.id, Kondisi: {tanggal_hari_ini}")

pilihantahun = ['2024', '2023', '2022', '2021', '2020', '2019']
pilihansemester = ['1', '2']

kol1, kol2 = st.columns(2)
with kol1:
    tahun = st.selectbox("Filter Tahun", pilihantahun, key='tahun')
with kol2:
    semester = st.selectbox("Filter Semester", pilihansemester, key='semester')
    
if tahun and semester:
        
    with st.container(border=True):
        # Ambil data dari URL
        url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=0&kode_wilayah=000000&semester_id={tahun}{semester}'
        response = requests.get(url)
        #soup = BeautifulSoup(response.content, 'html.parser')

        # Temukan tabel dalam HTML
        data = response.json()
        df = pd.DataFrame(data)
        del df['id_level_wilayah']
        del df['mst_kode_wilayah']
        del df['induk_provinsi']
        del df['kode_wilayah_induk_provinsi']
        del df['induk_kabupaten']
        del df['kode_wilayah_induk_kabupaten']
        
        st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("", divider='green')

pilihan = ['Jawa Barat', 'Bogor', 'Sukabumi', 'Cianjur', 'Bandung', 'Garut', 'Tasikmalaya', 'Ciamis',
           'Kuningan', 'Cirebon', 'Majalengka', 'Sumedang', 'Indramayu', 'Subang', 'Purwakarta',
           'Karawang', 'Bekasi', 'Bandung Barat', 'Pangandaran', 'Kota Bogor', 'Kota Sukabumi',
           'Kota Bandung', 'Kota Cirebon', 'Kota Bekasi', 'Kota Depok', 'Kota Cimahi',
           'Kota Tasikmalaya', 'Kota Banjar']

wilayah = st.selectbox("Pilih Wilayah", pilihan, key='pilihan')

if wilayah == 'Jawa Barat':
    with st.container(border=True):
        # Ambil data dari URL
        url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=1&kode_wilayah=020000&semester_id={tahun}{semester}'
        response = requests.get(url)
        #soup = BeautifulSoup(response.content, 'html.parser')

        # Temukan tabel dalam HTML
        data = response.json()
        df = pd.DataFrame(data)
        del df['id_level_wilayah']
        del df['mst_kode_wilayah']
        del df['induk_provinsi']
        del df['kode_wilayah_induk_provinsi']
        del df['induk_kabupaten']
        del df['kode_wilayah_induk_kabupaten']
        
        st.dataframe(df, use_container_width=True, hide_index=True)


if wilayah == 'Bogor':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=020500&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3201kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0205{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Sukabumi':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=020600&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3202kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0206{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    
if wilayah == 'Cianjur':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=020700&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3203kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0207{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    
if wilayah == 'Bandung': 
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=020800&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3204kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0208{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Garut':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=021100&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3205kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0211{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    
if wilayah == 'Tasikmalaya':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=021200&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3206kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0212{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    
if wilayah == 'Ciamis':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=021400&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3207kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0214{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    
if wilayah == 'Kuningan':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=021500&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3208kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0215{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Cirebon':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=021700&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3209kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0217{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Majalengka':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=021600&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3210kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0216{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Sumedang':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=021000&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3211kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0210{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Indramayu':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=021800&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3212kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0218{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Subang':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=021900&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3213kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0219{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Purwakarta':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=022000&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3214kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0220{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Karawang':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=022100&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3215kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0221{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Bekasi':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=022200&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3216kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0222{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Bandung Barat':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=022300&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3217kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0223{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Pangandaran':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=022500&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3218kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0225{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Kota Bogor':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=026100&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3271kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0261{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Kota Sukabumi':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=026200&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3272kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0262{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Kota Bandung':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=026000&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3273kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0260{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    
if wilayah == 'Kota Cirebon':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=026300&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3274kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0263{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    
if wilayah == 'Kota Bekasi':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=026500&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3275kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0265{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Kota Depok':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=026600&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3276kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0266{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Kota Cimahi':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=026700&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3277kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0267{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Kota Tasikmalaya':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=026800&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3278kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0268{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Kota Banjar':
    url = f'https://dapo.kemdikbud.go.id/rekap/dataPD?id_level_wilayah=2&kode_wilayah=026900&semester_id={tahun}{semester}'
    response = requests.get(url)
    #soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    data = response.json()
    df = pd.DataFrame(data)
    del df['id_level_wilayah']
    del df['mst_kode_wilayah']
    del df['induk_provinsi']
    del df['kode_wilayah_induk_provinsi']
    del df['induk_kabupaten']
    del df['kode_wilayah_induk_kabupaten']
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3279kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://dapo.kemdikbud.go.id/rekap/progresSP?id_level_wilayah=3&kode_wilayah=0269{kodeterpilih}&semester_id={tahun}{semester}'
    response2 = requests.get(url2)
    
    # Temukan tabel dalam HTML
    table2 = response2.json()
    df2 = pd.DataFrame(table2)
    del df2['sekolah_id']
    del df2['jumlah_kirim']
    del df2['induk_kecamatan']
    del df2['kode_wilayah_induk_kecamatan']
    del df2['induk_kabupaten']
    del df2['kode_wilayah_induk_kabupaten']
    del df2['induk_provinsi']
    del df2['kode_wilayah_induk_provinsi']
    #del df2['sinkron_terakhir']
    del df2['sekolah_id_enkrip']
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
