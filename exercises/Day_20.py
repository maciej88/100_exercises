#Q80:
li = [5,6,77,45,22,12,24]
def is_even(n):
    return n%2 == 0

print(list(filter(is_even, li)))

#Q81:
lst = [12,24,35,70,88,120,155]
lst = [i for i in lst if i%5!=0 and i%7!=0]
print(lst)

#Q82:
li = [12,24,35,70,88,120,155]
li = [li[i] for i in range(len(li)) if i%2 != 0 and i <= 6]
print(li)
