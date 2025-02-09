#Москаленко Н.В.
# №16 - Дано действительное число x. Вычислить выражение
x = 5

chisl = 1
znam = 1
for i in range(0,7):
    term = x - (2**i - 1)
    chisl *= term

for i in range(1,7):
    term = x - (2**i)
    znam *= term

result = chisl / znam

print("x = ", x ,"результат: ", result)