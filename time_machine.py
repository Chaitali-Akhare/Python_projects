import ntplib
from time import ctime, time
from datetime import datetime, timedelta

# Create an NTP client
client = ntplib.NTPClient()

# Fetch the current time from an NTP server
response = client.request('pool.ntp.org')

# Get the accurate time from NTP server and current system time
accurate_time = response.tx_time
system_time = time()

# Calculate the difference in seconds
time_difference = abs(system_time - accurate_time)

# Convert the difference into a timedelta object
time_diff = timedelta(seconds=time_difference)

# Break down the time difference
years, remainder = divmod(time_diff.days, 365)
months, remainder = divmod(remainder, 30)
weeks, days = divmod(remainder, 7)
hours, remainder = divmod(time_diff.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

# Print the accurate time
print()
print("Current Accurate Time:", ctime(accurate_time))

# Print the current system time
print("Current System Time:", ctime(system_time))

# Format the time difference output
time_diff_str = f"{years} years, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"

# Check if the difference is greater than 24 hours (1 day)
if time_diff.days > 0 or time_diff.seconds > 0:
    print("Warning: The time difference between the accurate time and your system time is greater than 24 hours.")
    print(f"Time Difference: {time_diff_str}")
    print("You should change the time of your system.")
else:
    print(f"Time Difference: {time_diff_str}")
    print("Your system time is within the acceptable range.")
