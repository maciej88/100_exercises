#Q51:
def compute():
    return 5/0

try:
    compute()
except ZeroDivisionError:
    print("0? are You serius?")