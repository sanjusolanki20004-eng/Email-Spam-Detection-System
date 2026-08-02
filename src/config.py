from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATASET_PATH = PROJECT_ROOT / "Src" / "Data1" / "email_spam_dataset (1).csv"

MODEL_PATH = PROJECT_ROOT / "Model" / "spam_model.pkl"
VECTORIZER_PATH = PROJECT_ROOT / "Model" / "vectorizer.pkl"