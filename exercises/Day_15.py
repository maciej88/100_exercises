#Q54:
def posted():
    email = input("enter email: ")
    end =email.split("@")[1]
    print(end.split(".")[0])

posted()