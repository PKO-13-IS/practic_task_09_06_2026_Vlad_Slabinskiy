m1 = float(input())
m2 = float(input())
m3 = float(input())

massive = max(m1, m2, m3)
lightest = min(m1, m2, m3)
total_mass = m1 + m2 + m3

print(f"Самое тяжёлое: {massive} кг")
print(f"Самое лёгкое: {lightest} кг")
print(f"Общая масса: {total_mass} кг")