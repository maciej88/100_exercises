#Q44:
def sqr_nums(items):
    return items ** 2

print(list(map(sqr_nums, range(1, 21))))

#Q45 & Q46:
class American():
    @staticmethod
    def printNationality():
        print('America')

class NewYorker(American):
    @staticmethod
    def printCity():
        print('New-York')

if __name__ == "__main__":
    x = American()
    x.printNationality()
    American.printNationality()

    y = NewYorker()
    y.printNationality()
    y.printCity()