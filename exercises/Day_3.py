#Q10
x = input("words to sort: ")
words = [word for word in x.split(' ')]
words = sorted(words)
words = list(dict.fromkeys(words))
print(' '.join(words))