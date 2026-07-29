
"""with open("data/user.json") as f:
    data= json.load(f)
"""

import json

data = {"name": "Kavya", "age": 21}

with open("data/user2.json", "w") as f:
    json.dump(data, f, indent=2)