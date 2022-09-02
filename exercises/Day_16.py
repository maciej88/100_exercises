#Q60:
def f(n):
    if n == 0:
        return 0
    return f(n-1) + 100

n = int(input("number: "))
print(f(n))

#Q61:
def f(n):
    if n < 2:
        return n
    return f(n-1) + f(n-2)

n = int(input("fib: "))
print(f(n))