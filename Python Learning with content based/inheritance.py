#Parent Class #Super Class #Base Class
#Child Class #Sub Class #Derived Class
class Phone:
    def call(self):
        print("You Can Call !")
    def message(self):
        print("You Can Message !")

class Iphone(Phone):
    def photo(self):
        print("You Can Take Picture !")
    def music(self):
        print("You can Play Music !")

i = Iphone()
i.call()
i.message()

print(issubclass(Iphone,Phone))