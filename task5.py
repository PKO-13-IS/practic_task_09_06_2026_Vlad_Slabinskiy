age = int(input())
if age < 8:
    price = 0
elif age <= 16:
    price = 150
elif age <= 60:
    price = 600
else:
    price = 420
print(price)