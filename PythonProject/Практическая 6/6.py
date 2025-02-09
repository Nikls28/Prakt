#Москаленко Н.В.
# №15 - Целое число можно представить, как сумму его частей, называемых разбиениями. Например, число 4 можно представить следующим образом: 4; 3 +
#1; 2 + 1 + 1; 2 + 2; 1 + 1 + 1 + 1 Тогда, обо значив через Р(n) количество разбиений числа n, можно записать Р(4) = 5 Для заданного числа n выполнить
#его разбиения и определить Р(n).
n = int(input("Введите число n: "))

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n + 1):
    for j in range(i, n + 1):
        dp[j] += dp[j - i]

print(f"Количество разбиений числа {n}: {dp[n]}")