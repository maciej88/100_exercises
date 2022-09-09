#Q95:
x = int(input("Score: "))
i = map(int, input("scores: ").split())
i = list(set(i))
i.sort()
print(i[-2])