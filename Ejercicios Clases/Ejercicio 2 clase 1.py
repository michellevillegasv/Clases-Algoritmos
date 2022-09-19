
number = (input("Enter a number: "))
is_valid = True

if number.isnumeric():
    number = float(number)
else:
    is_valid = False
if is_valid:
    if(number % 2 == 0):
        print("The number is even")
    else: 
        print("The number is odd")
else:
    print("Invalid")

    