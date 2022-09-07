#Q85:
li = [12,24,35,70,88,120,155]
lst = [li[i] for i in range(len(li)) if i not in (0, 4, 5)]
print(lst)
new = [x for (i, x) in enumerate(li) if i not in (0, 4, 5)]
print(new)

#Q86:
li = [12,24,35,24,88,120,155]
li = [i for i in li if i != 24]
print(li)

#Q87:
l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]
s1, s2 = set(l1), set(l2)
s1 &= s2
print(s1)

#88:
lst = [12,24,35,24,88,120,155,88,120,155]
s1 = set(lst)
print(sorted(s1))

#Q89:
class Person(object):
    def __init__(self):
        self.gender = "none"

    def get_gender(self):
        print(self.gender)

class Male(Person):
    def __init__(self):
        self.gender = 'Male'

class Female(Person):
    def __init__(self):
        self.gender = 'Female'

one = Person()
one.get_gender()
two = Female()
two.get_gender()