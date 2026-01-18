# 🕵️‍♂️ Insurance Claim Fraud Classification

A complete **Machine Learning project** that detects fraudulent insurance claims using **supervised classification** techniques.  
This project demonstrates the **end-to-end Data Science lifecycle** — from raw, messy data to a **deployed ML model** with **Streamlit**.

---

## 🧠 Overview

Insurance fraud causes billions in losses globally.  
This project builds a **fraud classification model** that predicts whether an insurance claim is **fraud (1)** or **genuine (0)**.  

It includes:
- **Dataset with 10,000 records**
- **Data cleaning & preprocessing** (handling errors, missing values, outliers)
- **EDA** for data understanding
- **Supervised ML models** for classification
- **Cross-validation** for reliability
- **Deployment** using Streamlit for real-time fraud detection

---

## 🎯 Objectives

- Build a robust supervised classification model to detect fraud.  
- Handle messy, inconsistent, and missing data effectively.  
- Deploy the model in a **Streamlit web application**.

---

## 📊 Dataset

**Dataset:** 10,000 rows × 10 columns 

| Feature | Description |
|----------|--------------|
| policy_id | Unique policy identifier |
| policy_state | US state code |
| policy_deductible | Deductible amount |
| Gender | Gender |
| incident_severity | Severity of the incident |
| vehicle_claim_amount | Claimed amount |
| vehicle_age | Vehicle age in years |
| num_of_claims | Number of previous claims |
| customer_tenure | Customer tenure in years |
| fraud_reported | Target variable (1 = Fraud, 0 = Real) |

---

## 🧹 Data Cleaning & Preprocessing

Performed using **Pandas** and **NumPy**:
- Fixed **spelling errors**, **abbreviations**, and **inconsistent categories**
- Converted **data types** (numeric, datetime)
- Handled **missing values** (imputation)
- Removed **duplicate** records
- Detected and treated **outliers**
- Ensured consistent formatting for all columns

---

## 🔍 Exploratory Data Analysis (EDA)

Conducted using **Matplotlib**, **Seaborn**, and **SQL**.

### SQL Insights

### Visual EDA (Pandas + Seaborn):

---

## 🤖 Model Training & Evaluation

### Algorithms Tested
- Logistic Regression  
- Decision Tree Classifier  
- Random Forest Classifier
- Support Vector Machine
- K-Nearest Neighbors

### Evaluation Metrics
- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**
- **ROC-AUC**
- **Cross-validation (5-fold)**

---

## 💾 Model Deployment

### Framework: **Streamlit**

**Features:**
- User inputs for claim details  
- Real-time fraud prediction with probability score  
- Interactive web interface  
