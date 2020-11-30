from math import *

# #ex1:
# lis = input('Podaj iczby: ').split(',')
# print(lis)
# print(tuple(lis))

#ex1:
# class InOutString:
#     def get_string(self):
#         self.stri = input("podaj wyraz: ")
#
#     def post_string(self):
#         print(self.stri.upper())
#
#     def lower_string(self):
#         print(self.stri.lower())
#
# xx = InOutString()
# xx.get_string()
# xx.post_string()
# xx.lower_string()
#ex3
#in this exercise I was empty of ideas.... but:
# c,h = 50,30
#
# def calc(d):
#     d = int(d)
#     return str(int(sqrt((2*c*d)/h)))
#
# d = input().split(',')
# d = list(map(calc,d))   # applying calc function on D and storing as a list
# print(",".join(d))

#ex4 (7);
# x,y = map(int,input().split(','))
# ls = []
#
# for i in range(x):
#     tmp = []
#     for j in range(y):
#         tmp.append(i*j)
#     ls.append(tmp)
#
# print(ls)

#ex 5(8):
lst = input().split(',')
lst.sort()
print(",".join(lst))