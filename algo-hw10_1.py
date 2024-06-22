import pulp

# Створюємо проблему лінійного програмування
model = pulp.LpProblem("Maximize Drinks Production", pulp.LpMaximize)

# Змінні для кількості вироблених напоїв
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable("FruitJuice", lowBound=0, cat="Integer")

# Цільова функція - максимізація загальної кількості вироблених напоїв
model += lemonade + fruit_juice, "Total Drinks Produced"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint"
model += 1 * lemonade <= 50, "Sugar Constraint"
model += 1 * lemonade <= 30, "Lemon Juice Constraint"
model += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Розв'язуємо проблему
model.solve()

# Виводимо результати
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade: {pulp.value(lemonade)}")
print(f"Fruit Juice: {pulp.value(fruit_juice)}")
print(f"Total Drinks Produced: {pulp.value(model.objective)}")
