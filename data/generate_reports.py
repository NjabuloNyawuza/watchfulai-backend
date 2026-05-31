import csv
import random
from datetime import datetime, timedelta

templates = [
    "I saw a man looking into cars on {street} around {time}",
    "Suspicious group of {num} people loitering near {street}",
    "Someone tried the gate on {street}, ran when they saw me",
    "Unfamiliar bakkie driving slowly on {street} for 20 mins",
    "Strange man sitting outside {street} for over an hour",
    "3 guys jumping over the wall at {street}, looked suspicious",
    "HELP someone is being attacked near {street}",
    "Unknown people trying car door handles on {street}",
    "Suspicious person with a hoodie walking up and down {street}",
    "Someone broke the streetlight on {street}, now its very dark",
    "Good morning everyone have a blessed day",
    "Has anyone seen a lost dog near {street}?",
    "Reminder: community meeting this Saturday at 10am",
    "Does anyone know a good plumber in the area?",
    "Load shedding schedule for this week just dropped",
]

streets = [
    "Oak Street", "Main Road", "Station Avenue",
    "Church Street", "Park Lane", "Berea Road",
    "Noord Street", "Commissioner Street", "Gate A",
    "Soweto Highway"
]

times = ["01:30", "02:15", "03:00", "22:45", "23:30", "00:15", "21:00"]
nums = ["2", "3", "4", "5"]

# Johannesburg area coordinates
BASE_LAT = -26.2041
BASE_LNG = 28.0473

rows = []
for i in range(200):
    street = random.choice(streets)
    time = random.choice(times)
    num = random.choice(nums)
    template = random.choice(templates)
    message = template.format(street=street, time=time, num=num)
    lat = BASE_LAT + random.uniform(-0.05, 0.05)
    lng = BASE_LNG + random.uniform(-0.05, 0.05)
    ts = datetime.now() - timedelta(hours=random.randint(0, 48))
    rows.append([message, round(lat, 6), round(lng, 6), ts.strftime("%Y-%m-%d %H:%M:%S"), street])

with open("data/fake_reports.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["message", "lat", "lng", "timestamp", "location_name"])
    writer.writerows(rows)

print(f"Generated {len(rows)} fake reports → data/fake_reports.csv")