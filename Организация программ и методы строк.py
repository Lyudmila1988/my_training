def main():

    my_string = input("Введите произвольный текст: ")

    print(f"Количество символов в строке: {len(my_string)}")

    print(f"Строка в верхнем регистре: {my_string.upper()}")

    print(f"Строка в нижнем регистре: {my_string.lower()}")

    no_spaces = my_string.replace(" ", "")
    print(f"Строка без пробелов: {no_spaces}")

    if len(my_string) > 0:
        print(f"Первый символ строки: {my_string[0]}")
    else:
        print("Строка пуста, первого символа нет.")

    if len(my_string) > 0:
        print(f"Последний символ строки: {my_string[-1]}")
    else:
        print("Строка пуста, последнего символа нет.")

if __name__ == "__main__":
    main()
