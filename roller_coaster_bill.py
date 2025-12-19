print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Your ticket is $5.")
    elif age <= 18:
        bill = 7
        print("Your ticket is $7.")
    else:
        bill = 12
        print("Your ticket is $12.")

    photos = input("Do you want photos? (y/n)")
    if photos == "y":
        bill += 3
else:
    print("Sorry you have to grow taller before you can ride.")

print(f"Your total bill is ${bill}")