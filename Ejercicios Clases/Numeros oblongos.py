num = int(input("Enter a number: "))
oblongo= False
for numeros in range(num):
    consecu=numeros+1
    if numeros*(consecu)==num:
        oblongo = True
        print(f"{num} es número oblongo")
        break
    elif oblongo:
        print(f"{num} no es número oblongo")



