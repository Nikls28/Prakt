#Москаленко Н.В.
# №16 - Составить программу, печатающую значение True, если следующие указанные высказывания являются истинными, и значение false — в противном случае. Два
# введенных символа не являются последовательно расположенными в кодовой таблице.
a = input()
b = input()

c1 = ord(a)
c2 = ord(b)

if abs(c1 - c2) == 1:
    print(False)
else:
    print(True)