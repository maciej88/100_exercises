# #ex 10:
# words = input("Podaj wyrażenie: ").split()
# for i in words:
#     if words.count(i) > 1:
#         words.remove(i)
#
# words.sort()
# print(' - '.join(words))

#ex 11:
def test(n):
    return int(n,2)%5 == 0

data = input("enter number sequence: ").split(',')

data = list(filter(test,data))
print(",".join(data))