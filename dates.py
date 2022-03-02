import pandas as pd
import csv
import collections


def nrOfDates(data, filesNames):
    # Get dates, first we get the date in ms then tranform it into date and time then split the date from the time and append just the date
    dates = []
    for i in range(1, len(filesNames)+1):
        for j in range(len(data[i])):
            dates.append(pd.to_datetime(data[i][j]['timestamp_ms'], unit='ms'))

    # Count dates
    allYears = pd.to_datetime(dates).year
    allYearsCounted = collections.Counter(allYears)

    # Write the dates on csv
    with open("dates.csv", mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Date'])
        for i in dates:
            writer.writerow([i])

    # Write the dates counter on csv
    date_counter_values = {"Date": [], "Count": []}
    with open("dateCounter.csv", mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Date' ' | ' 'Count'])
        for years in allYearsCounted:
            writer.writerow([years, allYearsCounted[years]])
            date_counter_values["Date"].append(years)
            date_counter_values["Count"].append(allYearsCounted[years])

    # Graph dates
    df = pd.DataFrame(date_counter_values)
    ax = df.plot.bar(x='Date', y='Count', rot=0)
    ax.bar_label(ax.containers[0])
