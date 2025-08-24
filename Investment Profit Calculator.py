# Investment Profit Calculator

# Get user inputs
while True:
    try:
        invest = float(input("💰 Enter your investment amount: "))
        if invest > 0:
            break
        print("Investment must be greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        rate = float(input("📈 Enter annual interest rate (%): "))
        if rate > 0:
            break
        print("Rate must be greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        time = int(input("⏳ Enter investment duration (in years): "))
        if time > 0:
            break
        print("Time must be greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    currency = input("💵 Choose currency ($ or £): ")
    if currency in ["$", "£"]:
        break
    print("Please choose only $ or £.")

# Calculation (Compound Interest Formula)
result = invest * pow(1 + rate / 100, time)

# Output
print(f"\n📊 After {time} years, your balance will be: {result:.2f} {currency}")