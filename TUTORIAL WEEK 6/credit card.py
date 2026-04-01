rate = 0.015
def calculate(oldBal,charges,credit):
    newBal = (oldBal*rate) + charges - credit + oldBal
    if newBal <= 20:
        minPayment = newBal
    else:
        minPayment = 20 + 0.10 * (newBal-20)
    return newBal,minPayment
 
def getInput():
    'GET OLD BALANCE AND CHARGES'
    oldBal = float(input("Enter old balance: "))
    charges = float(input("Enter charges: "))
    credit = float(input("Enter credits: "))
    return oldBal,charges,credit

def showOutput(newBal,minPayment):
    print("New Balance: ${0:.2f}\nMinmimum Payment: ${1:.2f}".format(newBal,minPayment))

def main():
    #INPUT -> PROCESS -> OUTPUT
    oldBal,charges,credit = getInput()
    newBal,minPayment = calculate(oldBal,charges,credit)
    showOutput(newBal,minPayment)

main()
