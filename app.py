import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Base styles */
    .main {
        padding: 2rem;
        animation: fadeIn 0.5s ease-in;
    }
    
    /* Button styles */
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        padding: 0.5rem 0;
        transition: all 0.3s ease;
        animation: buttonPulse 2s infinite;
    }
    
    .stButton>button:hover {
        background-color: #FF2B2B;
        transform: scale(1.02);
    }
    
    /* Text styles */
    div[data-testid="stMarkdownContainer"] > p {
        font-size: 1.1rem;
        animation: slideIn 0.5s ease-out;
    }

    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideIn {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }

    @keyframes buttonPulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }

    /* Responsive design */
    @media screen and (max-width: 768px) {
        .main {
            padding: 1rem;
        }
        div[data-testid="stMarkdownContainer"] > p {
            font-size: 1rem;
        }
        .stButton>button {
            padding: 0.7rem 0;
        }
    }

    @media screen and (max-width: 480px) {
        .main {
            padding: 0.5rem;
        }
        div[data-testid="stMarkdownContainer"] > p {
            font-size: 0.9rem;
        }
    }

    /* Footer styles */
    .footer {
        margin-top: 2rem;
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 5px;
        animation: fadeIn 1s ease-in;
    }

    .footer a {
        color: #FF4B4B;
        text-decoration: none;
        transition: color 0.3s ease;
    }

    .footer a:hover {
        color: #FF2B2B;
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Load models
model = joblib.load('knn_heart_model.pkl')
scaler = joblib.load('heart_scaler.pkl')
expected_columns = joblib.load('heart_columns.pkl')

# Header Section
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("❤️ Heart Disease Risk Predictor")
    st.markdown("#### A Machine Learning-based Health Assessment Tool")

# Main content
st.markdown("---")
left_column, right_column = st.columns(2)

with left_column:
    st.markdown("### 📋 Patient Information")
    age = st.slider("Age", 18, 100, 40, help="Select patient's age")
    sex = st.selectbox("Gender", ["M", "F"], help="Select patient's gender")
    chest_pain = st.selectbox("Chest Pain Type", 
        ["ATA (Typical Angina)", "NAP (Non-Anginal Pain)", 
         "TA (Atypical Angina)", "ASY (Asymptomatic)"],
        help="Select type of chest pain experienced")
    chest_pain = chest_pain.split(" ")[0]  # Extract first word only
    
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 
        80, 200, 120, help="Enter resting blood pressure")
    cholesterol = st.number_input("Cholesterol Level (mg/dL)", 
        100, 600, 200, help="Enter cholesterol level")

with right_column:
    st.markdown("### 🏥 Clinical Measurements")
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", 
        ["No (0)", "Yes (1)"], help="Select fasting blood sugar status")
    fasting_bs = int(fasting_bs[-2])  # Extract number from string
    
    resting_ecg = st.selectbox("Resting ECG Results", 
        ["Normal", "ST Abnormality (ST)", "Left Ventricular Hypertrophy (LVH)"],
        help="Select ECG result")
    resting_ecg = resting_ecg.split(" ")[0] if "(" in resting_ecg else resting_ecg
    
    max_hr = st.slider("Maximum Heart Rate", 60, 220, 150, 
        help="Select maximum heart rate achieved")
    exercise_angina = st.selectbox("Exercise-Induced Angina", 
        ["No (N)", "Yes (Y)"], help="Select if angina was induced by exercise")
    exercise_angina = exercise_angina[-2]  # Extract Y or N
    
    oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0, 
        help="Select ST depression induced by exercise relative to rest")
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"], 
        help="Select the slope of peak exercise ST segment")

# Prediction Section
st.markdown("---")
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("📊 Analyze Risk", help="Click to predict heart disease risk"):
        with st.spinner('Analyzing patient data...'):
            # Create input dictionary
            raw_input = {
                'Age': age,
                'RestingBP': resting_bp,
                'Cholesterol': cholesterol,
                'FastingBS': fasting_bs,
                'MaxHR': max_hr,
                'Oldpeak': oldpeak,
                'Sex_' + sex: 1,
                'ChestPainType_' + chest_pain: 1,
                'RestingECG_' + resting_ecg: 1,
                'ExerciseAngina_' + exercise_angina: 1,
                'ST_Slope_' + st_slope: 1
            }

            # Process and predict
            input_df = pd.DataFrame([raw_input])
            for col in expected_columns:
                if col not in input_df.columns:
                    input_df[col] = 0
            input_df = input_df[expected_columns]
            scaled_input = scaler.transform(input_df)
            prediction = model.predict(scaled_input)[0]

            # Display result with custom styling
            if prediction == 1:
                st.error("#### ⚠️ High Risk of Heart Disease Detected")
                st.markdown("""
                    Please consult a healthcare professional for a thorough evaluation.
                    This prediction is based on machine learning and should not be
                    considered as a medical diagnosis.
                """)
            else:
                st.success("#### ✅ Low Risk of Heart Disease Detected")
                st.markdown("""
                    While the risk appears low, maintain a healthy lifestyle and
                    regular check-ups. This prediction is for informational
                    purposes only.
                """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Developed by Savan Kansagara| Machine Learning-Based Health Assessment Tool</p>
    <p>📧 <a href="mailto:important.savan@gmail.com">important.savan@gmail.com</a> | 
    🔗 <a href="https://www.linkedin.com/in/savan-kansagara" target="_blank">LinkedIn Profile</a></p>
    <p>⚠️ This tool is for educational purposes only and should not replace professional medical advice.</p>
</div>
""", unsafe_allow_html=True)