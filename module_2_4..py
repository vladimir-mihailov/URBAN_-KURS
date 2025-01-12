numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []
is_prime = 0  #  Переменная (Выдает ошибку по строке 16 без нее ???)

for num in numbers:
    if num > 1:  # Исключаем 1, так как оно не является ни простым, ни составным
        is_prime = True  # Переменная-флаг для проверки на простоту (по заданию)

        for d in range(2, num):  # Проверяем делители от 2 до num-1
            if num % d == 0:  # Если есть делитель
                is_prime = False  # Устанавливаем флаг на False (по заданию)
                break  # Выход из цикла, так как уже определен делитель

        if is_prime:
            primes.append(num)  # Добавление в список простых чисел
        else:
            not_primes.append(num)  # Добавление в список не простых чисел
else:
    not_primes.append(num) # Добавление в список не простых чисел (по остатку)


# Вывод результата кода:
print("Primes:", primes)
print("Not_Primes:", not_primes)




