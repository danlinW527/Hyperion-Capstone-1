import math

type = " "

while True:
    type = input("""
Choose either 'investment' or 'bond' from the menu below to proceed:
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
""")
#cast the input into lower case so that it will be valid#
    type_lower = type.lower()

#For users who entered an invalid option, back to the first while True#
    if type_lower != "investment" and type_lower != "bond":
        print("Please enter a valid type from the menu below.")
        continue
    elif type_lower == "investment":
        deposit = float(input("Please enter the amount of money you are depositing: "))
        interest_rate = float(input("""
Please enter the 'x' percent of you annual interest rate. 
For example if your annual interest rate is 4%, you should enter 4: 
"""))
        time = int(input("Please enter the number of years you plan on investing: "))
        interest_type = " "
        while True:
            interest_type = input("Please choose 'simple' or 'compound' for your interest type: ")
            interest_type_lower = interest_type.lower()
#For users who entered invalid interest type, back to the 2nd while True#
            if interest_type_lower != "simple" and interest_type_lower != "compound":
                print("please enter a valid interest type")
                continue
#if the interest type is simple, use the given formula to calculate the total money#
            elif interest_type_lower == "simple":
                invest_total = round(deposit * (1+ interest_rate / 100 * time), 2)
                print(f"If you choose simple rate, you will get back approximately {invest_total} after {time}'s year of investment.")
#if the interest type is compound, use the given formular to calculate the total money#
            elif interest_type_lower == "compound":
                compound_total = round(deposit * math.pow((1+ interest_rate/100),time),2)
                print(f"If you choose compound rate, you will get back approximately {compound_total} after {time}'s year of investment.")
            break
    elif type_lower == "bond":
        value = float(input("Please enter the present value of the house: "))
        interest_rate_b = float(input("""
Please enter the 'x' percent of you annual interest rate.
For example if your annual interest rate is 4%, you should enter 4: 
"""))
        monthly_interest_rate = interest_rate_b / 100 / 12
        months = int(input("Please enter the number of months you plan to take to repay the bond: "))
#note, the formula was provided during the lecture, as the one in the Tast 12 is incorrect#
        monthly_bond = round((monthly_interest_rate * value) / (1 - (1 + monthly_interest_rate) ** (-months)),2)
        print(f"To borrow house value of {value} for {months} months with {interest_rate_b} percent interest rate, you will pay approximately {monthly_bond} per month.")
    break





