import textwrap
import string
import calendar

#Q95:
x = int(input("Score: "))
i = map(int, input("scores: ").split())
i = list(set(i))
i.sort()
print(i[-2])

#Q96:
s = input("String to wrap: ")
w = int(input("number of letters in wrap: "))
dspl = textwrap.wrap(s, w)
for i in dspl:
    print(i)

#Q97:
def rangoli():
    n = int(input("Size: "))
    alpha = string.ascii_lowercase
    w = 4*n - 3
    r = []
    for i in range(n):
       part = '-'.join(alpha[n-i - 1:n])
       mid = part[-1:0:-1] + part
       result = mid.center(w, '-')
       r.append(result)
    if len(r) > 1:
        for i in r[n - 2::-1]:
            r.append(i)
    r = '\n'.join(r)
    print(r)

rangoli()

#Q98:
month, day, year = map(int, input().split())

dayId = calendar.weekday(year, month, day)
print(calendar.day_name[dayId].upper())

#Q99:
n = int(input())
set1 = set(map(int, input().split()))

m = int(input())
set2 = set(map(int, input().split()))

result = list(set1 ^ set2)
result.sort()
for i in result:
    print(i)