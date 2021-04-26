#!/usr/bin/env python
# coding: utf-8

#Importing the CSV File.
import os
import csv
file = os.path.join('..', 'pybank', 'PyBank.csv')
with open('PyBank.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    #Lists 
    month_count = []
    profit = []
    change_profit = []
    
      #Make an Empty List
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
#Max/Min WRT List & Profit
increase = max(change_profit)
decrease = min(change_profit)

#Use the Index Data 
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1


print("Financial Analysis")
print("-------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)} USD")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)} USD")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))} USD)")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))} USD)")      

output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("-------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)} USD ")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)} USD")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))} USD)")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))} USD)")




