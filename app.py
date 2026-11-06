import streamlit as st
import joblib

st.set_page_config(page_title="Phishing URL Detector", page_icon="🛡️", layout="centered")

@st.cache_resource
def load_model():
    return joblib.load('url_model.joblib')

model = load_model()

st.title("🛡️ Phishing URL Detection System")
st.write("Enter a website URL to analyze whether it is **Legitimate** or **Phishing**.")

url_input = st.text_input("Enter Website URL:", placeholder="https://example.com")

if st.button("Analyze URL", type="primary"):
    url_clean = url_input.strip()
    
    # Auto-clean if markdown format was pasted
    if "[" in url_clean and "](" in url_clean:
        url_clean = url_clean.split("](")[0].replace("[", "").strip()
        
    if not url_clean:
        st.warning("⚠️ Please enter a valid URL to analyze.")
    else:
        # Predict class (0 = Legitimate, 1 = Phishing)
        prediction = model.predict([url_clean])[0]
        
        st.divider()
        
        # Check if model provides probabilities
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba([url_clean])[0]
            # Assuming classes are [0: Legitimate, 1: Phishing]
            legit_prob = probs[0]
            phish_prob = probs[1]
        else:
            legit_prob = 1.0 if prediction == 0 else 0.0
            phish_prob = 1.0 if prediction == 1 else 0.0

        if prediction == 1 or str(prediction).lower() == "phishing":
            st.error("🚨 **PHISHING URL DETECTED**", icon="⚠️")
            st.write(f"**Confidence Score:** {phish_prob:.2%}")
        else:
            st.success("✅ **LEGITIMATE URL**", icon="✅")
            st.write(f"**Confidence Score:** {legit_prob:.2%}")
          
        
