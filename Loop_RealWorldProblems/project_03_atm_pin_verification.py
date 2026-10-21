'''
Mini Project 3: ATM PIN Verification
'''
correct_pin = 1234
max_attempts = 3
attempts = 0
access = False

while attempts < max_attempts:
    pin = int(input("Enter your PIN: "))
    attempts += 1

    if pin == correct_pin:
        access = True
        break
    else:
        remaining = max_attempts - attempts
        print("Incorrect PIN. Attempts remaining:", remaining)

print("\n----- ATM STATUS -----")
if access:
    print("Access Granted")
else:
    print("Card Temporarily Locked")
print("Attempts Used:", attempts)
