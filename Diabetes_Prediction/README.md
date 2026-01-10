🩺 Diabetes Prediction Web App
🚀 Machine Learning | Logistic Regression | Streamlit
📌 Project Overview

This project is an end-to-end Machine Learning application that predicts whether a person is at risk of diabetes based on key medical parameters.
The trained ML model is deployed as an interactive Streamlit web application, enabling real-time predictions through a clean UI.

✨ Key Features

✅ Logistic Regression ML Model
✅ Data Preprocessing & Feature Scaling
✅ Model Serialization using Pickle
✅ Interactive Streamlit Web App
✅ Diabetes Risk Prediction with Probability (%)
✅ Clean, Modular & Deployment-Ready Code

📊 Dataset Information

The model is trained on the PIMA Indians Diabetes Dataset, a widely used benchmark dataset in healthcare ML.

🔹 Input Features
🧾 Feature	📖 Description
Pregnancies	Number of pregnancies
Glucose	Plasma glucose concentration
BloodPressure	Diastolic blood pressure (mm Hg)
BMI	Body Mass Index
DiabetesPedigreeFunction	Genetic likelihood of diabetes
Age	Age of the patient
🎯 Target Variable

Outcome

0 → ❌ No Diabetes

1 → ✅ Diabetes

🧠 Machine Learning Pipeline

🔹 Data Cleaning (handling invalid zero values)
🔹 Feature Selection
🔹 Feature Scaling using StandardScaler
🔹 Model Training using Logistic Regression
🔹 Model Evaluation (Accuracy, Confusion Matrix, Classification Report)
🔹 Model Saving using Pickle
🔹 Deployment using Streamlit

🛠️ Tech Stack

🟢 Python
🟢 Pandas & NumPy
🟢 Scikit-Learn
🟢 Streamlit
🟢 Pickle
🟢 VS Code

📂 Project Structure
Diabetes_Prediction_ML_Project/
│
├── app.py                  # Streamlit web application
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

🔹 3️⃣ Install Required Dependencies
pip install -r requirements.txt

🔹 4️⃣ Run the Streamlit App
streamlit run app.py


🌐 The app will automatically open in your browser.

📈 Model Performance

📌 Accuracy: ~77%
📌 Balanced Precision, Recall & F1-Score
📌 Best performance achieved using Logistic Regression

🔍 Logistic Regression performed better than other tested models on this dataset.

🔐 Important Notes

⚠️ Pickle files must be in the same directory as app.py
⚠️ Feature order during prediction must match training order
⚠️ Virtual environment is recommended for dependency isolation

🎯 Use Cases

✔️ Educational Machine Learning Project
✔️ Healthcare Risk Prediction Demo
✔️ Data Science Portfolio Project
✔️ Interview-Ready ML Deployment Example

🔮 Future Improvements

🚀 Add multiple ML models (SVM, KNN, Decision Tree)
🚀 Model comparison inside the web app
🚀 Improve UI/UX with charts and visualizations
🚀 Deploy on Streamlit Cloud / Render
🚀 Add input validation & warnings

👨‍💻 Author
Ishfaq Ahmed

🎓 Software Engineering Student
🎯 Aspiring Data Scientist

⭐ Acknowledgements

📌 Dataset: PIMA Indians Diabetes Dataset
📌 Libraries: Scikit-Learn, Streamlit

🌟 Final Note

If you like this project, please ⭐ star the repository and feel free to fork, use, or improve it!
