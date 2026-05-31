from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()

# Load the model once at startup
print("Loading AI classifier... (this takes ~30 seconds first time)")
classifier = pipeline("zero-shot-classification", model="cross-encoder/nli-MiniLM2-L6-H768")
print("Classifier ready!")

LABELS = ["suspicious activity", "emergency", "noise or irrelevant"]

LABEL_MAP = {
    "suspicious activity": "SUSPICIOUS",
    "emergency": "EMERGENCY",
    "noise or irrelevant": "NOISE"
}

def classify_report(text: str) -> dict:
    result = classifier(text, candidate_labels=LABELS)
    top_label = result["labels"][0]
    top_score = result["scores"][0]
    return {
        "label": LABEL_MAP[top_label],
        "confidence": round(top_score, 3)
    }