import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Ambil tanggal hari ini
tanggal_hari_ini = datetime.now().strftime("%d-%m-%Y")

st.header("Jumlah Sarana Yayasan Pendidikan")
st.warning(f"Sumber: referensi.data.kemdikbud.go.id, Kondisi: {tanggal_hari_ini}")
    
with st.container(border=True):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Jawa Barat"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/020000/1'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)


with st.expander("Kabupaten Bogor"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/020500/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Sukabumi"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/020600/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
with st.expander("Kabupaten Cianjur"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/020700/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
with st.expander("Kabupaten Bandung"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/020800/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Garut"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/021100/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
with st.expander("Kabupaten Tasikmalaya"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/021200/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
with st.expander("Kabupaten Ciamis"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/021400/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
with st.expander("Kabupaten Kuningan"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/021500/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Cirebon"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/021700/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Majalengka"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/021600/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Sumedang"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/021000/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Indramayu"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/021800/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Subang"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/021900/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Purwakarta"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/022000/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Karawang"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/022100/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Bekasi"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/022200/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Bandung Barat"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/022300/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kabupaten Pangandaran"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/022500/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kota Bogor"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/026100/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kota Sukabumi"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/026200/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kota Bandung"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/026000/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
with st.expander("Kota Cirebon"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/026300/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
with st.expander("Kota Bekasi"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/026500/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kota Depok"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/026600/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kota Cimahi"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/026700/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kota Tasikmalaya"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/026800/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)

with st.expander("Kota Banjar"):
    # Ambil data dari URL
    url = 'https://referensi.data.kemdikbud.go.id/pendidikan/yayasan/026900/2'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Temukan tabel dalam HTML
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    
    st.dataframe(df, use_container_width=True, hide_index=True)