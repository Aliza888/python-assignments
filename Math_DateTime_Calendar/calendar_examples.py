# Calendar Module Examples
#calendar module se hum saal/mahine ka calendar print kar saktay hain aur leap years check kar saktay hain.
import calendar

# Print full calendar of a year
print("Full Calendar of 2025:")
print(calendar.calendar(2025))

# Print calendar of a specific month
print("Calendar of May 2025:")
print(calendar.month(2025, 5))

# Check if a year is a leap year
print("Is 2024 a leap year?", calendar.isleap(2024))

# Count leap years between two years
print("Number of leap years from 2000 to 2025:", calendar.leapdays(2000, 2025))
