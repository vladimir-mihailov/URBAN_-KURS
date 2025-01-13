def generat_password(first_insert):
    password = ""
    # Генерация уникальных пар
    pairs = []
    for i in range(1, first_insert):
        for a in range(i + 1, first_insert + 1):
            pairs.append((i, a))
        # Проверка кратности и формирование пароля
        for pair in pairs:
            sum_pair = sum(pair)
            if first_insert % sum_pair == 0:
                password += f"{pair[0]}{pair[1]}"

        return password # Вырезаем до 42 символов, если нужно

#  вызов функции:
first_insert = int(input("Введите число от 3 до 20: "))
if 3 <= first_insert <= 20:
    reult = generat_password(first_insert)
    print(f"Паролем числа {first_insert} является {reult}")
else:
    print(f"Ошибка: повторите ввод (от 3 до 20) ")


