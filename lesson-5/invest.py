def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount += amount * (rate / 100)
        print(f"year {year}: ${amount:.2f}")

try:  
    amount = float(input("Amount: "))
    rate = float(input("Rate: "))
    years = int(input("Years: "))

    invest(amount, rate, years)
    
except ValueError as c:
    print(c)