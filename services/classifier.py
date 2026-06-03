from dotenv import load_dotenv
load_dotenv()

print("Classifier ready! (using keyword classifier)")

EMERGENCY_KEYWORDS = [
    "fire", "shooting", "shot", "gun", "knife", "stab", "attack", "attacked",
    "help", "emergency", "dying", "dead", "blood", "accident", "crash", "rape",
    "hijack", "hijacking", "explosion", "bomb"
]

SUSPICIOUS_KEYWORDS = [
    "suspicious", "stranger", "unknown", "watching", "following", "lurking",
    "broken", "forced", "tampered", "unusual", "weird", "strange", "prowling",
    "loitering", "masked", "hooded", "armed", "threatening", "threat"
]

def classify_report(text: str) -> dict:
    text_lower = text.lower()

    for word in EMERGENCY_KEYWORDS:
        if word in text_lower:
            return {"label": "EMERGENCY", "confidence": 0.95}

    for word in SUSPICIOUS_KEYWORDS:
        if word in text_lower:
            return {"label": "SUSPICIOUS", "confidence": 0.85}

    return {"label": "NOISE", "confidence": 0.75}