# Imports:
import random


# Constants
WAGE_PER_HR = 20
WR_DAY_PER_MONTH = 20


switcher = {
    0: {"Status": "ABSENT", "Working_Hr": 0},
    1: {"Status": "PRESENT", "Working_Hr": 12},
    2: {"Status": "PART_TIME", "Working_Hr": 8}
}


def calculate_total_wage():
    total_wage = 0
    for i in range(0, WR_DAY_PER_MONTH):
        attendance = random.randint(0, 2)
        wage = switcher.get(attendance).get("Working_Hr") * WAGE_PER_HR
        total_wage += wage
    return total_wage


print(f"{calculate_total_wage()} is Monthly Wage")

