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

#62:
def f(n):
    if n < 2:
        fibo[n] = n
        return fibo[n]
    fibo[n] = f(n-1) + f(n-2)
    return fibo[n]

n = int(input())
fibo = [0]*(n+1)  # initialize a list of size (n+1)
f(n)              # call once and it will set value to fibo[0-n]
fibo = [str(i) for i in fibo]   # converting integer data to string type
ans = ",".join(fibo)    # joining all string element of fibo with ',' character
print(ans)

#63:
n = int(input("Give number: "))

for i in range(0, n+1, 2):
    if i < n - 1:
        print(i, end=',')
    else:
        print(i)