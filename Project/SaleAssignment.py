salary = float(input("Enter employee salary: "))
numDependents = int(input("Enter number of dependents: "))

stateTax = (salary) * 0.065
federalTax = (salary) * 0.28
dependentDeduction = (salary) * 0.025 * (numDependents)
totalWithholding = (stateTax) + (federalTax) + (dependentDeduction)
takeHomepay = (salary) - (totalWithholding)

print("State Tax: $", format(stateTax, ".2f"))
print("Federal Tax: $", format(stateTax, ".2f"))
print("Dependents: $", format(dependentDeduction, ".2f"))
print("Salary: $", format(salary, ".2f"))
print("Take-Home Pay: $", format(takeHomepay, ".2f"))
