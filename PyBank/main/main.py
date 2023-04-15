import os
import csv

print("Financial Analysis")
print("----------------------------")

csvpath = os.path.join('..', 'Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")

    total=0
    row_count = 0
    for row in csvreader:
        row_count += 1
        total += float(row[1])

    average = total / row_count

print(f"Total Month: {row_count}")
print(f"Total: $ {total}")
print(f"Average Change:$- {average}")