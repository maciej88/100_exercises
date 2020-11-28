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
C,H = 50,30

def calc(D):
    D = int(D)
    return str(int(sqrt((2*C*D)/H)))

D = input().split(',')
D = list(map(calc,D))   # applying calc function on D and storing as a list
print(",".join(D))