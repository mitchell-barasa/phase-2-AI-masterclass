import json

with open("nairobi_report.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data["weather"]["main"]["temp"])
print(data["weather"]["weather"][0]["description"])