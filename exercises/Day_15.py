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

calculus()