#Q85:
li = [12,24,35,70,88,120,155]
lst = [li[i] for i in range(len(li)) if i not in (0, 4, 5)]
print(lst)
new = [x for (i, x) in enumerate(li) if i not in (0, 4, 5)]
print(new)

#Q86:
li = [12,24,35,24,88,120,155]
li = [i for i in li if i != 24]
print(li)