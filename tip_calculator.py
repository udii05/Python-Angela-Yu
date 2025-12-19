print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people to split the bill?"))

total_bill = bill + (bill * (tip / 100))
split_bill = round(total_bill / people, 2)
print(f"Each person should pay: ${split_bill}")
