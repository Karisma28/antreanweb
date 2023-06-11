import streamlit as st
import numpy as np

def calculate_queue_params(arrival_rate, service_rate):
    # Menghitung laju kedatangan rata-rata (arrival rate)
    arrival_rate_avg = 1 / arrival_rate

    # Menghitung laju pelayanan rata-rata (service rate)
    service_rate_avg = 1 / service_rate

    # Menghitung jumlah server
    servers = arrival_rate / service_rate

    # Menghitung utilitas sistem
    utilization = arrival_rate / (servers * service_rate)

    # Menghitung waktu rata-rata dalam sistem (average time in system)
    time_in_system = 1 / (service_rate - arrival_rate)

    # Menghitung jumlah rata-rata pelanggan dalam sistem (average number of customers in system)
    customers_in_system = arrival_rate * time_in_system

    return arrival_rate_avg, service_rate_avg, servers, utilization, time_in_system, customers_in_system

# Judul aplikasi
st.title("Teori Antrean - Research Operation")

# Input laju kedatangan (arrival rate)
st.header("Laju Kedatangan (Arrival Rate)")
arrival_rate = st.number_input("Masukkan laju kedatangan:", step=0.01)

# Input laju pelayanan (service rate)
st.header("Laju Pelayanan (Service Rate)")
service_rate = st.number_input("Masukkan laju pelayanan:", step=0.01)

# Tombol untuk menghitung
if st.button("Hitung"):
    # Menghitung parameter antrean
    arrival_rate_avg, service_rate_avg, servers, utilization, time_in_system, customers_in_system = calculate_queue_params(
        arrival_rate, service_rate)

    # Menampilkan hasil
    st.header("Hasil")
    st.write("Laju Kedatangan Rata-rata (Arrival Rate Average):", arrival_rate_avg)
    st.write("Laju Pelayanan Rata-rata (Service Rate Average):", service_rate_avg)
    st.write("Jumlah Server:", servers)
    st.write("Utilitas Sistem:", utilization)
    st.write("Waktu Rata-rata dalam Sistem (Average Time in System):", time_in_system)
    st.write("Jumlah Rata-rata Pelanggan dalam Sistem (Average Number of Customers in System):", customers_in_system)
