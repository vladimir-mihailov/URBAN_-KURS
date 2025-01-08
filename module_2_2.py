first = int(input("first: "))
second = int(input("second: "))
third = int(input("third: "))
print(f'first: {first}, second: {second}, third: {third}')

#if first == second != third or third == second != first or first!=third==second:
if(first==second and second!=third) or (second==first and first!=third) or (first==third and first!=second):
    print(2)
elif first==second==third:
    print(3)
#elif first!=third and first!=second and third!=second:
else:
    print(0)

