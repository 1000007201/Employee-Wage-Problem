# Imports:
import random

# Constants
PRESENT = 1
ABSENT = 0

attendence = random.randint(0,1)

switcher = {
    0:{"Status":"ABSENT"},
    1:{"Status":"PRESENT"}
}

print(switcher.get(attendence).get("Status"))
