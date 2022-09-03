#Q65
li = [2,4,6,8]
for i in li:
    assert i%2 == 0

#Q66:
val = input("Give to calculate: ")
print(eval(val))

#67:
def binary_search(lst, item):
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = round((low + high) / 2)

        if lst[mid] == item:
            return mid
        elif lst[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


lst = [1, 3, 5, 7, ]
print(binary_search(lst, 9))

#Q68:
import random
rand_num = random.uniform(10,100)
print(rand_num)

#Q69:
rand_num = random.uniform(5,95)
print(rand_num)