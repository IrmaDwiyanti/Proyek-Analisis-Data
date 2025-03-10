import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data dari CSV
file_path = os.path.join(os.path.dirname(__file__), "main_data.csv")
data = pd.read_csv(file_path)

# Konversi kolom tanggal jika ada
if 'Tanggal' in data.columns:
    data['Tanggal'] = pd.to_datetime(data['Tanggal'])

# Judul Dashboard
st.title('Dashboard Penjualan dan Pelanggan')

# Menampilkan data utama dalam bentuk tabel
st.subheader('Data Kategori Produk, Metode Pembayaran, Kota, dan Provinsi')
st.dataframe(data)

# Sidebar untuk filter interaktif
st.sidebar.header("Filter Data")

# Filter berdasarkan metode pembayaran
metode_pembayaran = st.sidebar.selectbox("Pilih Metode Pembayaran", ["Semua"] + data["Metode Pembayaran"].unique().tolist())

# Filter berdasarkan kategori produk
kategori_produk = st.sidebar.multiselect("Pilih Kategori Produk", data["Kategori Produk"].unique(), default=data["Kategori Produk"].unique())

# Filter berdasarkan rentang tanggal
if 'Tanggal' in data.columns:
    start_date = st.sidebar.date_input("Pilih Tanggal Awal", data["Tanggal"].min())
    end_date = st.sidebar.date_input("Pilih Tanggal Akhir", data["Tanggal"].max())

# Menyaring data berdasarkan filter yang dipilih
data_filtered = data.copy()

if metode_pembayaran != "Semua":
    data_filtered = data_filtered[data_filtered["Metode Pembayaran"] == metode_pembayaran]

if kategori_produk:
    data_filtered = data_filtered[data_filtered["Kategori Produk"].isin(kategori_produk)]

if 'Tanggal' in data.columns:
    data_filtered = data_filtered[(data_filtered["Tanggal"] >= pd.to_datetime(start_date)) & (data_filtered["Tanggal"] <= pd.to_datetime(end_date))]

# Menampilkan data yang telah difilter
st.subheader(f'Data Setelah Filter')
st.dataframe(data_filtered)

# Menampilkan statistik deskriptif setelah filter
st.subheader('Statistik Deskriptif Setelah Filter')
st.write(data_filtered.describe())

# Menampilkan grafik kategori produk dengan jumlah pembelian
st.subheader('Grafik Kategori Produk Berdasarkan Jumlah Pembelian')
fig1, ax1 = plt.subplots()
sns.barplot(x='Kategori Produk', y='Jumlah Pembelian', data=data_filtered, ax=ax1)
ax1.set_title('Kategori Produk Berdasarkan Jumlah Pembelian')
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
st.pyplot(fig1)

# Menampilkan grafik metode pembayaran dengan jumlah transaksi
st.subheader('Grafik Metode Pembayaran Berdasarkan Jumlah Transaksi')
fig2, ax2 = plt.subplots()
sns.barplot(x='Metode Pembayaran', y='Jumlah Transaksi', data=data_filtered, ax=ax2)
ax2.set_title('Metode Pembayaran Berdasarkan Jumlah Transaksi')
st.pyplot(fig2)

# Menampilkan grafik kota dengan jumlah pelanggan
st.subheader('Grafik Kota Berdasarkan Jumlah Pelanggan')
fig3, ax3 = plt.subplots()
sns.barplot(x='Kota', y='Jumlah Pelanggan', data=data_filtered, ax=ax3)
ax3.set_title('Kota Berdasarkan Jumlah Pelanggan')
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)
st.pyplot(fig3)

# Menampilkan grafik provinsi dengan jumlah pelanggan
st.subheader('Grafik Provinsi Berdasarkan Jumlah Pelanggan')
fig4, ax4 = plt.subplots()
sns.barplot(x='Provinsi', y='Jumlah Pelanggan', data=data_filtered, ax=ax4)
ax4.set_title('Provinsi Berdasarkan Jumlah Pelanggan')
ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45)
st.pyplot(fig4)
