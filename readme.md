# Customer Churn Prediction using ANN

This project predicts whether a bank customer is likely to churn (leave the bank) using an Artificial Neural Network (ANN) built with TensorFlow and Keras. The application is deployed using Streamlit and provides an interactive interface for real-time predictions.

## 🚀 Live Demo

https://annclassificationchunk.streamlit.app/

---

## 📌 Features

- Predict customer churn probability
- Interactive Streamlit web interface
- Real-time predictions
- Data preprocessing using:
  - Label Encoding
  - One-Hot Encoding
  - Feature Scaling
- ANN model built using TensorFlow/Keras

---

## 🛠️ Tech Stack

- Python
- TensorFlow
- Keras
- Streamlit
- Scikit-Learn
- Pandas
- NumPy

---

## 📂 Project Structure

```text
.
├── app.py
├── model.h5
├── scaler.pkl
├── label_encoder_gender.pkl
├── one_hot_encoder.pkl
├── requirements.txt
└── README.md
```

---

## 📊 Input Features

The model predicts churn based on the following customer information:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ann_classification_chunk.git
cd ann_classification_chunk
```

### 2. Create a Conda Environment

```bash
conda create -n ann_project python=3.11
conda activate ann_project
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 🧠 Model Information

- Model Type: Artificial Neural Network (ANN)
- Framework: TensorFlow / Keras
- Loss Function: Binary Crossentropy
- Optimizer: Adam
- Output: Customer Churn Probability

---

## 🌐 Deployment

The application is deployed using Streamlit Community Cloud.

**Live Application:**  
https://annclassificationchunk.streamlit.app/

---

## 👨‍💻 Author

**Shivam Saxena**  
Indian Institute of Technology (IIT) Bhubaneswar

- Machine Learning Enthusiast
- Full Stack Developer
- Competitive Programmer

---

## ⭐ If you like this project

Give the repository a star and feel free to contribute!
