def main():
    initial_amount = float(input("Введите сумму вклада: "))
    months = int(input("Введите количество месяцев: "))

    for month in range(1, months + 1):
        initial_amount += initial_amount * 0.07  # начисление 7% от суммы вклада

    print(f"Конечная сумма вклада после {months} месяцев: {initial_amount:.2f}")


if __name__ == "__main__":
    main()
