import json

result = []

with open("PAYDAY 2 Skills.csv", encoding="shift_jis") as f:
    for line in f.readlines()[1:]:
        t = line.split(",")
        result.append({
            "category": t[0],
            "subcategory": t[1],
            "tier": int(t[2]),
            "title": t[3],
            "basic": {
                "description": t[4],
                "point": int(t[5]),
                "recommended_plan": t[6].split("~")
            },
            "ace": {
                "description": t[7],
                "point": int(t[8]),
                "recommended_plan": t[9].replace("\n", "").split("~")
            }
        })

json.dump(result, open("skills.json", "w"))
