import os
import csv


csvpath = os.path.join('..', 'Resources','budget_data.csv')


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")
    months_count = 0
    profit_losses = 0
    previous_profit_loss = None
    changes = []
    dates =[]
  
  #loop through rows to count the total rows
  #loop through rows to count the total of profit/losses  
    
    for row in csvreader:
        date = row[0]
        months_count += 1
        profit_losses += float(row[1])
        profit_loss = int(row[1])
        dates.append(date)

#to generate a list of the profit change of each month period 

        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
        
        previous_profit_loss = profit_loss

# analyze the the changes

average_change = sum(changes) / len(changes)
greatest_increase = max(changes)
greatest_decrease = min(changes)


greatest_increase_date = dates[changes.index(greatest_increase)+ 1]
greatest_decrease_date = dates[changes.index(greatest_decrease)+ 1]


print("Financial Analysis")
print("----------------------------")
print(f"Total Month: {months_count}")
print(f"Total: $ {profit_losses}")
print(f"Average Change: ${average_change:,.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} ({greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease})")

# write the results to a text file

file_to_output = os.path.join("..","analysis", "election_analysis.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Month: {months_count}\n")
    txt_file.write(f"Total: $ {profit_losses}\n")
    txt_file.write(f"Average Change: ${average_change:,.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} ({greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} ({greatest_decrease})\n")