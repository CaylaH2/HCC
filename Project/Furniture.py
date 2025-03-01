itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00
profit = (retailPrice) - (wholesalePrice)
salePrice = (retailPrice) * 0.75
saleProfit = (salePrice) - (wholesalePrice)

print("Item Name: ", itemName)
print("Retail Price: $", format(retailPrice, ".2f"), sep="")
print("Wholesale Price: $", format(wholesalePrice, ".2f"), sep="")
print("Profit: $", format(profit, ".2f"), sep="")
print("Sale Price: $", format(salePrice, ".2f"), sep ="")
print("Sale Profit: $", format(saleProfit, ".2f"), sep="")
