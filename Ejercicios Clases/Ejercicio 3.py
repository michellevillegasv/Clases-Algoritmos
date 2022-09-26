num = input("Enter a number:")
if num.isnumeric():
    num=int(num)
    for i in range(1,num*2,2):
        aux = i
        while aux >= 1:
            if aux == 1:
                print(aux)
            else:
                print(aux, end=" ")
            aux-=2
else:   
    print("Invalid")