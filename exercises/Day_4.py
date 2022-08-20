# #ex 10:
# words = input("Podaj wyrażenie: ").split()
# for i in words:
#     if words.count(i) > 1:
#         words.remove(i)
#
# words.sort()
# # print(' - '.join(words))
#
# #ex 11:
# def test(n):
#     return int(n,2)%5 == 0
#
# data = input("enter number sequence: ").split(',')
#
# data = list(filter(test,data))
# print(",".join(data))
#Q14:
sentence = input('Give the sentence in upper and lowercase: ')
upper = 0
lower = 0

for i in sentence:
    upper += i.isupper()
    lower += i.islower()

print(f"lower: {lower}, upper: {upper}")

#Q15:
a = input()
total,tmp = 0,str()        # initialing an integer and empty string

for i in range(4):
    tmp+=a               # concatenating 'a' to 'tmp'
    total+=int(tmp)      # converting string type to integer type

print(total)