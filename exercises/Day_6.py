import re
#Q18:
def get_validation():
    passwords = input().split(',')
    approved = []
    pattern = re.compile(r"(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")
    for i in passwords:
        if pattern.findall(i):
            approved.append(i)
            print(approved)

get_validation()

#Q19:
from operator import itemgetter, attrgetter

l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split("," and '\n')))

print(sorted(l, key=itemgetter(0,1,2)))