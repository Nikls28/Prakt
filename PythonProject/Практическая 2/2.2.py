#Москаленко Н.В.
# №16 - Дана длина ребра куба. Найти площади грани, полной поверхности и объем этого куба.
a = int(input("Введите длину ребра куба: "))

b = a**2
print("Площадь грани: ", b)

c = 6 * b
print("Площадь полной поверхности: ", c)

d = a**3
print("Объем куба: ", d)