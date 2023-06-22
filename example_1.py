import random

n = int(input("Введите число n: "))
m = int(input("Введите число m: "))
s1 = random.sample(range(1000),n)
s2 = random.sample(range(1000),m)
result = s1 + s2
result_set = set(result)
itog = list(result_set)
itog.sort()
print(itog)
