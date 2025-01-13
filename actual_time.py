import ntplib
from time import ctime

# Create an NTP client
client = ntplib.NTPClient()

# Fetch the current time from an NTP server
response = client.request('pool.ntp.org')

# Print the accurate time
print("Current Accurate Time:", ctime(response.tx_time))
