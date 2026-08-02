import pickle

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Input email
email = input("Enter email text: ")

# Convert text
email_vector = vectorizer.transform([email])

# Predict
prediction = model.predict(email_vector)

if prediction[0] == 1:
    print("🚨 Spam Email")
else:
    print("✅ Ham (Not Spam)")
    