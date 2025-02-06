print("Таблица сложения:") 
print("+ | ", end='') 
for i in range(1, 16): 
    print(f"{hex(i)[2:].upper():>3}", end=' ') 
print() 

print("-" * 63) 

for i in range(1, 16): 
    print(f"{hex(i)[2:].upper():>2}| ", end='') 
    for j in range(1, 16): 
        result = i + j 
        print(f"{hex(result)[2:].upper():>3}", end=' ') 
    print()

print("Таблица умножения:") 
print("+ | ", end='') 
for i in range(1, 16): 
    print(f"{hex(i)[2:].upper():>3}", end=' ') 
print() 

print("-" * 63) 

for i in range(1, 16): 
    print(f"{hex(i)[2:].upper():>2}| ", end='')
    for j in range(1, 16): 
        result = i * j 
        print(f"{hex(result)[2:].upper():>3}", end=' ') 
    print()