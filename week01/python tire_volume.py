import math
from datetime import datetime
# python tire volume
print("python tire_volume.py")

# display current date
current_date = datetime.now().date()
print(f"current date {current_date:%Y-%m-%d}")

# The volume in MM
width=float(input("Enter the width of the tire in mm (ex 205):  "))

# Have the user enter the aspect ratio.
ratio=float(input("Enter the aspect ratio of the tire (ex 60): "))

# Have the user enter the diameter of the wheel in inches.
diameter=float(input("Enter the diameter of the wheel in inches (ex 15): "))


# Calculate the tire volume
volume = (math.pi * width**2 * ratio * (width * ratio + 2540 * diameter)) / 10000000000

# Display  result for the user to see

print(f"The approximate tire volume is {volume:.2f} liters")