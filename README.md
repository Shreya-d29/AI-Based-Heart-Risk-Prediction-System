❤️ HeartGuard AI – Heart Disease Risk Prediction System
📌 Project Overview

HeartGuard AI is an AI-powered heart disease risk prediction system that helps assess the likelihood of heart disease based on patient health parameters. The project combines machine learning, data analytics, and a user-friendly interface to provide early risk assessment and awareness.

This project is designed for educational and hackathon purposes, demonstrating how AI can assist in preventive healthcare.

🚨 Problem Statement

Heart disease is one of the leading causes of death worldwide. Early detection is critical, but many people lack access to timely medical screening tools. There is a need for a simple, accessible, and intelligent system that can analyze medical parameters and predict heart disease risk efficiently.

💡 Proposed Solution

HeartGuard AI uses a machine learning classification model trained on real medical data to predict whether a person is at high or low risk of heart disease.
Users input basic health parameters through an interactive interface, and the system instantly provides a risk prediction along with confidence levels.

✨ Key Features

🧠 AI-based heart disease prediction

📊 Uses real medical dataset for training

🖥️ Interactive Streamlit web application

📈 Probability-based risk assessment

🎨 Modern frontend UI (HTML + Tailwind CSS)

⚡ Fast and lightweight execution

🛠️ Tech Stack

Programming Language: Python

Machine Learning: XGBoost, Scikit-learn

Web Framework: Streamlit

Frontend UI: HTML, Tailwind CSS, JavaScript

Data Handling: Pandas, NumPy

Model Storage: Joblib

📂 Project Structure
HeartGuard-AI/
│
├── app.py                # Streamlit application
├── train_model.py        # Model training script
├── model.pkl             # Trained ML model
├── heart_disease.csv     # Dataset used for training
├── index.html            # Frontend UI design
├── README.md             # Project documentation

⚙️ How the System Works

User enters patient health details (age, BP, cholesterol, etc.)

Input data is preprocessed and passed to the trained ML model

The model predicts:

High Risk ⚠️ or Low Risk ✅

Probability score

Results are displayed instantly on the interface

▶️ How to Run the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/shreya-deshmukh/heartguard-ai.git
cd heartguard-ai

2️⃣ Install Required Libraries
pip install -r requirements.txt


(If requirements.txt is not created yet, install manually:)

pip install streamlit pandas numpy scikit-learn xgboost joblib

3️⃣ Train the Model 
python train_model.py

4️⃣ Run the Application
streamlit run app.py

📊 Dataset Information

Source: Heart Disease medical dataset

Format: CSV

Target column: target

1 → Presence of heart disease

0 → No heart disease

📸 Screenshots

GUI Interface: Streamlit-based prediction dashboard
<img width="1907" height="915" alt="Screenshot 2026-01-03 223439" src="https://github.com/user-attachments/assets/604d4203-1dd9-4e7f-b054-3b4d83316563" />

Final Output: Risk prediction with confidence/progress bar
<img width="1920" height="918" alt="Screenshot 2026-01-03 223007" src="https://github.com/user-attachments/assets/6e3946f3-f59a-4405-afa8-0beeab7a99de" />

⚠️ Disclaimer

This project is for educational and hackathon use only.
It is not a medical diagnostic tool and should not replace professional medical advice.

👩‍💻 Team / Author

Name: 1] Shreya Deshmukh (ML & Backend)
      2] Snehal Bandgar(Frontend & UI ) 

Project Type: Hackathon Project

🏁 Conclusion

HeartGuard AI demonstrates how machine learning and modern web technologies can be combined to build impactful healthcare solutions. The project emphasizes early risk detection, user accessibility, and AI-driven decision support.
