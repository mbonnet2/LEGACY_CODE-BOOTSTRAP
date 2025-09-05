from data import AccountData
from operation import AccountManager, OperationFactory

def main():
    account = AccountData(1000)
    manager = AccountManager(account)

    while True:
        print("--------------------------------")
        print("Account Management System")
        print("1. View Balance")
        print("2. Credit Account")
        print("3. Debit Account")
        print("4. Exit")
        print("--------------------------------")

        choice = input("Enter your choice (1-4): ").strip()

        match choice:
            case "1":
                op = OperationFactory.get_operation('BALANCE')
            case "2":
                amount = input("Enter credit amount: ")
                try:
                    float_amount = float(amount)
                    op = OperationFactory.get_operation('CREDIT', float_amount)
                    manager.perform_operation(op)
                except:
                    print(f"Invalid operation type")
            case "3":
                amount = input("Enter debit amount: ")
                try:
                    float_amount = float(amount)
                    op = OperationFactory.get_operation('DEBIT', float_amount)
                    manager.perform_operation(op)
                except:
                    print(f"Invalid operation type")
            case "4":
                print(f"Exiting the program. Goodbye!")
                break
            case _:
                print(f"Invalid choice, please select 1-4.")
        
        

if __name__ == "__main__":
    main()