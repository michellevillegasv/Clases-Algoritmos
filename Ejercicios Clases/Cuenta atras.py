num = input("Enter a number:")
if num.isnumeric():
    num=int(num)
    for i in range(1,num+1):
        print("*"*i)
else:
    print("Invalid")
