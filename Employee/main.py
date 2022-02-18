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

def working_hr():
    '''
    get work hour of particular day of employee
    :return: work_hr:number of hours employee worked in particular day
    '''
    attendance = random.randint(0, 2)
    work_hr = switcher.get(attendance).get("Working_Hr")
    return work_hr


def calculate_total_wage():
    '''
    Calculate wage of an Employee
    :return: total_wage:monthly wage of an Employee
    '''
    total_wage = 0
    for i in range(0, WR_DAY_PER_MONTH):
        working_hours = working_hr()
        wage = working_hours * WAGE_PER_HR
        total_wage += wage
    return total_wage


print(f"{calculate_total_wage()} is Monthly Wage")

