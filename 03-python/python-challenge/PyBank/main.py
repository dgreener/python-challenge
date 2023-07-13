#Imports modules csv and os
import csv
import os

#Sets the path for the CSV file with financial data
BANK_CSV_PATH = os.path.join("Resources", "budget_data.csv")

os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Gets data file
with open(BANK_CSV_PATH) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')
    csv_header = next(csvreader)

#Sets variable for total months to zero for counting and creates empty lists for the other parameters
    months = 0
    profit = []
    net_change_list = []
    max = ["",0]
    min = ["",0]

#Count the total months and the net amount of profit/loss over the time period
    first_row = next(csvreader)
    months +=1
    prev_profit_loss = int(first_row[1])

    total_net = int(first_row[1])

#Reading row by row, count the month-to-month change in profit/loss
    for row in csvreader:
        months +=1
        total_net = total_net + int(row[1])
        net_change = int(row[1]) - prev_profit_loss
        prev_profit_loss = total_net
        net_change_list.append(net_change)

#Use conditional to find months with greatest increase and greatest in profit (and amount of change)
        if net_change < min[1]:
            min[1] = net_change
            min[0] = row[0]

        if net_change > max[1]:
            max[1] = net_change
            max[0] = row[0]

#Calculate the average month-to-month change in profit/loss
    average = sum(net_change_list)/len(net_change_list)
    
#Prints out the calculated values 
    print("Financial Analysis")
    print("---------------------")
    print(f"Total months: {months}")
    print(f"Total: ${total_net}")
    print(f"Average: ${average: 0.2f}")
    print(f"Greatest Increase in Profits: {max}")
    print(f"Greatest Decrease in Profits: {min}")
    
#Outputs results to txt file
    output = os.path.join(".", 'output.text')
    with open(output, "w") as new:
        new.write("Financial Analysis")
        new.write("\n")
        new.write("---------------------")
        new.write("\n")
        new.write(f"Total Months: {months}")
        new.write("\n")
        new.write(f"Total: ${total_net}")
        new.write("\n")
        new.write(f"Average: ${average: 0.2f}")
        new.write("\n")
        new.write(f"Greatest Increase in Profits: {max}")
        new.write("\n")
        new.write(f"Great Decrease in Profits: {min}")

    #Prints file to terminal
    with open(output, 'r') as readfile:
        print(readfile.read())          
