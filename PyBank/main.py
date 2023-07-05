import os
import csv

#create the path to the file
csvpath = os.path.join('Resources', 'budget_data.csv')

#open the file 
with open(csvpath, 'r') as file:
    csv_reader = csv.reader(file)

    #skip header
    header = next(csv_reader)

    #state my variables
    total_months = 0
    net_loss = 0
    previous_loss = 0
    changes = []
    max_increase = ["", 0]
    max_decrease = ["", 0]

    for row in csv_reader:
        total_months += 1
        
        # Convert profit/loss to an integer
        profit_loss = int(row[1])

        # Calculate net loss
        net_loss += profit_loss

        # Calculate change in profit/loss from previous month
        change = profit_loss - previous_loss

        # Add change to the list of changes
        changes.append(change)

        # Update previous loss for the next iteration
        previous_loss = profit_loss

        # Check for the greatest increase in profits
        if change > max_increase[1]:
            max_increase = [row[0], change]

        # Check for the greatest decrease in profits
        if change < max_decrease[1]:
            max_decrease = [row[0], change]

    # Calculate the average change, excluding the first row (initial value)
    average_change = sum(changes[1:]) / (total_months - 1)

    # Print the financial analysis results
    print(f'Financial Analysis')
    print(f'---------------------------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${net_loss}')
    print(f'Average Change: ${average_change:.2f}')
    print(f'Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})')
    print(f'Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})')

    # Set variable output to the text I want to print in the text file
    output = f'Financial Analysis\n'
    output += f'---------------------------------------------\n'
    output += f'Total Months: {total_months}\n'
    output += f'Total: ${net_loss}\n'
    output += f'Average Change: ${average_change:.2f}\n'
    output += f'Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]})\n'
    output += f'Greatest Decrease in Profits: {max_decrease[0]} (${max_decrease[1]})\n'

    # Define the path and filename for the output text file
    output_file = os.path.join('analysis', 'Finacial_Analysis.txt')  

    # Write the output to the text file
    with open(output_file, 'w') as textfile:
        textfile.write(output)

    print(f'Financial analysis has been exported to {output_file} successfully.')