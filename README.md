# Heart Disease Risk Predictor 🫀

A machine learning-powered web application that predicts the risk of heart disease based on clinical parameters. Built with Streamlit and scikit-learn.

## 🌟 Features

- Real-time heart disease risk prediction
- Interactive and user-friendly interface
- Professional medical parameter inputs
- Instant results with recommendations
- Responsive design for all devices
- Secure and private (no data storage)

## 🛠️ Technologies Used

- **Frontend:** Streamlit
- **Backend:** Python
- **Machine Learning:** 
  - scikit-learn
  - KNN Classifier
  - Feature Scaling
- **Data Processing:** Pandas
- **Model Serialization:** Joblib

## 📊 Clinical Parameters Used

- Age
- Gender
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol Level
- Fasting Blood Sugar
- Resting ECG Results
- Maximum Heart Rate
- Exercise-Induced Angina
- ST Depression (Oldpeak)
- ST Slope

## 🚀 Live Demo

Try the live application: [Heart Disease Predictor App](https://heartstrokeprediction.streamlit.app/)

## 💻 Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/savankansagara1/Heart_stroke_prediction.git
   cd Heart_stroke_prediction
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
Heart_stroke_prediction/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Project dependencies
├── knn_heart_model.pkl      # Trained KNN model
├── heart_scaler.pkl         # Feature scaler
├── heart_columns.pkl        # Model columns
└── README.md                # Project documentation
```

## 🔑 Model Details

- **Algorithm:** K-Nearest Neighbors (KNN)
- **Accuracy:** ~85% on test data
- **Features:** 11 clinical parameters
- **Output:** Binary classification (Risk/No Risk)


## 👨‍💻 Developer

- **Savan Kansagara**
  - 📧 [important.savan@gmail.com](mailto:important.savan@gmail.com)
  - 💼 [LinkedIn Profile](https://www.linkedin.com/in/savan-kansagara)

## ⚠️ Disclaimer

This tool is for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

---
Made with ❤️ by Savan Kansagara
