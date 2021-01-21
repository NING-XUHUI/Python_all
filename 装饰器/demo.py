from collections.abc import Iterable


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while True:
        if count > n:
            break
        yield a + b
        a, b = b, a + b
        count += 1


gen = fibonacci(100)

for i in gen:
    print(i)
