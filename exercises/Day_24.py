#Q100:
n = int(input())

word_list = []
word_dict = {}

for i in range(n):
    word = input()
    if word not in word_dict:
        word_list.append(word)
    word_dict[word] = word_dict.get(word, 0) + 1

print(len(word_list))
for word in word_list:
    print(word_dict[word], end=' ')

#Q101:
letters = input()
d = {}
for i in letters:
    d[i] = d.get(i, 0) + 1

d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
for i in d:
    print(i[0], i[1])