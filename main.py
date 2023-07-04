
print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip = input("How many percentage tip would you like to give? ")
people = input("How many people to split the bill? ")
final= (float(total_bill) / int(people))* (1+int(tip)/100)
final=("{:.2f}".format(final))
print(f"Each person should pay: ${final}")
