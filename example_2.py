import random

n = int(input("Введите количество кустов: "))
s = random.sample(range(1000),n)
print(s)
max_total = 0
c = 0

for i in range(1,len(s)-1):
    if s[i+1] + s[i] + s[i-1] > max_total:
        max_total = s[i+1] + s[i] + s[i-1]
        c = i
print(f"Максимальное число ягод: {max_total}")
print(f"Номер куста: {c+1}")