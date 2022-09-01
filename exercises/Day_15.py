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
# s = input("any string: ")
# u = s.encode('utf-8')
# print(u)

#Q58:
# -*- coding: utf-8 -*-
#it should be on top of file.

#Q59:
def wierd():
    n = int(input("number: "))
    result = 0
    for i in range(1, n+1):
        result += float(i /float(i+1))
        print(round(result, 2))

wierd()