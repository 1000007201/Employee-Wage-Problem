# Imports:
import random

# Constants

attendence = random.randint(0,1)

switcher = {
    0:{"Status":"ABSENT"},
    1:{"Status":"PRESENT"}
}

print(switcher.get(attendence).get("Status"))
