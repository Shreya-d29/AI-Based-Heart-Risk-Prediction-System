import streamlit as st
import numpy as np
import joblib
import os

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Heart Disease Risk Prediction",
    page_icon="❤️",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.stApp {
    background-color: black; //#f4f6f9
}

h1 {
    color: #b30000;
    text-align: center;
    font-weight: 700;
}

.result-card {
    padding: 25px;
    border-radius: 15px;
    background-color: #ffffff;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.12);
    text-align: center;
}

.footer {
    text-align: center;
    font-size: 12px;
    color: gray;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")

@st.cache_resource
def load_model():
    return joblib.load(model_path)

model = load_model()

# ---------------- HEADER ----------------
st.markdown("<h1>❤️ Heart Disease Risk Prediction</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center;'>AI-powered system to assess heart disease risk</p>",
    unsafe_allow_html=True
)

st.divider()

# ---------------- SIDEBAR INPUTS ----------------
st.sidebar.header("🧾 Patient Information")

age = st.sidebar.slider("Age", 20, 100, 45)
sex = st.sidebar.selectbox("Sex", ["Male", "Female"])
cp = st.sidebar.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.sidebar.slider("Resting Blood Pressure", 80, 200, 120)
chol = st.sidebar.slider("Cholesterol", 100, 400, 200)
fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120", [0, 1])
restecg = st.sidebar.selectbox("ECG Result", [0, 1, 2])
thalach = st.sidebar.slider("Max Heart Rate", 60, 220, 150)
exang = st.sidebar.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.sidebar.slider("ST Depression", 0.0, 6.0, 1.0)
slope = st.sidebar.selectbox("Slope", [0, 1, 2])
ca = st.sidebar.selectbox("Major Vessels", [0, 1, 2, 3])
thal = st.sidebar.selectbox("Thalassemia", [1, 2, 3])

sex = 1 if sex == "Male" else 0

# ---------------- SUMMARY ----------------
st.subheader("📊 Patient Summary")

c1, c2, c3 = st.columns(3)
c1.metric("Age", age)
c2.metric("BP", f"{trestbps} mmHg")
c3.metric("Cholesterol", f"{chol} mg/dl")

st.divider()

# ---------------- PREDICTION ----------------
if st.button("🔍 Predict Heart Disease Risk", use_container_width=True):

    input_data = np.array([[ 
        age, sex, cp, trestbps, chol, fbs,
        restecg, thalach, exang, oldpeak,
        slope, ca, thal
    ]])

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.markdown("<div class='result-card'>", unsafe_allow_html=True)

    if prediction == 1:
        st.error("⚠️ HIGH RISK OF HEART DISEASE")
        st.progress(int(probability * 100))
        st.write(f"Risk Probability: **{probability:.2f}**")
    else:
        st.success("✅ LOW RISK OF HEART DISEASE")
        st.progress(int((1 - probability) * 100))
        st.write(f"Safety Confidence: **{1 - probability:.2f}**")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown("""
<div class="footer">
⚕️ Educational use only – not a medical diagnosis<br>
Developed using Machine Learning & Streamlit
</div>
""", unsafe_allow_html=True)
