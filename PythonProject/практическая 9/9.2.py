#Москаленко Н.В.
# №2 - В массивах А[К] и B[L] хранятся коэффициенты двух многочленов степеней К и
#L. Поместить в массив С[М] коэффициенты произведения этих многочленов.
#(Числа К, L, М — натуральные; М = К +L; элемент массива с индексом i
#содержит коэффициент при x в степени i.)
A = [1, 2] 
B = [3, 4] 

K = len(A) - 1 
L = len(B) - 1 

M = K + L + 1
C = [0] * M

for i in range(K + 1):
    for j in range(L + 1):
        C[i + j] += A[i] * B[j]

print(C)