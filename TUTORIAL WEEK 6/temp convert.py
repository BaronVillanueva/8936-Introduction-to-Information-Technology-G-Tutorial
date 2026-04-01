def calculate(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
 
def getInput():
    'GET TEMP AND CONVERT TO CELSIUS'
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    return fahrenheit

def showOutput(celsius):
    print("Temperature is {0:.2f} degrees Celsius".format(celsius))

def main():
    #INPUT -> PROCESS -> OUTPUT
    fahrenheit = getInput()
    celsius = calculate(fahrenheit)
    showOutput(celsius)

main()
