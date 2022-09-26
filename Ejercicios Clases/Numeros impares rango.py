from re import I


num = (input("Enter a number:"))
if num.isnumeric():
    num=int(num)
    for i in range(1, num +1, 2):
        if i >=num-1:
            print(i)
        else:
            print(i, end=",")
else:
    print("Invalid")
    
