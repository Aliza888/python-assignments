# DateTime Module Examples
# Yahan pe hum current date, time aur koi specific date ko print kar rahe hain using datetime module.
from datetime import datetime, date, time

# Current date and time
now = datetime.now()
print("Current Date & Time:", now)

# Current date only
today = date.today()
print("Today's date is:", today)

# Creating specific date and time
new_year = datetime(2025, 1, 1)
print("New Year 2025 starts on:", new_year)
