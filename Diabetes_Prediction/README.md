🩺 Diabetes Prediction Web App

Machine Learning | Logistic Regression | Streamlit

📌 Project Overview

This project is an end-to-end Machine Learning application that predicts whether a person is at risk of diabetes based on medical attributes.
The trained ML model is deployed using a Streamlit web interface, allowing users to input patient data and receive instant predictions.

🚀 Features

✅ Trained Logistic Regression model

✅ Data preprocessing & feature scaling

✅ Model saved using Pickle

✅ Interactive Streamlit Web App

✅ Predicts Diabetes Risk + Probability (%)

✅ Clean, modular, and deployment-ready structure

📊 Dataset Information

The model is trained on the PIMA Indians Diabetes Dataset.

🔹 Input Features
Feature	Description
Pregnancies	Number of pregnancies
Glucose	Plasma glucose concentration
BloodPressure	Diastolic blood pressure (mm Hg)
BMI	Body Mass Index
DiabetesPedigreeFunction	Genetic likelihood of diabetes
Age	Age of the patient
🔹 Target

Outcome

0 → No Diabetes

1 → Diabetes

🧠 Machine Learning Pipeline

Data Cleaning (handling zero values)

Feature Selection

Feature Scaling using StandardScaler

Model Training using Logistic Regression

Model Evaluation (Accuracy, Confusion Matrix, Classification Report)

Model Serialization using Pickle

Deployment using Streamlit

🛠️ Tech Stack

Python

Pandas, NumPy

Scikit-Learn

Streamlit

Pickle

VS Code

📂 Project Structure
Diabetes_Prediction_ML_Project/
│
├── app.py                  # Streamlit web app
├── logreg_model.pkl        # Trained Logistic Regression model
├── scaler.pkl              # StandardScaler object
├── requirements.txt        # Project dependencies
├── venv/                   # Virtual environment
└── README.md               # Project documentation

▶️ How to Run the Project
🔹 1️⃣ Clone the Repository
git clone https://github.com/your-username/diabetes-prediction-ml.git
cd diabetes-prediction-ml

🔹 2️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

🔹 3️⃣ Install Dependencies
pip install -r requirements.txt

🔹 4️⃣ Run Streamlit App
streamlit run app.py


The app will open in your browser 🎉

📈 Model Performance

Accuracy: ~77%

Balanced precision and recall

Suitable for baseline medical risk prediction

Logistic Regression performed best compared to other tested models on this dataset.

🔐 Important Notes

Pickle files must be in the same directory as app.py

Feature order during prediction must match training order

Virtual environment is recommended for dependency isolation

🎯 Use Cases

Educational Machine Learning project

Beginner-friendly ML deployment example

Healthcare risk prediction demo

Portfolio project for Data Science roles

🔮 Future Improvements

Add multiple ML models (SVM, KNN, Decision Tree)

Model comparison inside the app

Better UI/UX with charts

Deploy on Streamlit Cloud / Render

Add input validation & warnings

👨‍💻 Author

Ishfaq Ahmed
🎓 Software Engineering Student
🎯 Aspiring Data Scientist

⭐ Acknowledgements

Dataset: PIMA Indians Diabetes Dataset

Libraries: Scikit-Learn, Streamlit

📌 Final Note

If you find this project useful, give it a ⭐ on GitHub and feel free to fork or improve it!
