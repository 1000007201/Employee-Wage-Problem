# Imports:
import random

# Constants
WAGE_PER_HR = 20

attendance = random.randint(0, 2)
# 0-->ABSENT
# 1-->PRESENT
# 2-->PART_TIME

switcher = {
    0:{"Status": "ABSENT","Working_Hr": 0},
    1:{"Status": "PRESENT","Working_Hr": 12},
    2:{"Status": "PART_TIME","Working_Hr": 8}
}
wage = switcher.get(attendance).get("Working_Hr") * WAGE_PER_HR
print(f"{wage} is Daily Wage")

