a = int(input("введите точку a: "))
b = int(input("введите точку b: "))
c = int(input("введите точку c: "))

ab = abs(a - b)
ac = abs(a - c)

if ab < ac:
    print("точка b ближе")
elif ac < ab:
    print("точка c ближе")
else:
    print("одинаково")