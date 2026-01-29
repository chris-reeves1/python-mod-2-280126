# Conditionals:

# if, elif(else if), else

# basic_syntax

# if condition:
#     code to execute if condition is True
# else:
#     code to execute if none of the above conditions are True

# on_holiday = True
# is_admin = False
# is_verified = True

# if is_admin or is_verified and not on_holiday:
#     print("Access granted.")
# else:
#     print("Access denied.")

# import dis

# def disExample():
#     x = 0
#     while x < 3:
#         print("something")
#         x += 1

# dis.dis(disExample)

# temp = 35

# if temp > 30:
#     print("It's a hot day.")
# elif temp > 20:
#     print("It's a warm day.")
# elif temp > 10:
#     print("It's a cool day.")
# elif temp <= 10:
#     print("It's a cold day.")
# else:
#     print("It's a lovely day.")

# chanined comparison

# password = "password"
# deposit = 1000

# if not 0 < deposit < 5000 and password != "password":
#     print("Transaction denied.")
# else:   
#     print("You are allowed to make a withdrawal.")

# user = "admin"
# if user not in ("admin", "superuser", "root"):
#     print("Welcome, user!")
# else:
#     print("denied")

# Exercise:
# - weight converter
# - input for weight
# - input for unit (L for pounds, K for kilograms)
# - logic: check the unit entered
# - logic: calculate thwe converter value
# - print the converted value (nice format)
# - Error handling for invalid unit type (need to be k or l - upper/lower, while true)
# - optional stretch: error handle for non numeric weight input. 

# try:
#     result = 10 / 2
#     print(result)
# except ZeroDivisionError as e:
#     print(f"[ERROR] - cant divide by zero - {str(e)}")
# finally:
#     print("This will always execute.")

import sys

while True:
    try:    
        weight = int(input("Enter your weight: "))
        break
    except ValueError:
        print(f"[ERROR] - Invalid input. Please enter a numeric value for weight.")
        sys.exit() 

while True:
    unit = input("Enter the unit (L for pounds, K for kilograms): ").upper()
    if unit == "K":
        converted_weight = weight * 2.2
        print(f"Your weight in pounds is: {converted_weight:.2f} lbs")
        break
    elif unit == "L":
        converted_weight = weight / 2.2
        print(f"Your weight in kilograms is: {converted_weight:.2f} kgs")
        break
    else:
        print(f"Invalid unit. Please enter 'L' for pounds or 'K' for kilograms!!!")


    