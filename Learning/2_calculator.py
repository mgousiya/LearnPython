# Python Compound Interest Calculator

principal = 0
interest_rate = 0
time = 0

while principal <= 0:
   principal = float(input("Enter your principal amount: "))
   if principal <= 0:
      print("Principal can't be less than or equal to zero")
    
while interest_rate <= 0:
   interest_rate = float(input("Enter the interest rate: "))
   if interest_rate <= 0:
      print("Interest rate can't be less than or equal to zero")

while time <= 0:
   time = int(input("Enter your time in years: "))
   if time <= 0:
      print("Time can't be less than or equal to zero")


total_amount = principal * pow((1 + interest_rate/100), time)
print(f"Balance after {time} years. ${total_amount:.2f}")