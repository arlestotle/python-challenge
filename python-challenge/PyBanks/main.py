# Import Dependencies
import os
import csv
import shutil
from pathlib import Path 

# Read in the CSV
budget_csv = os.path.join("PyBanks", "Resources", "budget_data.csv")

# Create empty lists to store data
months_tot = []
profit_tot = []
profit_change = []

# Open csv
with open(budget_csv, newline="", encoding="utf-8") as budget:
    budgetcsv = csv.reader(budget, delimiter = ",")
    header = next(budgetcsv)

    # Look through the rows in the budget_data.csv to fill total months and profit total lists
    for row in budgetcsv:
        months_tot.append(row[0])
        profit_tot.append(int(row[1]))

    # Look through profits to fill monthly profit change list
    for i in range(len(profit_tot)-1):
        profit_change.append(profit_tot[i+1]-profit_tot[i])


# Use max and min function to find the min and max of the new profit_change list
max_increase = max(profit_change)
max_decrease = min(profit_change)

# match the max_increase and max_decrease with the monthly profit_change list
month_max_increase = profit_change.index(max(profit_change)) + 1
month_max_decrease = profit_change.index(min(profit_change)) + 1

# Create print statements to match output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months_tot)}")
print(f"Total: ${sum(profit_tot)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months_tot[month_max_increase]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {months_tot[month_max_decrease]} (${(str(max_decrease))})")

# Create new text file for summary output
financial_analysis = open("finanacial_analysis.txt","w")

financial_analysis.write("Financial Analysis" + "\n")
financial_analysis.write("----------------------------------------" + "\n")
financial_analysis.write(f"Total Months: {len(months_tot)}" + "\n")
financial_analysis.write(f"Total: ${sum(profit_tot)}" + "\n")
financial_analysis.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}" + "\n")
financial_analysis.write(f"Greatest Increase in Profits: {months_tot[month_max_increase]} (${(str(max_increase))})" + "\n")
financial_analysis.write(f"Greatest Decrease in Profits: {months_tot[month_max_decrease]} (${(str(max_decrease))})" + "\n")

financial_analysis.close()


