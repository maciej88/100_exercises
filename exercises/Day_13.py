#Q47:

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14*self.r**2

#Q48:
class Ractangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

class Shape():
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l=0):
        Shape.__init__(self)
        self.l = l

    def area(self):
        return self.l * self.l

if __name__ == "__main__":
    a = Circle(2)
    print(a.area())

    b = Ractangle(2, 3)
    print(b.area())

    c = Square(5)
    print(c.area())