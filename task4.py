num = int(input())

a = num // 100
b = (num // 10) % 10
c = num % 10

total = a + b + c

print(f"Сумма цифр = {total}")