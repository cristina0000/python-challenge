# Imports
import csv
import os

# input and output files
input_file = os.path.join("Resources", "budget_data.csv")
output_file = os.path.join("Resources", "pybank_analysis.txt")

# initialize variables needed for calculations
total_no_months = 0
change_list = []
greatest_increase_profits = ["", 0]
greatest_decrease_losses = ["", 9999999999999999]
total_net_profit_or_loss = 0

# Read the input file
with open(input_file) as budget_data:
    reader = csv.reader(budget_data)

    # header row
    header = next(reader)
    # to get 
    # get first row
    first_row = next(reader)
    total_no_months += 1
    total_net_profit_or_loss += int(first_row[1])
    previous_net = int(first_row[1])

    #for loop
    for row in reader:

        total_no_months += 1
        total_net_profit_or_loss += int(row[1])

        # construct the list of changes
        change = int(row[1]) - previous_net
        previous_net = int(row[1])
        change_list += [change]
       

        # Determine greatest increase in profits
        if change > greatest_increase_profits[1]:
            greatest_increase_profits[0] = row[0]
            greatest_increase_profits[1] = change

        # Determine greatest decrease in lossees
        if change < greatest_decrease_losses[1]:
            greatest_decrease_losses[0] = row[0]
            greatest_decrease_losses[1] = change

# Calculate the Average of changes over the whole period
avg_of_changes = sum(change_list) / len(change_list)

# Generate Financial analysis
budget_output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_no_months}\n"
    f"Total: ${total_net_profit_or_loss}\n"
    f"Average  of Changes: ${avg_of_changes:.1f}\n"
    f"Greatest Increase in Profits: {greatest_increase_profits[0]} (${greatest_increase_profits[1]})\n"
    f"Greatest Decrease in Losses: {greatest_decrease_losses[0]} (${greatest_decrease_losses[1]})\n")

# Print analysis to teminal
print(budget_output)

# Export a text file with the results
with open(output_file, "w") as txt_file:
    txt_file.write(budget_output)
