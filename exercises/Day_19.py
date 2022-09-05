import random
import zlib
import datetime
import itertools

#Q75:
print(random.randrange(7, 16))

#Q76:
s = 'hello world!hello world!hello world!hello world!'
# In Python 3 zlib.compress() accepts only DataType <bytes>
y = bytes(s, 'utf-8')
x = zlib.compress(y)
print(x)
print(zlib.decompress(x))

#Q77:
start_time = datetime.datetime.now()
for i in range(100):
    x = 1 + 1
end_time = datetime.datetime.now()
result = end_time - start_time
print(result)

#Q78:
li = [3,6,7,8]
random.shuffle(li)
print(li)

#79:
who = ["I", "You"]
what = ["Play", "Love"]
sport = ["Hockey","Football"]
combination_list = [who, what, sport]
finish = list(itertools.product(*combination_list))
print(finish)