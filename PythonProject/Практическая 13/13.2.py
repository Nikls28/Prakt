#Москаленко Н.В.
# №6 - Дан файл Assort, содержащий сведения об игрушках: назва­ние игрушки, ее стоимость в рублях и возрастные границы 
# (на­пример, игрушка может предназначаться для детей от двух до пяти лет). Определить:
import csv

filename = "Assort.csv"

def load_data(filename):
    toys = []
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name, price, min_age, max_age = row
            toys.append({
                "name": name,
                "price": float(price),
                "min_age": int(min_age),
                "max_age": int(max_age)
            })
    return toys

toys = load_data(filename)

# (а)названия игрушек, цена которых не превышает 14 тыс. р. и которые подходят детям пяти лет;
toys_for_five = [t["name"] for t in toys if t["price"] <= 14000 and t["min_age"] <= 5 <= t["max_age"]]

# (б)стоимость самого дорогого конструктора;
constructors = [t["price"] for t in toys if "конструктор" in t["name"].lower()]
max_constructor_price = max(constructors) if constructors else None

# (в)названия наиболее дорогих игрушек (цена которых отлича­ется от цены самой дорогой игрушки не более чем на 5 тыс. р.);
max_price = max(t["price"] for t in toys)
expensive_toys = [t["name"] for t in toys if max_price - t["price"] <= 5000]

# (г)названия игрушек, которые подходят детям и четырех, и де­сяти лет;
toys_for_4_and_10 = [t["name"] for t in toys if t["min_age"] <= 4 <= t["max_age"] and t["min_age"] <= 10 <= t["max_age"]]

# (д)можно ли подобрать игрушку (любую, кроме мяча), подходя­щую ребенку трех лет;
suitable_for_three = any(t for t in toys if t["min_age"] <= 3 <= t["max_age"] and "мяч" not in t["name"].lower())

# (е)название самой дешевой игрушки;
cheapest_toy = min(toys, key=lambda t: t["price"])["name"]

# (ж)название самой дорогой игрушки для детей до четырех лет;
expensive_under_4 = max((t for t in toys if t["max_age"] <= 4), key=lambda t: t["price"], default=None)
expensive_under_4_name = expensive_under_4["name"] if expensive_under_4 else None

# (з)названия игрушек для детей от четырех до пяти лет;
toys_for_4_5 = [t["name"] for t in toys if t["min_age"] <= 4 and t["max_age"] >= 5]

# (и)название самой дорогой игрушки, подходящей детям от двух до трех лет;
expensive_2_3 = max((t for t in toys if 2 <= t["min_age"] and t["max_age"] <= 3), key=lambda t: t["price"], default=None)
expensive_2_3_name = expensive_2_3["name"] if expensive_2_3 else None

# (л)стоимость самой дорогой куклы;
doll_prices = [t["price"] for t in toys if "кукла" in t["name"].lower()]
most_expensive_doll = max(doll_prices) if doll_prices else None

# (м)стоимость кукол для детей шести лет;
dolls_for_six = [t["price"] for t in toys if "кукла" in t["name"].lower() and t["min_age"] <= 6 <= t["max_age"]]

# (н)для детей какого возраста предназначается конструктор;
constructor_ages = {t["min_age"]: t["max_age"] for t in toys if "конструктор" in t["name"].lower()}

# (о)для детей какого возраста предназначены кубики и указать их среднюю стоимость.
cubes = [t for t in toys if "кубики" in t["name"].lower()]
cube_ages = {(c["min_age"], c["max_age"]) for c in cubes}
average_cube_price = sum(c["price"] for c in cubes) / len(cubes) if cubes else None

# Вывод результатов
print(f"(а) Игрушки до 14 тыс. р. для 5 лет: {toys_for_five}")
print(f"(б) Самый дорогой конструктор: {max_constructor_price} руб.")
print(f"(в) Дорогие игрушки: {expensive_toys}")
print(f"(г) Игрушки для 4 и 10 лет: {toys_for_4_and_10}")
print(f"(д) Можно ли найти игрушку для 3 лет (не мяч): {suitable_for_three}")
print(f"(е) Самая дешевая игрушка: {cheapest_toy}")
print(f"(ж) Самая дорогая игрушка до 4 лет: {expensive_under_4_name}")
print(f"(з) Игрушки для 4-5 лет: {toys_for_4_5}")
print(f"(и) Самая дорогая игрушка для 2-3 лет: {expensive_2_3_name}")
print(f"(л) Самая дорогая кукла: {most_expensive_doll} руб.")
print(f"(м) Стоимость кукол для 6 лет: {dolls_for_six}")
print(f"(н) Возраст конструктора: {constructor_ages}")
print(f"(о) Возраст кубиков: {cube_ages}, Средняя цена: {average_cube_price} руб.")