'''
Mini Project 3: ATM Withdrawal System
'''
name = input("Enter account holder name: ")
balance = float(input("Enter current balance: "))
withdraw = float(input("Enter withdrawal amount: "))

print("\n----- ATM TRANSACTION -----")
print("Account Holder :", name)

if withdraw <= 0:
    print("Transaction Status : Rejected")
    print("Reason             : Withdrawal amount must be greater than Rs. 0")
else:
    if withdraw > balance:
        print("Transaction Status : Rejected")
        print("Reason             : Insufficient balance")
    else:
        if withdraw > 20000:
            print("Transaction Status : Rejected")
            print("Reason             : Maximum limit per transaction is Rs. 20,000")
        else:
            remaining = balance - withdraw
            print("Transaction Status : Successful")
            print("Withdrawn Amount   : Rs.", withdraw)
            print("Remaining Balance  : Rs.", remaining)
            if remaining < 1000:
                print("Low Balance Warning")
