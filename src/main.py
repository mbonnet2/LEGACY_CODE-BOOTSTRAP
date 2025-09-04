from data import AccountData
from operation import AccountManager, OperationFactory

def main():
    manager = AccountManager()

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
                amount = float(input("Enter credit amount: "))
                op = OperationFactory.get_operation('CREDIT', amount)
            case "3":
                amount = float(input("Enter debit amount: "))
                op = OperationFactory.get_operation('DEBIT', amount)
            case "4":
                print(f"Exiting the program. Goodbye!")
                break
            case _:
                print(f"Invalid choice, please select 1-4.")
                continue
        
        manager.perform_operation(op)

if __name__ == "__main__":
    main()