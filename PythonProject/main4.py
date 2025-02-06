a = input()
b = input()

c1 = ord(a)
c2 = ord(b)

if abs(c1 - c2) == 1:
    print(False)
else:
    print(True)