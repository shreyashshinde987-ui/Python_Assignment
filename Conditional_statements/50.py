'''
50. Write a program to build a simple ATM menu using a match case.
'''
balance = 10000
pin = 1234

entered_pin = int(input("Enter your 4-digit PIN: "))

if entered_pin != pin:
    print("Incorrect PIN. Access denied.")
else:
    while True:
        print("\n------ ATM MENU ------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        match choice:
            case 1:
                print("Current balance: Rs.", balance)
            case 2:
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print("Deposited. New balance: Rs.", balance)
                else:
                    print("Invalid amount")
            case 3:
                amount = float(input("Enter amount to withdraw: "))
                if amount <= 0:
                    print("Invalid amount")
                elif amount > balance:
                    print("Insufficient balance")
                else:
                    balance -= amount
                    print("Please collect cash. New balance: Rs.", balance)
            case 4:
                print("Thank you for using the ATM")
                break
            case _:
                print("Invalid choice")
