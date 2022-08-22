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