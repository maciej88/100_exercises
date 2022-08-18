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