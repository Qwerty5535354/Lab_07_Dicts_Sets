# Лабораторна робота №7, варіант 5
# Завдання 1 (словник): населення міст
# Завдання 2 (множини): міста, які відвідали двоє туристів

# ---------- Завдання 1 ----------
cities = {
    "Київ": 2950000,
    "Харків": 1420000,
    "Одеса": 1010000,
    "Дніпро": 980000,
    "Львів": 720000,
    "Запоріжжя": 710000,
}

print("Завдання 1")
biggest = max(cities, key=cities.get)   # місто з найбільшим населенням
print("Найбільше місто:", biggest, cities[biggest])

# додаємо нове місто
name = input("Назва нового міста: ").strip()
try:
    population = int(input("Населення: "))
    if name == "":
        print("Помилка: назва не може бути порожньою")
    elif population <= 0:
        print("Помилка: населення має бути додатним")
    elif name in cities:
        print("Помилка: таке місто вже є")
    else:
        cities[name] = population
        print("Місто додано")
except ValueError:
    print("Помилка: населення має бути цілим числом")

# міста з населенням більшим за задане
try:
    limit = int(input("Показати міста з населенням понад: "))
    found = False
    for city, people in cities.items():
        if people > limit:
            print(city, people)
            found = True
    if not found:
        print("Таких міст немає")
except ValueError:
    print("Помилка: потрібно ввести ціле число")

# ---------- Завдання 2 ----------
tourist1 = {"Київ", "Львів", "Одеса", "Харків", "Дніпро", "Чернівці"}
tourist2 = {"Львів", "Одеса", "Ужгород", "Вінниця", "Чернівці", "Полтава"}

print("\nЗавдання 2")
print("Спільні міста:", sorted(tourist1 & tourist2))
print("Лише перший турист:", sorted(tourist1 - tourist2))
print("Усі унікальні міста:", sorted(tourist1 | tourist2))
