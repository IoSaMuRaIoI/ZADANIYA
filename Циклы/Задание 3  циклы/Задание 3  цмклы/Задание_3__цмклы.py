def main():
    while True:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))

        if 0 <= num1 <= 10 and 0 <= num2 <= 10:
            result = num1 * num2
            print(f"Результат умножения: {result}")
            break  
        else:
            print("Введенные числа недопустимы. Пожалуйста, введите числа от 0 до 10.")

if __name__ == "__main__":
    main()
