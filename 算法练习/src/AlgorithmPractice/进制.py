a, b = map(int, input().split(",", 1))
sum = 0
time = 0
while a != 0:
    c = a % 10
    sum += (b ** time) * c
    time += 1
    a = a // 10
print(sum)
