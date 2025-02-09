#Москаленко Н.В.
# №2 - Одномерный массив с четным количеством элементов (2N) содержит координаты N точек плоскости, которые располагаются в следующем порядке:
#х1, y1, х2, у2, х3, у3 и т.д. Определить:
#а) минимальный радиус окружности с центром в начале координат, которая содержит все точки;
#б) кольцо с центром в начале координат, которое содержит все точки;
#в) номера точек, которые могут являться вершинами квадрата;
#г) номера точек, которые могут являться вершинами равнобедренного треугольника;
#д) номера наиболее удаленных и наименее удаленных друг от друга точек;
#е) три точки, являющиеся вершинами треугольника, для которого разность точек вне его и внутри является минимальной.
import numpy as np
from itertools import combinations

# Пример массива координат
points = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# a)
x = points[::2]
y = points[1::2]
distances = np.sqrt(x**2 + y**2)
min_radius = np.max(distances)
print("Минимальный радиус:", min_radius)

# б) 
ring_min = np.min(distances)
ring_max = np.max(distances)
print("Кольцо (минимальный и максимальный радиус):", (ring_min, ring_max))

# в)
coords = list(zip(points[::2], points[1::2]))
square_points = None

for comb in combinations(range(len(coords)), 4):
    p = [coords[i] for i in comb]
    sides = [np.sqrt((p[i][0] - p[j][0])**2 + (p[i][1] - p[j][1])**2) for i, j in combinations(range(4), 2)]
    sides.sort()
    if np.isclose(sides[0], sides[1]) and np.isclose(sides[0], sides[2]) and np.isclose(sides[0], sides[3]) and np.isclose(sides[4], sides[5]):
        square_points = comb
        break

print("Номера точек, образующих квадрат:", square_points)

# г)
isosceles_points = None

for comb in combinations(range(len(coords)), 3):
    p = [coords[i] for i in comb]
    sides = [np.sqrt((p[i][0] - p[j][0])**2 + (p[i][1] - p[j][1])**2) for i, j in combinations(range(3), 2)]
    if len(set(np.round(sides, 5))) == 2:
        isosceles_points = comb
        break

print("Номера точек, образующих равнобедренный треугольник:", isosceles_points)

# д) 
max_dist = 0
min_dist = float('inf')
max_pair = None
min_pair = None

for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        dist = np.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)
        if dist > max_dist:
            max_dist = dist
            max_pair = (i, j)
        if dist < min_dist:
            min_dist = dist
            min_pair = (i, j)

print("Наиболее удаленные и наименее удаленные пары точек:", (max_pair, min_pair))

# е) 
min_diff = float('inf')
best_triangle = None

for comb in combinations(range(len(coords)), 3):
    a, b, c = [coords[i] for i in comb]
    inside = 0
    outside = 0
    
    for i in range(len(coords)):
        if i not in comb:
            d1 = (a[0] - coords[i][0]) * (b[1] - coords[i][1]) - (b[0] - coords[i][0]) * (a[1] - coords[i][1])
            d2 = (b[0] - coords[i][0]) * (c[1] - coords[i][1]) - (c[0] - coords[i][0]) * (b[1] - coords[i][1])
            d3 = (c[0] - coords[i][0]) * (a[1] - coords[i][1]) - (a[0] - coords[i][0]) * (c[1] - coords[i][1])
            
            if (d1 < 0 and d2 < 0 and d3 < 0) or (d1 > 0 and d2 > 0 and d3 > 0):
                inside += 1
            else:
                outside += 1
    
    diff = abs(inside - outside)
    if diff < min_diff:
        min_diff = diff
        best_triangle = comb

print("Треугольник с минимальной разностью точек внутри и снаружи:", best_triangle)