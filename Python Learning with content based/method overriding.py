class Phone:
    def __init__(self):
        print("I Am In Phone Class !")

class Iphone(Phone):
   # pass

    def __init__(self):
        super().__init__()
        print("I Am In Iphone Class !!!")


i = Iphone()
