a = [[1, 2, 3], [4, 5, 6]]
B = [[-1, 0], [0, 1] [1,1]]

for list in a: 
    for num in list:
        num=int(num)
        num=[list[num]]
for listB in B:
    for numB in listB:
        numB=int(num)
        numB=[list[numB]]
product=num*numB
print(product)
