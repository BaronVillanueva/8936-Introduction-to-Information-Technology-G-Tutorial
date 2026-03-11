# WEEK 4 TUTORIAL
# Step 1 — Your first print
#print('Welcome to the Python Coffee Shop!\n')

# Step 2 — Ask for a name
#customer_name = input('What is your name? ')
#print("Hello, " + customer_name + "! Let's order some coffee <3")

# Step 3 — Prices (numbers)
#price_coffee = 3.5
#price_latte = 4.0
#print("Coffee: $" + str(price_coffee))
#print("Latte: $" + str(price_latte))

# Step 6 — A short list
#menu_items = ["coffee","latte","espresso"]
#print("Our menu: ", menu_items)

# Put it together — Complete starter program
'''print("Welcome to the Python Coffee Shop!")

customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some coffee.")

price_coffee = 3.50
price_latte = 4.00
price_mocha = 4.00
price_matcha = 5.00


print("Coffee: $" + str(price_coffee))
print("Latte: $" + str(price_latte))
print("Mocha: $" + str(price_coffee))
print("Matcha: $" + str(price_latte))

choice = input("What would you like to order? (coffee/latte/mocha/matcha): ").lower()
if choice == "coffee":
    cost = price_coffee
elif choice == "latte":
    cost = price_latte
elif choice == "mocha":
    cost = price_latte
elif choice == "matcha":
    cost = price_latte    
else:
    print("Sorry, we do not have that.")
    cost = 0

quantity = int(input("How many cups would you like? "))

total_cost = cost * quantity

if quantity > 1:
         print("You get a discount of $1.00!")
         total_cost -= 1.00
 
print("Your total is: $" + str(total_cost))
print("Thank you, " + customer_name + "! Please come again.")'''

# Student discount
'''print("Welcome to the Python Coffee Shop!")

customer_name = input("What is your name? ")
print("Hello, " + customer_name + "! Let's order some coffee.")

price_coffee = 3.50
price_latte = 4.00
price_mocha = 4.00
price_matcha = 5.00


print("Coffee: $" + str(price_coffee))
print("Latte: $" + str(price_latte))
print("Mocha: $" + str(price_coffee))
print("Matcha: $" + str(price_latte))

choice = input("What would you like to order? (coffee/latte/mocha/matcha): ").lower()
if choice == "coffee":
    cost = price_coffee
elif choice == "latte":
    cost = price_latte
elif choice == "mocha":
    cost = price_latte
elif choice == "matcha":
    cost = price_latte    
else:
    print("Sorry, we do not have that.")
    cost = 0

quantity = int(input("How many cups would you like? "))

total_cost = cost * quantity

student = input("\nAre you a student? (Y/N): ").lower()
if student == "y":
    print("You get a 10% student discount!")
    #total_cost -= (.1 * total_cost)
    total_cost *= 0.9
     

else:
    print("Sorry, you're not getting a student discount.")

print("Your total is: $" + str(total_cost))
print("Thank you, " + customer_name + "! Please come again.")'''

# Keep ordering until user says no
#c = set()
print("Welcome to the Python Coffee Shop!")

customer_name = input("What is your name? ")
flag = "y"
total = 0
while flag == "y":

    print("Hello, " + customer_name + "! Let's order some coffee.")

    price_coffee = 3.50
    price_latte = 4.00
    price_mocha = 4.00
    price_matcha = 5.00


    print("Coffee: $" + str(price_coffee))
    print("Latte: $" + str(price_latte))
    print("Mocha: $" + str(price_coffee))
    print("Matcha: $" + str(price_latte))

    choice = input("What would you like to order? (coffee/latte/mocha/matcha): ").lower()
    if choice == "coffee":
        cost = price_coffee
    elif choice == "latte":
        cost = price_latte
    elif choice == "mocha":
        cost = price_latte
    elif choice == "matcha":
        cost = price_latte    
    else:
        print("Sorry, we do not have that.")
        cost = 0

    quantity = int(input("How many cups would you like? "))
    flag = input("Would you like to order again? (Y/N): ").lower()

    total_cost = cost * quantity
    total+=total_cost

if quantity > 1:
         print("You get a discount of $1.00!")
         total -= 1.00
 
print("Your total is: $" + str(total))
print("Thank you, " + customer_name + "! Please come again.")
 
