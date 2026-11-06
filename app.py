import streamlit as st
import joblib
import re

# Set page title and layout
st.set_page_config(page_title="Phishing URL Detector", page_icon="🛡️", layout="centered")

# Load trained Random Forest model
@st.cache_resource
def load_model():
    return joblib.load('url_model.joblib')

model = load_model()

# Feature extraction function matching your training features
def extract_features(url):
    path_length = len(url)
    token_count = len(re.split(r'[/.\-_?&=]', url))
    https_flag = 1 if url.startswith('https://') else 0
    number_of_digits = sum(c.isdigit() for c in url)
    percentage_numeric_chars = (number_of_digits / path_length) if path_length > 0 else 0
    
    return [
        path_length,
        token_count,
        https_flag,
        number_of_digits,
        percentage_numeric_chars
    ]

# UI Layout
st.title("🛡️ Phishing URL Detection System")
st.write("Enter a website URL to analyze whether it is **Legitimate** or **Phishing**.")

url_input = st.text_input("Enter Website URL:", placeholder="https://example.com")

if st.button("Analyze URL", type="primary"):
    url_clean = url_input.strip()
    
    if not url_clean:
        st.warning("⚠️ Please enter a valid URL to analyze.")
    else:
        # Extract features vector
        feature_vector = [extract_features(url_clean)]
        
        # Make prediction
        prediction = model.predict(feature_vector)[0]
        
        st.divider()
        
        # Check prediction output
        if prediction == 1 or str(prediction).lower() == "phishing":
            st.error("🚨 **PHISHING URL DETECTED**", icon="⚠️")
        else:
            st.success("✅ **LEGITIMATE URL**", icon="✅")

        # Display probability score if supported by model
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(feature_vector)[0]
            confidence = max(probs)
            st.write(f"**Confidence Score:** {confidence:.2%}")
