#Москаленко Н.В. 2 вариант
#Практическая  №12 - Даны имена девочек. Определить, какие из этих имен встречаются во всех
#параллельных классах школы, какие есть только в некоторых классах и какие не
#встречаются ни в одном из классов.
school_classes = [
    ["Анна", "Мария", "Елена", "Дарья"],
    ["Мария", "София", "Анна", "Ольга"],
    ["Анна", "София", "Мария", "Дарья"]
]
givenames = ["Анна", "Мария", "Елена", "София", "Ольга", "Дарья"]

allclasses = [set(classnames) for classnames in school_classes]

common_names = set.intersection(*allclasses) if allclasses else set()
classes_names = set.union(*allclasses) if allclasses else set()

intwo_classes = set()
inone_class = set()

for name in classes_names:
    count = sum(1 for classnames in allclasses if name in classnames)
    if count == 2:
        intwo_classes.add(name)
    elif count == 1:
        inone_class.add(name)

print("Имена, встречающиеся во всех трех классах:", common_names)
print("Имена, встречающиеся в двух классах:", intwo_classes)
print("Имена, встречающиеся только в одном классе:", inone_class)
