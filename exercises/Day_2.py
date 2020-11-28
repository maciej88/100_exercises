# #ex1:
# lis = input('Podaj iczby: ').split(',')
# print(lis)
# print(tuple(lis))

#ex1:
class InOutString:
    def get_string(self):
        self.stri = input("podaj wyraz: ")

    def post_string(self):
        print(self.stri.upper())

    def lower_string(self):
        print(self.stri.lower())

xx = InOutString()
xx.get_string()
xx.post_string()
xx.lower_string()