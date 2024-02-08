# Welcome message
print("Welcome to tip calculator")
# Input: total bill amount
bill = int(input("What was the total bill?"))
# Input: number of people to split the bill
people = int(input("How many people to split the bill?"))
# Calculate individual share of the bill
split = bill / people
# Input: tip percentage
tip = int(input("What percent tip would you like to give? 10, 12, or 15?"))
# Calculate the total amount to be paid per person, including tip
final = float(split + split * (tip / 100))

# Format the final amount to two decimal places
final1 = "{:.2f}".format(final)

# Output the amount each person has to pay
print("You have to pay " + str(final1) + " each")

