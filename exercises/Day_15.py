import re

#Q54:
def posted():
    email = input("enter email: ")
    end =email.split("@")[1]
    print(end.split(".")[0])

#Q55:
def calculus():
    n = input("sentence: ")
    print(re.findall("\d+", n))

#Q56:
def unicode():
    sentence = u"Hello World"
    print(sentence)

#Q57:
s = input("any string: ")
u = s.encode('utf-8')
print(u)

#Q58:
# -*- coding: utf-8 -*-