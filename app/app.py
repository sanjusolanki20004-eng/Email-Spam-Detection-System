import streamlit as st
import os
import pickle

# Page settings
st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧",
    layout="centered"
)

# Load model and vectorizer
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR, "..", "Model", "spam_model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "..", "Model", "vectorizer.pkl"), "rb"))

# Sidebar
st.sidebar.title("📌 Project Details")
st.sidebar.write("**Project:** Email Spam Detection")
st.sidebar.write("**Algorithm:** Multinomial Naive Bayes")
st.sidebar.write("**Vectorizer:** TF-IDF")

# Main title
st.title("📧 Email Spam Detection System")
st.markdown("---")

st.write("Enter an email message below and click **Predict**.")

# Input
email = st.text_area(
    "✉️ Email Text",
    height=180,
    placeholder="Type or paste your email here..."
)

col1, col2 = st.columns(2)

with col1:
    predict = st.button("🔍 Predict", use_container_width=True)

with col2:
    clear = st.button("🗑 Clear", use_container_width=True)

if predict:

    if email.strip() == "":
        st.warning("⚠️ Please enter an email.")
    else:
        email_vector = vectorizer.transform([email])
        prediction = model.predict(email_vector)

        st.markdown("---")

        if prediction[0] == 1:
            st.error("🚨 **Result: SPAM EMAIL**")
        else:
            st.success("✅ **Result: HAM (Safe Email)**")

        st.info(f"📄 Characters: {len(email)}")
        st.info(f"📝 Words: {len(email.split())}")

if clear:
    st.rerun()

st.markdown("---")
st.caption("Developed using Python • Streamlit • Scikit-learn")