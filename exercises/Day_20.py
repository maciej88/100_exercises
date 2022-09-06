#Q80:
li = [5,6,77,45,22,12,24]
def is_even(n):
    return n%2 == 0

print(list(filter(is_even, li)))