#Q22:
sentence = input('Sentence: ').split()
words = sorted(set(sentence))
for i in words:
    print(f"{i}: {sentence.count(i)}")

#Q23:
def calc():
    num = int(input())
    return print(num ** 2)

calc()