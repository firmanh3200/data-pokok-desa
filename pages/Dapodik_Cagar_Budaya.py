import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Ambil tanggal hari ini
tanggal_hari_ini = datetime.now().strftime("%d-%m-%Y")

st.header("Jumlah Cagar Budaya")
st.warning(f"Sumber: referensi.data.kemdikbud.go.id, Kondisi: {tanggal_hari_ini}")
    
with st.container(border=True):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

st.subheader("", divider='green')

pilihan = ['Jawa Barat', 'Bogor', 'Cianjur', 'Garut', 'Tasikmalaya', 'Ciamis',
           'Kuningan', 'Sumedang', 'Indramayu', 'Purwakarta',
           'Karawang', 'Bekasi', 'Bandung Barat', 'Kota Bogor', 
           'Kota Bandung', 'Kota Cirebon', 'Kota Depok']

wilayah = st.selectbox("Pilih Wilayah", pilihan, key='pilihan')

if wilayah == 'Jawa Barat':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/020000/1'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

if wilayah == 'Bogor':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/020500/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0205{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
       

if wilayah == 'Cianjur':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/020700/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0207{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    


if wilayah == 'Garut':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/021100/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0211{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Tasikmalaya':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/021200/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0212{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Ciamis':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/021400/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0214{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Kuningan':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/021500/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0215{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    


if wilayah == 'Sumedang':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/021000/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0210{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Indramayu':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/021800/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0218{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    


if wilayah == 'Purwakarta':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/022000/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0220{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Karawang':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/022100/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0221{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Bekasi':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/022200/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0222{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Bandung Barat':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/022300/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0223{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    


if wilayah == 'Kota Bogor':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/026100/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0261{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    


if wilayah == 'Kota Bandung':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/026000/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0260{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    

if wilayah == 'Kota Cirebon':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/026300/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0263{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    


if wilayah == 'Kota Depok':
    url = 'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/026600/2'
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
    
    url2 = f'https://referensi.data.kemdikbud.go.id/kebudayaan/cagarbudaya/0266{kodeterpilih}/3'
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')

    # Temukan tabel dalam HTML
    table2 = soup2.find('table')
    df2 = pd.read_html(str(table2))[0]
    
    st.dataframe(df2, use_container_width=True, hide_index=True)
    
