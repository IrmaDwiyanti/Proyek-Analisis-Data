import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data dari CSV
file_path = os.path.join(os.path.dirname(__file__), "main_data.csv")
data = pd.read_csv(file_path)

# Judul Dashboard
st.title('Dashboard Penjualan dan Pelanggan')

# Menampilkan data utama dalam bentuk tabel
st.subheader('Data Kategori Produk, Metode Pembayaran, Kota, dan Provinsi')
st.dataframe(data)

# Menambahkan filter pada sidebar untuk memilih metode pembayaran
st.sidebar.header("Filter Berdasarkan Metode Pembayaran")
metode_pembayaran = st.sidebar.selectbox("Pilih Metode Pembayaran", ["Semua"] + data["Metode Pembayaran"].unique().tolist())

# Mengambil data berdasarkan metode pembayaran yang dipilih
if metode_pembayaran != "Semua":
    data_filtered = data[data["Metode Pembayaran"] == metode_pembayaran]
else:
    data_filtered = data

# Menampilkan data yang telah difilter berdasarkan metode pembayaran
st.subheader(f'Filter Data dengan Metode Pembayaran: {metode_pembayaran}')
st.dataframe(data_filtered)

# Menampilkan statistik deskriptif
st.subheader('Statistik Deskriptif')
st.write(data.describe())

# Menampilkan grafik kategori produk dengan jumlah pembelian
st.subheader('Grafik Kategori Produk Berdasarkan Jumlah Pembelian')
fig1, ax1 = plt.subplots()
sns.barplot(x='Kategori Produk', y='Jumlah Pembelian', data=data[:4], ax=ax1)
ax1.set_title('Kategori Produk Berdasarkan Jumlah Pembelian')
st.pyplot(fig1)

# Menampilkan grafik metode pembayaran dengan jumlah transaksi
st.subheader('Grafik Metode Pembayaran Berdasarkan Jumlah Transaksi')
fig2, ax2 = plt.subplots()
sns.barplot(x='Metode Pembayaran', y='Jumlah Transaksi', data=data[4:7], ax=ax2)
ax2.set_title('Metode Pembayaran Berdasarkan Jumlah Transaksi')
st.pyplot(fig2)

# Menampilkan grafik kota dengan jumlah pelanggan
st.subheader('Grafik Kota Berdasarkan Jumlah Pelanggan')
fig3, ax3 = plt.subplots()
sns.barplot(x='Kota', y='Jumlah Pelanggan', data=data[7:12], ax=ax3)
ax3.set_title('Kota Berdasarkan Jumlah Pelanggan')
st.pyplot(fig3)

# Menampilkan grafik provinsi dengan jumlah pelanggan
st.subheader('Grafik Provinsi Berdasarkan Jumlah Pelanggan')
fig4, ax4 = plt.subplots()
sns.barplot(x='Provinsi', y='Jumlah Pelanggan', data=data[12:], ax=ax4)
ax4.set_title('Provinsi Berdasarkan Jumlah Pelanggan')
st.pyplot(fig4)
