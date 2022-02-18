# Imports:
import random


# Constants
WAGE_PER_HR = 20
WR_DAY_PER_MONTH = 20
MAX_WRK_HR = 100


switcher = {
    0: {"Status": "ABSENT", "Working_Hr": 0},
    1: {"Status": "PRESENT", "Working_Hr": 12},
    2: {"Status": "PART_TIME", "Working_Hr": 8}
}


def calculate_total_wage():
    total_wage = 0
    temp_day = WR_DAY_PER_MONTH
    temp_hr = MAX_WRK_HR
    while temp_day > 0 and temp_hr > 0:
        attendance = random.randint(0, 2)
        wage = switcher.get(attendance).get("Working_Hr") * WAGE_PER_HR
        temp_hr -= switcher.get(attendance).get("Working_Hr")
        temp_day -= 1
        total_wage += wage
    return total_wage


print(f"{calculate_total_wage()} is Monthly Wage")

