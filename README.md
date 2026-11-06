# 🛡️ Phishing URL Detection System

An end-to-end Machine Learning web application designed to detect malicious phishing URLs in real time using engineered lexical features and a Random Forest Classifier. Deployed seamlessly on Streamlit Community Cloud.

🚀 **Live Demo:** [Phishing URL Detector App](https://irfana31-phishing-url-detection-app-bvvr1s.streamlit.app)

---

## 📌 Features & Highlights

- **Real-Time Detection:** Evaluates user-submitted URLs instantly and outputs classification results along with confidence probabilities.
- **High Accuracy Model:** Trained Random Forest model achieving an **ROC-AUC score of ~0.9999**.
- **Lexical Feature Extraction:** Extracts key domain and URL structural metrics without requiring slow external network pinging.
- **Cloud Deployed:** Built and hosted using Python 3.11 and Streamlit Community Cloud.

---

## 📊 Key Features Extracted

The classifier evaluates URLs based on key engineered lexical indicators:
1. `path_length` — Length of the URL path segment.
2. `token_count` — Count of delimiter tokens within the URL structure.
3. `https_flag` — Indicator of secure protocol usage (`HTTPS`).
4. `number_of_digits` — Count of numeric characters present in the URL.
5. `percentage_numeric_chars` — Ratio of numbers relative to total URL length.

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.11
- **Machine Learning:** Scikit-Learn, Joblib, NumPy, Pandas
- **Web Interface:** Streamlit
- **Deployment & Version Control:** Git, GitHub, Streamlit Community Cloud

---

## ⚙️ Local Setup & Running Instructions

To run this application locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Irfana31/phishing-url-detection.git](https://github.com/Irfana31/phishing-url-detection.git)
   cd phishing-url-detection
