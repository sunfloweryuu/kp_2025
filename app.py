import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# === Dummy data and model setup ===
# Kamu bisa ganti ini dengan model & data asli

# Sample training to simulate the model
df = pd.DataFrame({
    "Program Studi": ["Magister Kedokteran", "Magister Manajemen", "Magister Keperawatan", "Magister Farmasi"] * 25,
    "Jalur Masuk": np.random.choice(["Mandiri", "Beasiswa", "Kerja Sama"], 100),
    "IPK S1": np.round(np.random.uniform(2.75, 4.0, 100), 2),
    "Status Beasiswa": np.random.choice(["Ya", "Tidak"], 100),
    "Lama Studi (semester)": np.random.randint(3, 7, 100),
    "Tahun Masuk": np.random.choice([2020, 2021, 2022, 2023, 2024], 100),
    "Jumlah SKS": np.random.randint(30, 50, 100)
})

# SPP calculation
spp = 5000000 + \
      (df["Program Studi"] == "Magister Kedokteran") * 3000000 + \
      (df["Jalur Masuk"] == "Mandiri") * 2000000 - \
      (df["IPK S1"] * 500000) - \
      (df["Status Beasiswa"] == "Ya") * 3000000 + \
      (df["Lama Studi (semester)"] * 200000) + \
      (df["Jumlah SKS"] * 10000)

df["SPP (Rp)"] = spp

# Model training
X = df.drop(columns=["SPP (Rp)"])
y = df["SPP (Rp)"]

categorical_features = ["Program Studi", "Jalur Masuk", "Status Beasiswa"]
preprocessor = ColumnTransformer(transformers=[
    ("cat", OneHotEncoder(drop="first"), categorical_features)
], remainder="passthrough")

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(random_state=42))
])
model.fit(X, y)

# === STREAMLIT UI ===
st.title("🎓 Prediksi SPP Mahasiswa Pascasarjana")

st.markdown("Masukkan data mahasiswa untuk memprediksi jumlah SPP:")

program_studi = st.selectbox("Program Studi", df["Program Studi"].unique())
jalur_masuk = st.selectbox("Jalur Masuk", df["Jalur Masuk"].unique())
ipk = st.slider("IPK S1", 2.75, 4.00, 3.5)
beasiswa = st.radio("Status Beasiswa", ["Ya", "Tidak"])
lama_studi = st.slider("Lama Studi (semester)", 3, 6, 4)
tahun_masuk = st.selectbox("Tahun Masuk", sorted(df["Tahun Masuk"].unique()))
jumlah_sks = st.slider("Jumlah SKS", 30, 50, 40)

# Prediksi
input_data = pd.DataFrame([{
    "Program Studi": program_studi,
    "Jalur Masuk": jalur_masuk,
    "IPK S1": ipk,
    "Status Beasiswa": beasiswa,
    "Lama Studi (semester)": lama_studi,
    "Tahun Masuk": tahun_masuk,
    "Jumlah SKS": jumlah_sks
}])

predicted_spp = model.predict(input_data)[0]

st.subheader("💰 Prediksi SPP:")
st.success(f"Rp {int(predicted_spp):,}")

