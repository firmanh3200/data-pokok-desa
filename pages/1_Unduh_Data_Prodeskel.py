import streamlit as st
import pandas as pd
import requests
from io import BytesIO
import xlsxwriter

# Function to fetch data from URL based on selected code
def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = pd.read_html(response.text)  # Read HTML tables from the response
        return data[0]  # Assuming the data is in the first table
    else:
        st.error("Gagal mengambil data. Status code: {}".format(response.status_code))
        return None

def kamus():
    mfd = pd.read_csv('data/mfd2023.csv', sep=',', encoding='utf-8')
    
    mendagri = pd.read_csv('data/kdkec_mendagri.csv', sep=',', encoding='utf-8')
    
    return mfd, mendagri
mfd, mendagri = kamus()

# Main Streamlit app
def main():
    st.title("PEDAS PROSA")
    st.subheader("Pengumpulan Data Sekunder Profil Desa/ Kelurahan", divider='rainbow')

    with st.container(border=True):
        st.subheader("Profil Desa Kelurahan")
        
        # Dropdown for user to select code (replace dummy options with actual values)
        kol1, kol2 = st.columns(2)
        with kol1:
            kabkot = mfd['idkab'].unique().tolist()
            kabterpilih1 = st.selectbox("Filter IDKAB", kabkot, key='kabkot1')
        with kol2:
            kec = mfd[mfd['idkab'] == kabterpilih1]['idkec'].unique().tolist()
            kecterpilih1 = st.selectbox("Filter IDKEC", kec, key='kec1')
            desa = mfd[mfd['idkec'] == kecterpilih1]['iddesa'].unique().tolist()
            
        with kol1 and kol2:
            # Menampilkan tombol unduh
            unduh = st.button(label="Unduh Data Profil", key='unduh')

            for iddesa in desa:
                try:
                    url = f"https://e-prodeskel.kemendagri.go.id/datapokok/data.php?kodesa={iddesa}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url)

                    df0 = tables[0]
                    df1 = tables[1]
                    df2 = tables[2]
                    df3 = tables[3]

                    tabel0 = pd.DataFrame(df0)
                    tabel1 = pd.DataFrame(df1)
                    tabel2 = pd.DataFrame(df2)
                    tabel3 = pd.DataFrame(df3)

                    gabungan = pd.concat([tabel0, tabel1, tabel2, tabel3], axis=1)

                    if gabungan is not None:
                        # Memproses unduhan ketika tombol diklik
                        if unduh:
                            nama_file=f"dataprofil_{iddesa}.xlsx"

                            gabungan.to_excel(f"{nama_file}", index=False)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada desa {iddesa}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati desa ini", key='lewati'):
                        continue
                    else:
                        st.stop()        
    
    with st.expander("Sarana Prasarana"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab2')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/10?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datasarpras_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Pendidikan Penduduk"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab3')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/2?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datapendidikan_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Keluarga Sejahtera"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab4')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/6?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"dataprasejahtera_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Lembaga Kemasyarakatan"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab5')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/7?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datalembaga_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Musrenbang"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab8')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/8?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datamusrenbang_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Posyandu"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab9')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/9?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"dataposyandu_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Potensi Iklim"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab11')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/11?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"dataiklim_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Sawah"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab12')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/12?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datasawah_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Penduduk"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab13')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/13?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datapenduduk_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Lahan Hutan"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab14')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/14?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datahutan_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Lahan Perkebunan"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab15')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/15?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"dataperkebunan_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Lahan Pertanian"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab16')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/16?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datapertanian_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Perangkat Desa"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab18')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/18?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"dataperangkat_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Luas Wilayah"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab19')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/19?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"dataluas_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Prasarana Keagamaan"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab20')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/20?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datafasagama_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Pendidikan Perangkat Desa"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab21')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/21?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datapendperangkat_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Air Bersih"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab22')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/22?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"dataairbersih_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Kesehatan"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab23')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/23?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datakesehatan_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Kominfo"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab24')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/24?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datakominfo_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("Umur Tunggal"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab25')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/25?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"dataumur_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
    with st.expander("RT RW"):
        # Mendapatkan daftar kodekab dari DataFrame 'mendagri' sebagai list
        kodekab_list = mendagri['kodekab'].unique().tolist()

        # Menambahkan pilihan kosong ke awal daftar kodekab
        pilihkab2 = [""] + [kode for kode in kodekab_list]

        kabterpilih2 = st.selectbox("Pilih IDKAB", pilihkab2, key='kab34')
        kec2 = mendagri[mendagri['kodekab'] == kabterpilih2]['kodekec'].unique().tolist()
        
        for kodekec in kec2:
                try:
                    url2 = f"https://e-prodeskel.kemendagri.go.id/api/d/2024/data-integrasi-level/34?kode_daerah={kodekec}"

                    # Fetch data based on selected code
                    tables = pd.read_html(url2)

                    df = tables[0]
                    
                    tabel = pd.DataFrame(df)
                    
                    if tabel is not None:
                        # Memproses unduhan ketika tombol diklik
                        if kabterpilih2:
                            nama_file=f"datartrw_{kodekec}.xlsx"

                            tabel.to_excel(f"{nama_file}", index=True)

                            # Menampilkan pesan informasi
                            st.write(f"File '{nama_file}' berhasil diunduh dan disimpan.")
            
                except Exception as e:
                    st.write(f"Kesalahan pada kecamatan {kodekec}: {e}")
                    # Tawarkan opsi kepada pengguna
                    if st.button("Lewati kecamatan ini", key='lewati2'):
                        continue
                    else:
                        st.stop()
        
            
if __name__ == "__main__":
    main()