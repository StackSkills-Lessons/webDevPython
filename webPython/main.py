
class Program():
    
    # Function called at the program launch
    def __init__(self, *args, **kwargs):
        self.language = input("What is your language?: ")
        self.age = float(input("What is your age?: "))

    def upgrade(self):
        new_Age = input("New Age?: ")
        print("The new age for you is :" + new_Age + " instead of " + str(self.age)) 
        self.age = float(new_Age)

p1 = Program()

