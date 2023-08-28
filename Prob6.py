#Prob6

# Chef's commute time in minutes
chef_commute_time = 30

# Input for how many minutes Chef left before he was supposed to reach
minutes_before_schedule = int(input("Enter the minutes Chef left before schedule: "))

if minutes_before_schedule == chef_commute_time:
    print("Chef will reach on time.")
elif minutes_before_schedule > chef_commute_time:
    print("Chef will reach early.")
else:
    late_minutes = chef_commute_time - minutes_before_schedule
    print("Chef will reach", late_minutes, "minutes late.")