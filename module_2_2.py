first = int(input("first: "))
second = int(input("second: "))
third = int(input("third: "))
print(f'first: {first}, second: {second}, third: {third}')

if(first==second and second!=third) or (second==third and third!=first) or (third==first and first!=second):
    print(2)
elif not first!=second!=third:
    print(3)
else:
    print(0)

