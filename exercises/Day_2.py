from math import sqrt
# Q4:
def get_sequence(n):
    raw = n.split(',')
    print(raw)
    print(tuple(raw))
print(get_sequence('34,67,55,33,12,98'))

# Q5:
class StringConvert:
    def get_string(self):
        self.n = input("Give string to upper: ")

    def print_string(self):
        print(self.n.upper())

x = StringConvert()
x.get_string()
x.print_string()

#Q6:
# Q = Sqr[(2*C*D)/H]
C, H = 50, 30
def calc(D):
    return sqrt((2*C*D)/H)

D = [int(i) for i in input("enter 3 numbers, egz: x,y,z: ").split(',')] # splits in comma position and set up in list
D = [int(i) for i in D]   # converts string to integer
D = [calc(i) for i in D]  # returns floating value by calc method for every item in D
D = [round(i) for i in D] # All the floating values are rounded
D = [str(i) for i in D]   # All the integers are converted to string to be able to apply join operation

print(",".join(D))

#Q7:
x,y = map(int,input("two numbers separated by \',\':").split(','))
print(f"Calcuating arrays for {x} and {y}")

li = []

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i*j)
    li.append(tmp)
print(li)

#Q8:
def sort():
    items = input("Words conected by \",\": ").split(',')
    items.sort()
    return print(','.join(items))

sort()