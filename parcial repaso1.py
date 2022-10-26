
def print_welcome():
    print("WELCOME...")
def get_option(studies):
    for types, descriptions in studies.item():
        for key, price in descriptions.items():
            print(f"{types} - {price}", end=",")
        print("")
    return input("Please enter an option: ")
def get_client_data(study):
    client = {
        "ID": input("Please enter your ID: "),
        "Name": input("Please enter your name: "),
        "Age": input("Please enter your age: "),
        "Gender": input("Please enter your Gender: "),
        "Study": study 

        
            }
    return client
def print_invoice(client, studies):
    print("--- RECEIPT ---")

def main():
    studies_dict ={
            "U": { "description":"ultrasonido","price": 8900},
            "T": { "description":"tomografia","price": 12640},
            "R": { "description":"resonancia","price": 15600}
        }
    
    clients = []
    print_welcome()
    option = get_option(studies_dict)
    client = get_client_data(option)
    main()
