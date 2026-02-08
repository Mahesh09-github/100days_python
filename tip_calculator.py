print("Welcome to the tip calculator!")
#Enter the total bill,tip percentage and number of people to split the bill
bill=float(input("What was the total Bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15"))
people = int(input("How many people to split the bill?"))

#converting the tip percentage to a decimal
tip_as_percent = tip/100

#Calculating the total tip amount 
total_tip_amount = bill*tip_as_percent

#Calculating total bill
total_bill = bill + total_tip_amount

#calcuating the amount each person should pay
bill_per_person = total_bill/people
final_amount= round(bill_per_person,2)

#Result
print(f"Each person should pay: ${final_amount}")