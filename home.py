from db import create_database, get_connection

#------------------------------------------------Table Creation--------------------------------------------------------------------------------------

def create_table():
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS currency_conversions (
                    id SERIAL PRIMARY KEY,
                    from_currency VARCHAR(10),
                    to_currency VARCHAR(10),
                    amount NUMERIC,
                    converted_amount NUMERIC,
                    conversion_rate NUMERIC
                );
            """)
    conn.close()
    print("Table created!")

#------------------------------------------------------CRUD OPerations----------------------------------------------------------------------------------------------------

# CREATE
def insert_conversion(from_currency, to_currency, amount, converted_amount, conversion_rate):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO currency_conversions
                (from_currency, to_currency, amount, converted_amount, conversion_rate)
                VALUES (%s, %s, %s, %s, %s);
            """, (from_currency, to_currency, amount, converted_amount, conversion_rate))
    conn.close()
    print("Conversion saved successfully!")


# READ
def read_conversions():
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM currency_conversions;")
        records = cursor.fetchall()
        for record in records:
            print(record)
    conn.close()


# UPDATE
def update_conversion(record_id, new_amount, new_converted_amount):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                UPDATE currency_conversions
                SET amount = %s, converted_amount = %s
                WHERE id = %s;
            """, (new_amount, new_converted_amount, record_id))
    conn.close()
    print("Record updated successfully!")


# DELETE
def delete_conversion(record_id):
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                DELETE FROM currency_conversions
                WHERE id = %s;
            """, (record_id,))
    conn.close()
    print("Record deleted successfully!")


# """TASK 1:
# Program: Currency Input Program
# Objective:
# This program asks the user to enter a currency type and an amount.
# It checks if the amount entered is a valid number.
# Then it displays the currency and amount entered by the user.
# """

transactions = []

# """
# for i in range(4):
#     currency = input("Enter currency (USD or EUR or JPY or GBP): ")
#     amount = float(input("Enter amount: "))
#     print("Currency entered:", currency)
#     print("Amount entered:", amount)
#
#     if currency == "USD":
#         converted_amount = amount * 132
#     elif currency == "EUR":
#         converted_amount = amount * 145
#     elif currency == "JPY":
#         converted_amount = amount * 9.4
#     elif currency == "GBP":
#         converted_amount = amount * 198
#     else:
#         print("Unsupported currency.")
#         exit()
#
#     print("Converted amount in NPR:", converted_amount)
# """

# ---------------- FUNCTIONS ----------------

def convert_currency(amount, rate):
    return amount * rate


def get_currency_rate(currency):
    if currency == "USD":
        return 132
    elif currency == "EUR":
        return 145
    elif currency == "INR":
        return 1.6
    elif currency == "JPY":
        return 9.4
    elif currency == "GBP":
        return 198
    else:
        return None


# """
# currency_input = input("Enter the currency: ")
# rate = get_currency_rate(currency_input)
#
# if rate is not None:
#     print(f"The conversion rate for {currency_input} is: {rate}")
# """

# ---------------- FILE SAVE ----------------

def save_conversion(currency, amount, result):
    file = open("currency_history.txt", "a")
    file.write(f"{currency} {amount} -> NPR {result}\n")
    file.close()


# ---------------- DATA ----------------

exchanges_rates = [
    ("USD", "NPR", 132),
    ("INR", "NPR", 1.6),
    ("EUR", "NPR", 145),
    ("GBP", "NPR", 198),
    ("JPY", "NPR", 9.4)
]

conversion_request = []
unique_currencies = set()


def get_rate_to_nrp(source):
    for rate in exchanges_rates:
        if rate[0] == source:
            return rate[2]
    return None


def add_conversion_request():
    name = input("Enter your name: ")
    source = input("Enter source currency: ").upper()
    amount = float(input("Enter amount: "))

    rate = get_rate_to_nrp(source)
    if rate is None:
        print("Invalid currency")
        return

    converted_amount = amount * rate

    request = {
        "Name": name,
        "Source": source,
        "Target": "NPR",
        "Amount": amount,
    }

    conversion_request.append(request)

    print(f"{name} converted {amount} {source} to {converted_amount:.2f} NPR")


def print_conversion_report():
    if not conversion_request:
        print("No conversion to display")
        return

    for request in conversion_request:
        converted_amount = request["Amount"] * get_rate_to_nrp(request["Source"])
        print(request["Name"], request["Amount"], request["Source"], "->", converted_amount)


# ---------------- MENU ----------------

# --------- MENU DRIVEN TASK (MY PART) ---------

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Insert Data")
        print("2. Delete Data")
        print("3. Update Data")
        print("4. Show Report")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            source = input("Enter currency: ").upper()
            amount = float(input("Enter amount: "))
            rate = get_currency_rate(source)

            if rate is None:
                print("Invalid currency")
                continue

            converted = amount * rate
            insert_conversion(source, "NPR", amount, converted, rate)

        elif choice == "2":
            record_id = int(input("Enter ID: "))
            delete_conversion(record_id)

        elif choice == "3":
            record_id = int(input("Enter ID: "))
            amount = float(input("Enter new amount: "))
            rate = 132
            converted = amount * rate

            update_conversion(record_id, amount, converted)

        elif choice == "4":
            print_conversion_report()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


# ---------------- MAIN ----------------

if __name__ == "__main__":
    create_database()
    create_table()
    menu()