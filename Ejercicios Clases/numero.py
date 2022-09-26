num=int(input("Please enter a number:"))

suma = 0
for divisor in range(1, num):
    if num%divisor==0:
        
        suma+=divisor
if suma == num:
    print(f"{num} is a perfect number")
        
else: 
    print(f"{num} is not a perfect number")