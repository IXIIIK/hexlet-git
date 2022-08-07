def fib(n):
    f1 = 0
    f2 = 1

    for f in range(0, n):
        f = f1 + f2
        f2 += f1
        print(f, f2)
    return f2

print(fib(10))
