import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from config import DATASET_PATH, MODEL_PATH, VECTORIZER_PATH

# Load Dataset
df = pd.read_csv(DATASET_PATH)

# Check columns
print(df.columns)

# Features and Target
X = df["email_text"]
y = df["label"]

# Convert labels to numbers (if needed)
if y.dtype == "object":
    y = y.map({"ham": 0, "spam": 1})

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2),
    max_features=5000,
    min_df=2
)

X = vectorizer.fit_transform(X)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train Model
model = MultinomialNB(alpha=0.5)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save Model
with open(MODEL_PATH, "wb") as model_file:
    pickle.dump(model, model_file)

with open(VECTORIZER_PATH, "wb") as vectorizer_file:
    pickle.dump(vectorizer, vectorizer_file)

print("\nModel and Vectorizer saved successfully!")