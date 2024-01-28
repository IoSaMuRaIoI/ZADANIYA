def main():
    print("Введите номер операции: 1. Сложение 2. Вычитание 3. Умножение")
    operation = int(input("Номер операции: "))
    
    result = ""
    if operation == 1:
        result = "Сложение"
    elif operation == 2:
        result = "Вычитание"
    elif operation == 3:
        result = "Умножение"
    else:
        result = "Операция неопределена"
    
    print("Выбранная операция:", result)

if __name__ == "__main__":
    main()
