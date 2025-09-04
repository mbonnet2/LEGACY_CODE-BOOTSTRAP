def main():
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
                print(f"total")
            case "2":
                print(f"credit")
            case "3":
                print(f"debit")
            case "4":
                print(f"exit")
                break
            case _:
                print(f"Invalid choice, please select 1-4.")

if __name__ == "__main__":
    main()