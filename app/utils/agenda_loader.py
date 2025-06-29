import json
from pathlib import Path

def load_agenda_for_day(day: str) -> dict:
    syllabus_path = Path("app/data/syllabus.json")
    if not syllabus_path.exists():
        return {"topic": "No agenda found", "objectives": [], "concepts": []}

    with open(syllabus_path, "r") as f:
        syllabus = json.load(f)

    return syllabus.get(day, {"topic": "Not found", "objectives": [], "concepts": []})
