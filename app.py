import streamlit as st
import joblib

# Set page title
st.set_page_config(page_title="Phishing URL Detector", page_icon="🛡️", layout="centered")

# Load model
@st.cache_resource
def load_model():
    return joblib.load('url_model.joblib')

model = load_model()

st.title("🛡️ Phishing URL Detection System")
st.write("Enter a website URL to analyze whether it is **Legitimate** or **Phishing**.")

url_input = st.text_input("Enter Website URL:", placeholder="https://example.com")

if st.button("Analyze URL", type="primary"):
    url_clean = url_input.strip()
    
    if not url_clean:
        st.warning("⚠️ Please enter a valid URL to analyze.")
    else:
        # Pass the raw URL string directly in a list to the pipeline
        prediction = model.predict([url_clean])[0]
        
        st.divider()
        if prediction == 1 or str(prediction).lower() == "phishing":
            st.error("🚨 **PHISHING URL DETECTED**", icon="⚠️")
        else:
            st.success("✅ **LEGITIMATE URL**", icon="✅")

        # Display probability if supported by model
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba([url_clean])[0]
            st.write(f"**Confidence Score:** {max(probs):.2%}")
        
          
        
