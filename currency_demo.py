"""
Currency Converter Demo
Demonstrates Day 1 → Day 4
"""

# -------------------- DAY 1 --------------------
print("\n===== DAY 1: Basic Input + Conversion =====")

for i in range(2):  # Reduced for demo (you can keep 4)
    print(f"\n--- Transaction {i+1} ---")
    currency = input("Enter currency (USD, EUR, JPY, GBP): ").upper()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print(" Invalid amount")
        continue

    print("Currency entered:", currency)
    print("Amount entered:", amount)

    if currency == "USD":
        converted_amount = amount * 132
    elif currency == "EUR":
        converted_amount = amount * 145
    elif currency == "JPY":
        converted_amount = amount * 9.4
    elif currency == "GBP":
        converted_amount = amount * 198
    else:
        print("❌ Unsupported currency")
        continue

    print("Converted amount in NPR:", converted_amount)


# -------------------- DAY 2 --------------------
print("\n===== DAY 2: Functions =====")

def convert_currency(amount, rate):
    return amount * rate

def get_currency_rate(currency):
    rates = {"USD": 132, "EUR": 145, "INR": 1.6, "JPY": 9.4, "GBP": 198}
    return rates.get(currency, None)

currency_input = input("\nEnter a currency to get its rate: ").upper()
rate = get_currency_rate(currency_input)
if rate is not None:
    print(f"Rate for {currency_input} is {rate}")
else:
    print(" Currency not supported")


# -------------------- DAY 3 --------------------
print("\n===== DAY 3: Save Conversion to File =====")

def save_conversion(currency, amount, result):
    with open("currency_history.txt", "a") as file:
        file.write(f"{currency} {amount} -> NPR {result}\n")

# Example save
save_conversion("USD", 100, 13200)
print("Saved example conversion: USD 100 -> NPR 13200")


# -------------------- DAY 4 --------------------
print("\n===== DAY 4: Full System with List, Tuple, Set =====")

exchange_rates = [
    ("USD", "NPR", 132),
    ("INR", "NPR", 1.6),
    ("EUR", "NPR", 145),
    ("GBP", "NPR", 198),
    ("JPY", "NPR", 9.4)
]

conversion_request = []
unique_currencies = set()

def get_rate_to_npr(source):
    for rate in exchange_rates:
        if rate[0] == source and rate[1] == "NPR":
            return rate[2]
    return None

def add_conversion_request():
    name = input("Enter your name: ")
    source = input("Enter source currency: ").upper()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print(" Invalid amount")
        return

    rate = get_rate_to_npr(source)
    if rate is None:
        print(" Currency not supported")
        return

    converted_amount = amount * rate
    request = {"Name": name, "Source": source, "Target": "NPR", "Amount": amount}
    conversion_request.append(request)
    unique_currencies.add(source)
    print(f"{name} converted {amount} {source} -> {converted_amount:.2f} NPR")
    save_conversion(source, amount, converted_amount)

def print_conversion_report():
    if not conversion_request:
        print("No conversions yet.")
        return
    print("\n Conversion Report:")
    for req in conversion_request:
        converted_amount = req["Amount"] * get_rate_to_npr(req["Source"])
        print(req["Name"], "converted", req["Amount"], req["Source"], "to", converted_amount, "NPR")
    print("Unique currencies used:", unique_currencies)

num_request = int(input("\nHow many conversions do you want to enter for full system? "))
for i in range(num_request):
    add_conversion_request()

print_conversion_report()
print("\nDemo complete! Conversion history also saved in currency_history.txt")