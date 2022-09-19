
option = input("Please enter a valid option: \n1 -Vegetarian\n2- Non Vegetarian\n->")
if option == "1":
    ingredient = int(input("Choose one ingredient: \n1-Pimiento\n2- Tofu\n->"))
    if ingredient == 1:
        ingredient = "Pimiento"
    else:
        ingredient = "Tofu"
    print(f"Your pizza is Vegetarian and have this ingredient {ingredient}")
elif option == "2":
    ingredient = int(input("Choose one ingredient: \n1-Jam\n2- Salmon\n->"))
    if ingredient == 1:
        ingredient = "Jam"
    else:
        ingredient = "Salmon"
    print(f"Your pizza is Non Vegetarian and teh ingredient you chose is {ingredient}")
else: 
    print("Invalid option")
