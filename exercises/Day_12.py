#Q44:
def sqr_nums(items):
    return items ** 2

print(list(map(sqr_nums, range(1, 21))))

#Q45:
class American(object):
    @staticmethod
    def printNationality():
        print('America')


if __name__ == "__main__":
    x = American()
    x.printNationality()
    American.printNationality()