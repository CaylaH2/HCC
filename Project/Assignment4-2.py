#This program is for calculating an employee's productivity bonus based on their productivity score.

# Get user Input
employeeName = input("Enter Employee's name: ")
numShifts = int(input("Enter number of shifts: "))
numTransactions = int(input("Enter number of transactions: "))
transactionValue = float(input("Enter transaction dollar value: "))

# Calculate productivity score
if numShifts > 0 and numTransactions > 0:
    productivityScore = (transactionValue / numTransactions) / numShifts
else:
    productivityScore = 0

#Determine bonus
if productivityScore <= 30:
    bonus = 50.00
elif 31 <= productivityScore < 70:
    bonus = 75.00
elif 70 <= productivityScore <=199:
    bonus = 100.00
else:
    bonus = 200.00

#Display Results
print("Employee name:", employeeName)
print("Employee Bonus: $" + str(bonus))