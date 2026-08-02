# 📧 Email Spam Detection System

A Machine Learning project that classifies an email as **Spam** or **Not Spam** using Natural Language Processing (NLP), TF-IDF Vectorization, and the Multinomial Naive Bayes algorithm.

The project is built using **Python, Scikit-learn, Pickle, Pandas, and Streamlit**.

---

# 📌 Project Overview

This project demonstrates the complete Machine Learning workflow for text classification.

- Understanding the dataset
- Data visualization
- Text preprocessing
- Feature extraction using TF-IDF
- Model training
- Saving the trained model
- Predicting spam emails
- Building a Streamlit web application

---

# 🎯 Project Objective

The objective of this project is to classify an email or SMS message as either:

- Spam
- Not Spam

using a trained Machine Learning model.

---

# 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| Python 3.9+ | Programming Language |
| Pandas | Data Analysis |
| NumPy | Numerical Computing |
| Scikit-learn | Machine Learning |
| TF-IDF Vectorizer | Feature Extraction |
| Pickle | Model Serialization |
| Streamlit | Web Application |
| VS Code | Code Editor |
| Git & GitHub | Version Control |

---

# 📁 Project Structure

```text
E-MAIL-SPAM_PROJECT/
│
├── app/
│   └── app.py
│
├── Data/
│   └── email_spam_dataset.csv
│
├── Model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── Src/
│   ├── config.py
│   ├── understand_data.py
│   ├── Data_visual.py
│   ├── train_model.py
│   └── predict.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 🤖 Machine Learning Workflow

```text
Dataset
    │
    ▼
Understand Data
    │
    ▼
Data Visualization
    │
    ▼
Text Cleaning
    │
    ▼
TF-IDF Vectorization
    │
    ▼
Train-Test Split
    │
    ▼
Train Multinomial Naive Bayes
    │
    ▼
Save Model (.pkl)
    │
    ▼
Prediction
    │
    ▼
Streamlit Application
```

---

# 📦 Installation

## Clone the Repository

```bash
git clone <repository-url>
```

## Open Project

```bash
cd E-MAIL-SPAM_PROJECT
```

## Create Virtual Environment

### Windows

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📂 Dataset

Place the dataset inside the **Data** folder.

```text
Data/email_spam_dataset.csv
```

Required Columns

| Column |
|---------|
| label |
| message |

Example

| label | message |
|-------|---------|
| ham | Hello, how are you? |
| spam | Congratulations! You won ₹50,000. |

---

# 🚀 Training the Model

Run

```bash
python Src/train_model.py
```

The trained model will be saved inside

```text
Model/
```

Generated Files

- spam_model.pkl
- vectorizer.pkl

---

# 🔍 Predict Spam Email

Run

```bash
python Src/predict.py
```

---

# 🌐 Run Streamlit Application

```bash
streamlit run app/app.py
```

The application will automatically open in your browser.

---

# ✨ Application Features

- Clean User Interface
- Email Spam Prediction
- TF-IDF Text Vectorization
- Multinomial Naive Bayes Model
- Fast Prediction
- Pickle Model Loading
- Beginner Friendly Code
- Modular Project Structure

---

# 📚 Project Modules

### config.py

Stores project configuration.

### understand_data.py

Loads and analyzes the dataset.

### Data_visual.py

Visualizes the dataset using graphs.

### train_model.py

Trains the spam detection model.

### predict.py

Loads the saved model and predicts spam emails.

### app.py

Provides the Streamlit web interface.

---

# 📝 Example Input

```
Congratulations!

You have won ₹1,00,000.

Click below to claim your reward.
```

---

# ✅ Example Output

```
Prediction

Spam
```

or

```
Prediction

Not Spam
```

---

# 🎓 Learning Outcomes

After completing this project, you will understand:

- Machine Learning Workflow
- Data Analysis using Pandas
- Text Classification
- TF-IDF Vectorization
- Naive Bayes Algorithm
- Model Serialization using Pickle
- Streamlit Web Applications
- GitHub Project Structure

---

# 🚀 Future Improvements

- Logistic Regression
- Support Vector Machine (SVM)
- Random Forest
- XGBoost
- Deep Learning (LSTM)
- Email Subject Analysis
- Multi-language Spam Detection
- Cloud Deployment
- User Authentication

---

# 👨‍💻 Developed By

**Sanju Solanki**
**

Machine Learning Project

Email Spam Detection System

---

# 📄 License

This project is developed for educational purposes.

Feel free to learn, modify, and improve it.
