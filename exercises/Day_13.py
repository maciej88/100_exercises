#Q47:

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14*self.r**2

if __name__ == "__main__":
    a = Circle(2)
    print(a.area())