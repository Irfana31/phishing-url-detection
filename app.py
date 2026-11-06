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
    
    return {
        'path_length': path_length,
        'token_count': token_count,
        'https_flag': https_flag,
        'number_of_digits': number_of_digits,
        'percentage_numeric_chars': percentage_numeric_chars
    }

# UI Layout
st.title("🛡️ Phishing URL Detection System")
st.write("Enter a website URL to analyze whether it is **Legitimate** or **Phishing** using our Random Forest classifier.")

url_input = st.text_input("Enter Website URL:", placeholder="https://example.com")

if st.button("Analyze URL", type="primary"):
    url_clean = url_input.strip()
    
    if not url_clean:
        st.warning("⚠️ Please enter a valid URL to analyze.")
    else:
        # Extract features
        features = extract_features(url_clean)
        feature_vector = [[
            features['path_length'],
            features['token_count'],
            features['https_flag'],
            features['number_of_digits'],
            features['percentage_numeric_chars']
        ]]
        
        # Make prediction
        prediction = model.predict(feature_vector)[0]
        probabilities = model.predict_proba(feature_vector)[0]
        
        # Display Results
        st.divider()
        if prediction == 1 or prediction == "phishing":
            st.error("🚨 **PHISHING URL DETECTED**", icon="⚠️")
            phish_prob = probabilities[1] if len(probabilities) > 1 else 1.0
            st.progress(float(phish_prob), text=f"Phishing Confidence: {phish_prob:.2%}")
        else:
            st.success("✅ **LEGITIMATE URL**", icon="✅")
            legit_prob = probabilities[0] if len(probabilities) > 1 else 1.0
            st.progress(float(legit_prob), text=f"Legitimate Confidence: {legit_prob:.2%}")
            
        # Display extracted features breakdown
        st.subheader("🔍 Extracted Lexical Features")
        col1, col2, col3 = st.columns(3)
        col1.metric("URL Length", features['path_length'])
        col2.metric("Token Count", features['token_count'])
        col3.metric("HTTPS Enabled", "Yes" if features['https_flag'] else "No")
        
        col4, col5 = st.columns(2)
        col4.metric("Digit Count", features['number_of_digits'])
        col5.metric("Numeric Ratio", f"{features['percentage_numeric_chars']:.2%}")

st.caption("🔒 *This tool uses machine learning predictions for risk assessment and should be used alongside standard web safety precautions.*")

        
