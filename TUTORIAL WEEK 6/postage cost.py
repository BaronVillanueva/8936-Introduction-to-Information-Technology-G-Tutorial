def cost(ounces):
    return 0.05 + (0.10*ceil(ounces-1))

def ceil(ounces):
    if int(ounces) != ounces:
        return int(ounces+1)
    else:
        return ounces
 
def getInput():
    'Getting weight of postage rom user'
    return float(input("Enter number of ounces: "))

def showOutput(cost):
    print("Cost: ${0:.2f}".format(cost))

def main():
    #INPUT -> PROCESS -> OUTPUT
    ounces = getInput()
    postageCost = cost(ounces)
    showOutput(postageCost)

main()
