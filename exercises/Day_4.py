#ex 10:
words = input("Podaj wyrażenie: ").split()
for i in words:
    if words.count(i) > 1:
        words.remove(i)

words.sort()
print(' - '.join(words))