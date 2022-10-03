from multiprocessing import Value


dictionary = {}
while True: 
    key = input("Enter:")
    if key == "salir":
        break
    Value = input("")
    dictionary[key] = Value
    for key,value in dictionary.items():
        print(f"Your {key} is {value}")

