# 🫀 Heart Disease Prediction – End-to-End ML Project

**Machine Learning Project | Developed by Ishfaq 🧑‍💻**

Predict the risk of heart disease using patient medical data. This **end-to-end machine learning project** covers the entire workflow: **data preprocessing → model training → scaling → web app deployment using Streamlit**.

---

## 🌟 Project Highlights

- **End-to-End Workflow:** Complete ML pipeline from data processing to deployment.  
- **Accurate Predictions:** Random Forest model trained on heart disease datasets.  
- **Interactive Web App:** Real-time predictions with probability scores.  
- **User-Friendly Interface:** Clean design with custom background, modern buttons, and responsive layout.  
- **Scalable:** Easily extendable to other medical datasets or ML models.  

---
---

## ⚙️ End-to-End Workflow

1. **Data Collection & Preprocessing**  
   - Cleaned dataset, handled missing values.  
   - Scaled numerical features using `StandardScaler`.  

2. **Model Training & Evaluation**  
   - Built **Random Forest Classifier**.  
   - Evaluated performance using accuracy, confusion matrix, and probability scores.  

3. **Model Serialization**  
   - Saved trained model (`rf_model.pkl`) and scaler (`scaler.pkl`) using `pickle`.  

4. **Deployment**  
   - Streamlit web application for real-time prediction.  
   - Interactive user interface with input validation and probability output.  

---

## 🗂️ Project Structure

Heart_Disease_Predictor/
├── app.py # Streamlit web application
├── rf_model.pkl # Trained Random Forest model
├── scaler.pkl # Preprocessing Scaler
├── requirements.txt # Python dependencies
├── 
├── README.md # Project documentation
└── .gitignore # Files to ignore in Git

📊 Tech Stack

Python: Core programming & data handling

NumPy & pandas: Data preprocessing

scikit-learn: Machine Learning (Random Forest)

Streamlit: Web application deployment

Pickle: Model & scaler serialization

👨‍💻 Author

Ashfaque Ahmed – Machine Learning & Data Science Enthusiast
GitHub
 | LinkedIn
