#Q20:
class DiviseGen():
    def by_seven(self, n):
        for i in range(0, int(n/7) + 1):
            print(f'i:{i}')
            yield i * 7

for i in DiviseGen().by_seven(int(input('Give number to divine: '))):
    print(i)