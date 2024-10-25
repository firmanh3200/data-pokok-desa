import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Ambil tanggal hari ini
tanggal_hari_ini = datetime.now().strftime("%d-%m-%Y")

st.header("Jumlah Sarana Pendidikan Dasar")
st.warning(f"Sumber: referensi.data.kemdikbud.go.id, Kondisi: {tanggal_hari_ini}")
    
with st.container(border=True):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("", divider='green')

pilihan = ['Jawa Barat', 'Bogor', 'Sukabumi', 'Cianjur', 'Bandung', 'Garut', 'Tasikmalaya', 'Ciamis',
           'Kuningan', 'Cirebon', 'Majalengka', 'Sumedang', 'Indramayu', 'Subang', 'Purwakarta',
           'Karawang', 'Bekasi', 'Bandung Barat', 'Pangandaran', 'Kota Bogor', 'Kota Sukabumi',
           'Kota Bandung', 'Kota Cirebon', 'Kota Bekasi', 'Kota Depok', 'Kota Cimahi',
           'Kota Tasikmalaya', 'Kota Banjar']

wilayah = st.selectbox("Pilih Wilayah", pilihan, key='pilihan')

if wilayah == 'Jawa Barat':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/020000/1/all/all/all'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)


if wilayah == 'Bogor':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/020500/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3201kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0205{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    df2 = df2.sort_values(by='Kelurahan')
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa01')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    

if wilayah == 'Sukabumi':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/020600/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3202kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0206{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa02')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    
    
if wilayah == 'Cianjur':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/020700/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3203kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0207{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa03')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    
    
if wilayah == 'Bandung': 
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/020800/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3204kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0208{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa04')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Garut':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/021100/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3205kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0211{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa05')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    
    
if wilayah == 'Tasikmalaya':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/021200/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3206kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0212{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa06')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    
    
if wilayah == 'Ciamis':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/021400/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3207kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0214{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa07')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    
    
if wilayah == 'Kuningan':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/021500/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3208kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0215{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa08')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Cirebon':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/021700/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3209kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0217{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa09')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Majalengka':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/021600/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3210kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0216{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa10')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Sumedang':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/021000/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3211kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0210{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa11')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Indramayu':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/021800/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3212kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0218{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa12')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Subang':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/021900/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3213kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0219{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa13')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Purwakarta':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/022000/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3214kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0220{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa14')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Karawang':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/022100/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3215kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0221{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa15')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Bekasi':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/022200/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3216kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0222{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa16')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Bandung Barat':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/022300/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3217kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0223{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa17')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Pangandaran':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/022500/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3218kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0225{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa18')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Kota Bogor':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/026100/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3271kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0261{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa71')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Kota Sukabumi':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/026200/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3272kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0262{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa72')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Kota Bandung':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/026000/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3273kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0260{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa73')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    
    
if wilayah == 'Kota Cirebon':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/026300/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3274kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0263{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa74')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    
    
if wilayah == 'Kota Bekasi':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/026500/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3275kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0265{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa75')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Kota Depok':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/026600/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3276kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0266{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa76')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Kota Cimahi':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/026700/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3277kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0267{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa77')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Kota Tasikmalaya':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/026800/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3278kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0268{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa78')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
    
    

if wilayah == 'Kota Banjar':
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/026900/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    st.subheader("", divider='orange')
    
    data = pd.read_csv('data/dikdas/3279kodedikbud.csv', dtype={'kodekec':'str'})
    kecterpilih = st.selectbox('Pilih Kecamatan', data['namakec'], key='kec01')
    kodeterpilih = data.loc[data['namakec'] == kecterpilih, 'kodekec'].values[0]
    
    url2 = f'https://referensi.data.kemdikbud.go.id/pendidikan/dikdas/0269{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
    desa = df2['Kelurahan'].unique()
    desaterpilih = st.selectbox("Pilih Desa/Kelurahan", desa, key='desa79')
    
    if desaterpilih:
        df3 = df2[df2['Kelurahan'] == desaterpilih]
        df3 = df3[['Kelurahan', 'Nama Satuan Pendidikan', 'Status', 'Alamat', 'NPSN']]
        st.dataframe(df3, use_container_width=True, hide_index=True)
