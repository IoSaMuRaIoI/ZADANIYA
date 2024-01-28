deposit = float(input("Введите сумму вклада: "))

if deposit < 100:
    interest_rate = 0.05
elif deposit <= 200:
    interest_rate = 0.07
else:
    interest_rate = 0.1

total_amount = deposit + deposit * interest_rate

print("Сумма вклада с начисленными процентами: ", total_amount)
