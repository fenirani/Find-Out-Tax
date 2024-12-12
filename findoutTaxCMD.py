#Objective: Find tax in a certian split amount

print("Enter amount: $")
amount = float(input())
beforeTax = round(amount / 1.06625,2)
tax = round(amount - beforeTax, 2)

print("\n Tax is: $", tax )
print("\n Before Tax amount is ", beforeTax)


input("\n\n\nClose the window when ready")