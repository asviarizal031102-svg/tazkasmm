import streamlit as st

# Judul Aplikasi
st.title("📊 Simulator Model Perilaku & Keputusan Pembelian")
st.write("Silakan sesuaikan nilai koefisien jalur untuk melihat dampaknya pada variabel endogen.")

st.divider()

# --- SIDEBAR: INPUT KOEFISIEN OLEH USER ---
st.sidebar.header("🕹️ Kontrol Koefisien Jalur (Hypothesis)")

# Koefisien untuk Eksogen -> Endogen (BA)
h1 = st.sidebar.slider("H1: SMM ➔ Brand Awareness", min_value=-1.0, max_value=1.0, value=0.4, step=0.01)
h2 = st.sidebar.slider("H2: Product Strategy ➔ Brand Awareness", min_value=-1.0, max_value=1.0, value=0.3, step=0.01)

# Koefisien untuk ke Endogen Akhir (PI)
h3 = st.sidebar.slider("H3: Customer Experience ➔ Purchase Intention", min_value=-1.0, max_value=1.0, value=0.5, step=0.01)
h4 = st.sidebar.slider("H4: Brand Awareness ➔ Purchase Intention", min_value=-1.0, max_value=1.0, value=0.6, step=0.01)

# --- PANEL UTAMA: SIMULASI NILAI VARIABEL ---
st.header("⚡ Simulasi Pengaruh")
col1, col2, col3 = st.columns(3)

with col1:
    smm = st.number_input("Skor Social Media Marketing (SMM)", min_value=1.0, max_value=5.0, value=4.0)
with col2:
    ps = st.number_input("Skor Product Strategy (PS)", min_value=1.0, max_value=5.0, value=4.2)
with col3:
    cx = st.number_input("Skor Customer Experience (CX)", min_value=1.0, max_value=5.0, value=3.9)

st.divider()

# --- LOGIKA HITUNG VARIABEL ENDOGEN ---
# 1. Hitung Endogen Mediasi (Brand Awareness)
nilai_ba = (h1 * smm) + (h2 * ps)

# 2. Hitung Endogen Akhir (Purchase Intention)
# Dampak Langsung dari CX + Dampak Tidak Langsung dari BA
nilai_pi = (h3 * cx) + (h4 * nilai_ba)

# --- TAMPILKAN HASIL ENDOGEN ---
st.header("🎯 Hasil Variabel Endogen")

res_col1, res_col2 = st.columns(2)
with res_col1:
    st.metric(label="Brand Awareness (BA)", value=f"{nilai_ba:.3f}")
    st.caption("Dipengaruhi oleh SMM (H1) & PS (H2)")

with res_col2:
    st.metric(label="Purchase Intention (PI)", value=f"{nilai_pi:.3f}")
    st.caption("Dipengaruhi oleh CX (H3) & BA (H4)")
