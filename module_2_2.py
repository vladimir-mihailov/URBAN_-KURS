first = int(input("Число: "))
second = int(input("Число: "))
third = int(input("Число: "))
print(f'first: {first}, second: {second}, third: {third}')

if first==second==third:
    print(3)
elif not first != second == third or first == second != third or first!=third==second:
    print(2)
elif not first==second==third:
    print(0)

