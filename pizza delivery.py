print("Welcome to Pizza Delivery!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni in your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

if size == "S":
    pizza = 15
    if pepperoni == "Y":
        pizza = pizza + 2   
    elif pepperoni == "N":
        pizza = 15
elif size == "M":
    pizza = 20
    if pepperoni == "Y":
        pizza = pizza + 3
    elif pepperoni == "N":
        pizza = 20
else:
    pizza = 25
    if pepperoni == "Y":
        pizza = pizza + 3
    elif pepperoni == "N":
        pizza = 25

if extra_cheese == "Y":
    pizza = pizza + 1

print(f"Your total bill is: ${pizza}")