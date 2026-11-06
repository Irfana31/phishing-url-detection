import streamlit as st
import joblib

# Load the trained model
model = joblib.load("url_model.joblib")

# Website title
st.title("🛡️ Phishing URL Detection System")

st.write(
    "Enter a website URL to check whether it is phishing or legitimate."
)

# URL input
url = st.text_input("Enter Website URL:")

# Check URL button
if st.button("Check URL"):

    if url.strip():

        prediction = model.predict([url.strip()])[0]
        probabilities = model.predict_proba([url.strip()])[0]

        classes = model.classes_
        phishing = probabilities[list(classes).index(0)] * 100
        legitimate = probabilities[list(classes).index(1)] * 100

        if prediction == 0:
            st.error("⚠️ PHISHING URL")
        else:
            st.success("✅ LEGITIMATE URL")

        st.write(f"Phishing Probability: {phishing:.2f}%")
        st.write(f"Legitimate Probability: {legitimate:.2f}%")

        st.warning(
            "This is a machine-learning prediction, "
            "not a guarantee of website safety."
        )

    else:
        st.warning("Please enter a URL.")
       
        
        
