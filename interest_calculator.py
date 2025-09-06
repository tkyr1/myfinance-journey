#int calc

#get user input for the principal amount
# float() converts the text input into a number with decimals
principal = float(input("enter the principal amount: "))

#get user input for the annual interest rate
rate = float(input("enter the annual interest rate (e.g. 5 for %5): "))

#get user input for the time period in years
time = float(input("enter the time in years: "))

#calculate simple interest
# We divide the rate by 100 to convert it from a percentage to a decimal
simple_interest = principal * (rate / 100) * time

#calculate the total amount
total_amount = principal + simple_interest

#display the results using an f-string for nice formatting
print("\n--- Results ---")
print(f"principal amount: ${principal:,.2f}")
print(f"annual interest rate: {rate}%")
print(f"time: {time} years")
print(f"simple interest earned: ${simple_interest:,.2f}")
print(f"total amount after {time} years: ${total_amount:,.2f}")