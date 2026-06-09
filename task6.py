a = float(input())
b = float(input())
c = float(input())

# Находим самую длинную сторону (гипотенузу)
sides = sorted([a, b, c])
if sides[2]**2 == sides[0]**2 + sides[1]**2:
    print("Да")
else:
    print("Нет")