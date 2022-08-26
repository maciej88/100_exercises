#Q31:
def get_dict():
    new_dict = {}
    for i in range (1, 21):
        new_dict[i] = i ** 2
    print(new_dict)

get_dict()

#Q32:
def get_new_dict():
    new_dict = {}
    for i in range(1, 21):
        new_dict[i] = i ** 2
    for k in new_dict.keys():
        print(k)

get_new_dict()

#Q33:
def get_sqr_list():
    lst = []
    for i in range(1, 21):
        lst.append(i**2)
    return print(lst)

get_sqr_list()

#Q34:
def get_sqr_list_part():
    lst = []
    for i in range(1, 21):
        lst.append(i**2)
    return print(lst[:5])

get_sqr_list_part()