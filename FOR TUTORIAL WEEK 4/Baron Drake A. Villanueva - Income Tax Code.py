income = float(input("State your income: "))
 
if income <= 20000:
    tax = 0.2*income
 
else:
    if income <= 50000:
        tax = 400 + 0.25 * (income - 20000)
        
    else:
        tax = 1150 + 0.35 * (income - 50000)
 
print("Your tax is: ", "%.2f" %float(tax))
 
