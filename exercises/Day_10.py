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