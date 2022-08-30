#Q51:
def compute():
    return 5/0

try:
    compute()
except ZeroDivisionError:
    print("0? are You serius?")

#Q52:
class CustomError(Exception):
    """New Error
    Attributes:
    err - Yes, You messed it up!
    """
    def __init__(self, err):
        self.err = err

exemple = int(input())

try:
    if exemple < 5:
        raise CustomError('Ekhem')
    elif exemple > 5:
        raise CustomError("try 0")
except CustomError as ce:
    print("you made it " + ce.err)

#Q53:
email = input("enter email")
print(email.split("@")[0])