import random

N = int(input("ведите размер массива: "))
nums = [random.randint(-100,100) for _ in range(N)]

pos = 0
neg = 0
zero = 0

for num in nums:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1

print("массив: ",nums)
print("Положительные: ",pos)
print("Отрицательные: ",neg)
print("Ноль: ", zero)