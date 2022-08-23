#Q20:
class DiviseGen():
    def by_seven(self, n):
        for i in range(0, int(n/7) + 1):
            print(f'i:{i}')
            yield i * 7

for i in DiviseGen().by_seven(int(input('Give number to divine: '))):
    print(i)

#Q21:
from math import sqrt
lst = []
position = [0,0]
while True:
    a = input()
    if not a:
        break
    lst.append(a)
for i in lst:
    if 'UP' in i:
        position[0] -= int(i.strip('UP '))
    if 'DOWN' in i:
        position[0] += int(i.strip('DOWN '))
    if 'LEFT' in i:
        position[1] -= int(i.strip('LEFT '))
    if 'RIGHT' in i:
        position[1] += int(i.strip('RIGHT '))
print(round(sqrt(position[1] ** 2 + position[0] ** 2)))