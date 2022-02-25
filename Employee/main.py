# Imports:
import random


class Employee:

    def __init__(self):
        # Constants
        self.WAGE_PER_HR = 20
        self.WR_DAY_PER_MONTH = 20
        self.MAX_WRK_HR = 100

        self.switcher = {
            0: {"Status": "ABSENT", "Working_Hr": 0},
            1: {"Status": "PRESENT", "Working_Hr": 12},
            2: {"Status": "PART_TIME", "Working_Hr": 8}
        }

    def working_hr(self):
        """
        get work hour of particular day of employee
        :return: work_hr:number of hours employee worked in particular day
        """
        attendance = random.randint(0, 2)
        work_hr = self.switcher.get(attendance).get("Working_Hr")
        return work_hr

    def calculate_total_wage(self):
        """
        Calculate wage of an Employee
        :return: total_wage:monthly wage of an Employee
        """
        total_wage = 0
        temp_day = 1
        temp_hr = self.MAX_WRK_HR
        daily_wage = {}
        while temp_day <= self.WR_DAY_PER_MONTH and temp_hr > 0:
            working_hours = self.working_hr()
            wage = working_hours * self.WAGE_PER_HR
            daily_wage.__setitem__(temp_day,wage)
            temp_hr -= working_hours
            temp_day += 1
            total_wage += wage
        return daily_wage, total_wage


if __name__ == "__main__":
    employee = Employee()
    daily, monthly = employee.calculate_total_wage()
    print(f"Daily Wages:\n{daily}")
    print(f"Monthly Wage:{monthly}")
