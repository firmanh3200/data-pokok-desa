import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.express as px
import requests

st.set_page_config(layout='wide')

st.title("Peta Tematik Desa")
st.subheader("", divider='rainbow')
kolom1, kolom2 = st.columns(2)
with kolom1:
    st.link_button("Sumber Peta", url="https://github.com/Alf-Anas/batas-administrasi-indonesia")
with kolom2:
    st.link_button("Sumber Data", url="https://portaldatadesa.jabarprov.go.id/index-profile-desa/Sosial/Demografi")
st.subheader("", divider='rainbow')

pilihan = ['Kabupaten Majalengka', 'Kabupaten Bogor', 'Kabupaten Cianjur', 'Kabupaten Bandung', 'Kabupaten Garut', 'Kabupaten Tasikmalaya',
           'Kabupaten Ciamis', 'Kabupaten Kuningan', 'Kabupaten Cirebon', 'Kabupaten Sumedang', 'Kabupaten Indramayu',
           'Kabupaten Subang', 'Kabupaten Purwakarta', 'Kabupaten Karawang', 'Kabupaten Bekasi', 'Kabupaten Bandung Barat',
           'Kabupaten Pangandaran', 'Kota Banjar']

st.subheader("", divider='green')
pilihkabkot = st.selectbox("Pilih Kabupaten", pilihan, key='kabkot')

if pilihkabkot == 'Kabupaten Majalengka':
    with st.container(border=True):
        st.subheader(f"Sebaran Penduduk di Kabupaten Majalengka, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3210.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.836392508954653, "lon": 108.22905773884696},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
######################################################################
if pilihkabkot == 'Kabupaten Bogor':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Bogor, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3201.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.59950, "lon": 106.78638},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Cianjur':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Cianjur, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3203.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.81448, "lon": 107.14060},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Bandung':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Bandung, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3204.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -7.02992, "lon": 107.52708},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Garut':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Garut, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3205.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -7.214405, "lon": 107.882637},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Tasikmalaya':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Tasikmalaya, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3206.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -7.346442, "lon": 108.217894},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Ciamis':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Ciamis, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3207.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -7.329357, "lon": 108.335811},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Kuningan':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Kuningan, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3208.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.982109, "lon": 108.492086},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Cirebon':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Cirebon, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3209.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.741128, "lon": 108.549489},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Sumedang':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Sumedang, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3211.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.836392508954653, "lon": 108.22905773884696},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Indramayu':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Indramayu, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3212.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.342386, "lon": 108.331508},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Subang':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Subang, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3213.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.559537, "lon": 107.763252},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Purwakarta':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Purwakarta, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3214.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.538031, "lon": 107.448404},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Karawang':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Karawang, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3215.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.242965, "lon": 107.404929},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Bekasi':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Bekasi, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3216.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.269498, "lon": 106.980228},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Bandung Barat':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Bandung Barat, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3217.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -6.850142, "lon": 107.502407},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kabupaten Pangandaran':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kabupaten Pangandaran, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3218.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -7.649611, "lon": 108.651554},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################
if pilihkabkot == 'Kota Banjar':
    with st.container(border=True):
        
        st.subheader(f"Sebaran Penduduk di Kota Banjar, Tahun 2023")
        geojson_data = requests.get(
            "https://raw.githubusercontent.com/firmanh3200/batas-administrasi-indonesia/refs/heads/master/Kel_Desa/desa3279.json"
        ).json()

        data = pd.read_csv(
            'data/idm_sosial_demografi_desa.csv', 
            dtype={'id_kab':'str', 'id_kec':'str', 'id_desa':'str', 'total_pend':'float'}
        )

        data['KODE_KD'] = data['id_desa'].astype(str).str.slice(0, 2) + '.' + \
                        data['id_desa'].astype(str).str.slice(2, 4) + '.' + \
                        data['id_desa'].astype(str).str.slice(4, 6) + '.' + \
                        data['id_desa'].astype(str).str.slice(6, 10)

        fig = px.choropleth_mapbox(
            data_frame=data,
            geojson=geojson_data,
            locations="KODE_KD",
            color="total_pend",
            range_color=[0, 10000],
            color_continuous_scale="Viridis_r",
            opacity=0.7,
            featureidkey="properties.KODE_KD",
            zoom=9,
            center={"lat": -7.370041, "lon": 108.529670},
            mapbox_style="carto-positron",
            hover_name="desa",
            hover_data=["kecamatan", "desa", "total_pend"]
        )

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(fig, use_container_width=True)
############################################################

