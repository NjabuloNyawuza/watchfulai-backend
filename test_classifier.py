from services.classifier import classify_report

test_messages = [
    "There is a suspicious man looking into cars on Oak Street",
    "Someone is trying to break into the house next door, please help!",
    "Good morning everyone, hope you all have a great day",
    "Unfamiliar bakkie driving slowly up and down Park Lane for 20 minutes",
    "Has anyone seen my cat? She went missing this afternoon",
    "3 men jumping over the wall at the school, looks suspicious",
    "HELP someone is being attacked outside the shop on Main Road",
    "Reminder: community meeting this Saturday at 10am",
    "Strange man sitting outside Gate 5 for the past hour, won't leave",
    "Does anyone know a good plumber in the area?"
]

print("Testing WatchfulAI Classifier")
print("=" * 50)

for message in test_messages:
    result = classify_report(message)
    print(f"\nMessage: {message}")
    print(f"Label: {result['label']} | Confidence: {result['confidence']}")

print("\n" + "=" * 50)
print("Test complete!")