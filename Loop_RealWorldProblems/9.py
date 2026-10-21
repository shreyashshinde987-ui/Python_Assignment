'''
Mini Project 9: Bank Transaction History
'''
balance = float(input("Enter opening balance: Rs. "))
count = int(input("Enter number of transactions: "))

if balance < 0 or count <= 0:
    print("Error: Balance cannot be negative and transactions must be greater than 0")
else:
    deposits = 0
    withdrawals = 0
    rejected = 0

    for i in range(1, count + 1):
        print(f"\n--- Transaction {i} ---")
        t_type = input("Enter type (D = Deposit, W = Withdraw): ").strip().upper()
        while t_type != "D" and t_type != "W":
            print("Invalid type. Enter D or W.")
            t_type = input("Enter type (D = Deposit, W = Withdraw): ").strip().upper()

        amount = float(input("Enter amount: Rs. "))
        while amount <= 0:
            print("Amount must be greater than 0. Try again.")
            amount = float(input("Enter amount: Rs. "))

        if t_type == "D":
            balance += amount
            deposits += 1
            print("Status: Deposit successful")
        else:
            if amount <= balance:
                balance -= amount
                withdrawals += 1
                print("Status: Withdrawal successful")
            else:
                rejected += 1
                print("Status: Withdrawal rejected (insufficient funds)")

    print("\n----- ACCOUNT SUMMARY -----")
    print("Final Balance            : Rs.", balance)
    print("Deposit Count            :", deposits)
    print("Successful Withdrawals   :", withdrawals)
    print("Rejected Withdrawals     :", rejected)

    if balance < 1000:
        print("Warning: Balance is below Rs. 1,000")
