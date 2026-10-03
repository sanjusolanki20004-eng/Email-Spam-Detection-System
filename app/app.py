import os
import pickle
import streamlit as st


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧",
    layout="centered"
)


# =========================================================
# FIND PROJECT DIRECTORIES
# =========================================================

# app.py is inside:
# E-MAIL-SPAM-PROJECT/app/app.py

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one level up from /app
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Model folder:
# E-MAIL-SPAM-PROJECT/model/
MODEL_DIR = os.path.join(PROJECT_DIR, "model")


# =========================================================
# MODEL FILE PATHS
# =========================================================

MODEL_PATH = os.path.join(
    MODEL_DIR,
    "spam_model.pkl"
)

VECTORIZER_PATH = os.path.join(
    MODEL_DIR,
    "vectorizer.pkl"
)


# =========================================================
# LOAD MODEL AND VECTORIZER
# =========================================================

@st.cache_resource
def load_model_and_vectorizer():

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model file not found: {MODEL_PATH}"
        )

    if not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError(
            f"Vectorizer file not found: {VECTORIZER_PATH}"
        )

    with open(MODEL_PATH, "rb") as model_file:
        model = pickle.load(model_file)

    with open(VECTORIZER_PATH, "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)

    return model, vectorizer


# Load model
try:
    model, vectorizer = load_model_and_vectorizer()

except Exception as e:
    st.error("❌ Model could not be loaded.")
    st.error(str(e))

    st.stop()


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("📌 Project Details")

st.sidebar.write("**Project:** Email Spam Detection")
st.sidebar.write("**Algorithm:** Multinomial Naive Bayes")
st.sidebar.write("**Vectorizer:** TF-IDF")
st.sidebar.write("**Framework:** Streamlit")

st.sidebar.markdown("---")

st.sidebar.info(
    "This project classifies an email message "
    "as Spam or Ham (Not Spam)."
)


# =========================================================
# MAIN TITLE
# =========================================================

st.title("📧 Email Spam Detection System")

st.markdown("---")

st.write(
    "Enter an email message below and click **Predict** "
    "to determine whether it is Spam or Not Spam."
)


# =========================================================
# EMAIL INPUT
# =========================================================

email = st.text_area(
    "✉️ Email Text",
    height=200,
    placeholder="Enter your email message here..."
)


# =========================================================
# PREDICTION
# =========================================================

if st.button("🔍 Predict"):

    if not email.strip():

        st.warning("⚠️ Please enter an email message.")

    else:

        try:

            # Convert email text into TF-IDF features
            email_vector = vectorizer.transform([email])

            # Make prediction
            prediction = model.predict(email_vector)[0]

            # =================================================
            # RESULT
            # =================================================

            if prediction == 1:

                st.error("🚨 SPAM EMAIL")

                st.write(
                    "This email is likely to be spam."
                )

            else:

                st.success("✅ HAM / NOT SPAM")

                st.write(
                    "This email appears to be legitimate."
                )

        except Exception as e:

            st.error("❌ Prediction failed.")

            st.write(str(e))


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "Email Spam Detection System | "
    "Machine Learning Project"
)