#Q26:
def sum_func(num1, num2):
    return print(num1 + num2)

sum_func(5, 3)

#Q27:
def int_to_str(n):
    return print(str(n))

int_to_str(33)

#Q28:
def sum_str(x, y):
    return print(int(x) + int(y))

sum_str("5", "3")

#Q29:
def concentrate(x, y):
    return print(x + y)

concentrate("8", "2")

#Q30:
def get_lenght(x, y):
    y1 = len(y)
    x1 = len(x)
    if x1 > y1:
        return print(f"{x} - longer: {x1}")
    elif y1 > x1:
        return print(f"{y} - longer: {y1}")
    else:
        return print("booth the same")

get_lenght("ala ma", "kocuraaaa")