print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15: "))
tip = 1 + tip/100
people = int(input("How many people to split the bill? "))

total = round((bill * tip)/people, 2)
print(f"Each person should pay ${total}")