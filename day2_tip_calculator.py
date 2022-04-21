## Tip calculator
## Gives user the message how much each person should pay, taking a tip into account

welcome_message = "Welcome to the tip calculator!"
print(welcome_message)

total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
no_of_people = int(input("How many people to split the bill? "))

tip = tip_percentage/100 + 1
result = total_bill * tip / no_of_people
result_rounded = round(result, 2)

result_message = f"Each person should pay: ${result_rounded}"
print(result_message)
