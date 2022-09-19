num1 = (input("Enter a number:"))
num2 = (input("Enter another number:"))
is_valid = True

if num1.isnumeric():
    num1 = float(num1)
else: 
    is_valid = False
if num2.isnumeric():
    num2 = float(num2)
else: 
    is_valid = False
if is_valid:    
    if(num2 == 0):
         print("Error, the divisor is 0")
    else:
        print(f"The result of the division is {num1 / num2}")
else: 
    print("Invalid numbers")