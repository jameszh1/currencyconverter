import requests

req = requests.get("https://api.frankfurter.app/latest")
rates = req.json()['rates']
currency_count = 0
print("Welcome to Currency Converter Made Easy")
print("Here are the 30 currencies that we support: ")
for idx, currency in enumerate(rates, start=1):
    print(f"{idx}. {currency}")
    currency_count += 1

from_currency = input("What currency do you want convert from: ").upper()
to_currency = input("What currency do you want convert to: ").upper()
amount = float(input("What is the amount: "))
req2 = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(f"The conversion from {amount} {from_currency} to {to_currency} is", end=' ')
print(f"{req2.json()['rates'][to_currency]}")



