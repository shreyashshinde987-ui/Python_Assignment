'''
Mini Project 9: Insurance Premium Calculator
'''
name = input("Enter customer name: ")
age = int(input("Enter age: "))
risk = input("Enter occupation risk (Low/Medium/High): ").strip().lower()
smoker = input("Smoker (Yes/No): ").strip().lower()

print("\n----- INSURANCE PREMIUM -----")
print("Customer Name :", name)

if age < 0:
    print("Error: Age cannot be negative")
elif age < 18:
    print("Eligibility   : Not Eligible (age below 18)")
else:
    if risk != "low" and risk != "medium" and risk != "high":
        print("Error: Occupation risk must be Low, Medium or High")
    elif smoker != "yes" and smoker != "no":
        print("Error: Smoker must be Yes or No")
    else:
        base_premium = 10000
        additional = 0

        if age > 50:
            additional = additional + 5000

        if risk == "high":
            additional = additional + 7000
        elif risk == "medium":
            additional = additional + 3000

        if smoker == "yes":
            additional = additional + 5000

        final_premium = base_premium + additional

        if additional >= 10000:
            message = "High Risk Policy"
        else:
            message = "Standard Risk Policy"

        print("Eligibility        : Eligible")
        print("Base Premium       : Rs.", base_premium)
        print("Additional Charges : Rs.", additional)
        print("Final Premium      : Rs.", final_premium)
        print("Risk Message       :", message)
