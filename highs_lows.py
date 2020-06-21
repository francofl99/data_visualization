import csv
from matplotlib import pylab as plt
from datetime import datetime

# Get high temperatures from file 
filename = 'death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(current_date, 'Missing data')
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

# Plot data
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily high - low temperatures 2018\nDeath Valley, CA", fontsize=10)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(first_date)




