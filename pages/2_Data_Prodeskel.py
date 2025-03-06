import streamlit as st
import pandas as pd
import requests
from io import BytesIO
import xlsxwriter

st.set_page_config(layout='wide')

st.title('PEDAS PROSA')
st.subheader('Kompilasi Data Prodeskel Kemendagri', divider='orange')

kolom1, kolom2, kolom3, kolom4 = st.columns(4)

# Daftar tahun yang tersedia
daftar_tahun = list(range(2019, 2026))

# Pemilihan Tahun
with kolom1:
    tahun_terpilih = st.selectbox("Pilih Tahun:", daftar_tahun)

# 1. Baca Data CSV (Asumsi: file berisi kodekab, namakab, kodekec, namakec)
try:
    df = pd.read_csv('data/kdkec_mendagri.csv')  # Ganti dengan nama file CSV Anda
except FileNotFoundError:
    st.error("File CSV kabupaten/kecamatan tidak ditemukan. Pastikan file berada di direktori yang benar.")
    st.stop()

# 2. Ambil Daftar Nama Kabupaten Unik
nama_kabupaten_unik = sorted(df['namakab'].unique())

# 3. Streamlit Selectbox untuk Kabupaten
with kolom2:
    kabupaten_terpilih = st.selectbox("Pilih Kabupaten/Kota:", nama_kabupaten_unik)

# 4. Filter Data Berdasarkan Kabupaten Terpilih
df_kecamatan = df[df['namakab'] == kabupaten_terpilih]

# 5. Ambil Daftar Nama Kecamatan Berdasarkan Kabupaten Terpilih
nama_kecamatan = sorted(df_kecamatan['namakec'].unique())

# 6. Streamlit Selectbox untuk Kecamatan
with kolom3:
    kecamatan_terpilih = st.selectbox("Pilih Kecamatan:", nama_kecamatan)

# 7. Dapatkan Kode Kecamatan Berdasarkan Kecamatan Terpilih
kodekecterpilih = df_kecamatan[df_kecamatan['namakec'] == kecamatan_terpilih]['kodekec'].iloc[0]

# Kategori Data Options
kategori_data_options = {
    "Pendidikan": "2",
    "Kesejahteraan Keluarga": "6",
    "Perkembangan LKM": "7",
    "Musrenbangdes": "8",
    "Posyandu": "9",
    "PKK": "10",
    "Iklim": "11",
    "Lahan": "12",
    "Potensi Penduduk": "13",
    "Lahan Kehutanan": "14",
    "Lahan Perkebunan": "15",
    "Lahan Pertanian": "16",
    "Potensi LKM": "17",
    "Potensi Pemerintahan": "18",
    "Luas Wilayah": "19",
    "Keagamaan": "20",
    "Sarana Prasarana": "21",
    "Air Bersih": "22",
    "Kesehatan": "23",
    "Kominfo": "24",
    "Umur Tunggal": "25",
    "RT - RW": "34",
}

with kolom4:
    kategori_terpilih = st.selectbox(
        "Pilih Kategori Data:",
        options=list(kategori_data_options.keys()),
    )

# Dapatkan kode kategori
kodekategori = kategori_data_options[kategori_terpilih]

st.subheader('', divider='orange')

# Tombol Tampilkan
tampilkan = st.button("Tampilkan Data") #Ganti Tombol Download jadi Tampilkan
if tampilkan: #Jika Tombol Tampilkan Ditekan
    if tahun_terpilih and kodekategori and kodekecterpilih:
        url = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahun_terpilih}/data-integrasi-level/{kodekategori}?kode_daerah={kodekecterpilih}"

        # Fetch data based on selected code
        try:
            tables = pd.read_html(url)
            df = tables[0]
            tabel = pd.DataFrame(df)

            if tabel is not None:
                st.dataframe(tabel)  # Tampilkan DataFrame

        except ValueError as e:
            st.error(f"Tidak ada tabel yang ditemukan pada URL: {url}. Pastikan URL benar dan tabel HTML tersedia.")

# Opsi Download
st.subheader('', divider='orange')
donlot = st.checkbox("Opsi Download Data") #Tambahkan Checkbox Download
if donlot: #Jika Checkbox Download Dicentang
    if tahun_terpilih and kodekategori and kodekecterpilih:
        url = f"https://e-prodeskel.kemendagri.go.id/api/d/{tahun_terpilih}/data-integrasi-level/{kodekategori}?kode_daerah={kodekecterpilih}"

        # Fetch data based on selected code
        try:
            tables = pd.read_html(url)
            df = tables[0]
            tabel = pd.DataFrame(df)
        except ValueError as e:
            st.error(f"Tidak ada tabel yang ditemukan pada URL: {url}. Pastikan URL benar dan tabel HTML tersedia.")
            st.stop()

        if tabel is not None:
            nama_file = f"{kategori_terpilih}_{kecamatan_terpilih}_{tahun_terpilih}.xlsx"
            buffer = BytesIO()

            with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
                tabel.to_excel(writer, sheet_name='Sheet1', index=False)

            buffer.seek(0)
            st.download_button(
                label="Klik untuk Download File Excel",
                data=buffer,
                file_name=nama_file,
                mime='application/vnd.ms-excel'
            )