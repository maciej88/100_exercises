#Q22:
sentence = input('Sentence: ').split()
words = sorted(set(sentence))
for i in words:
    print(f"{i}: {sentence.count(i)}")

#Q23:
def calc():
    num = int(input())
    return print(num ** 2)

calc()

#Q24:
def help_me():
    print(help.__doc__)
    print(str.__doc__)
    print(sorted.__doc__)

help_me()

def pow(n,p):
    '''
    param n: This is any integer number
    param p: This is power over n
    return:  n to the power p = n^p
    '''

    return n**p

print(pow(3,4))
print(pow.__doc__)

#Q25:
class Robot:
    name = "Robot"
    def __init__(self, name):
        self.name = name

vector = Robot("Vector")
print(vector.name, Robot.name)