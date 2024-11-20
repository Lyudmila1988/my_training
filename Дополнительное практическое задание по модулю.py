def generate_password(n):

    result = ""

    for i in range(1, 20):

        for j in range(i + 1, 21):

            if n % (i + j) == 0:

                result += str(i) + str(j)

    return result

number = int(input("Введите число от 3 до 20: "))
if 3 <= number <= 20:
    password = generate_password(number)
    print(f"Пароль для числа {number}: {password}")
else:
    print("Число должно быть от 3 до 20.")
