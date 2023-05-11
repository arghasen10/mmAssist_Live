import csv
from datetime import datetime, timedelta

# username_activity_b/a.csv
filename = 'heamanth_rear_back_b.csv'
with open(filename, 'w') as file:
    fieldnames = ['Datetime', 'Activity', 'User']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

start_time = datetime.strptime("2023-05-09 22:21:41", "%Y-%m-%d %H:%M:%S")
end_time = datetime.strptime("2023-05-09 22:25:10", "%Y-%m-%d %H:%M:%S")

curr_time = start_time
while curr_time < end_time:
    with open(filename, 'a') as file:
        fieldnames = ['Datetime', 'Activity', 'User']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow({'Datetime': curr_time, 'Activity': 'rear_back' ,'User': 'Heamanth'})

    curr_time += timedelta(seconds=1)

