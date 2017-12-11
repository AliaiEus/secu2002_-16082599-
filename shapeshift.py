# TASK 3
# Creating a version of the data ordered by timestamp, where the timestamp is a datetime object

import csv
from datetime import datetime as dt

# Open the CSV file I want to pull the information from
f = open('/Users/aliai/secu2002_16082599/Lab09/shapeshift.csv', 'r')
# Create the reader object
reader = csv.DictReader(f)

# Open an empty list
list = []
# Iterate the rows of the file
for row in reader:
    # Select the timestamp row and convert it onto decimal digits
    time = dt.fromtimestamp(float(row['timestamp']))
    # The row selected is equal to the time
    row['timestamp'] = time
    # Add the row selected to the list I created above
    list.append(row)
# The list is ordered by timestamp
list.sort(key = lambda x : x['timestamp'])
# The mechanism is concluded and the result printed
print 'Sorted:', list



