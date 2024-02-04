print("Welcome to tip calulator")
bill=int(input("What was the total bill?"))
people=int(input("How many people to split the bill?"))
split=bill/people
tip=int(input("What percent tip would you like to give? 10 12 or 15?"))
final=float(split+split*(tip/100))
final1="{:.2f}".format(final=float(split+split*(tip/100)))
print("you have to pay "+str(final1)+" each")
