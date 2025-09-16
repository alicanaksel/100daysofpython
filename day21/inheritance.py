class Animal:
    def __init__(self):
        self.num_eyes=2

    def breathe(self):
        print("Inhale, exhale.")


#inheritance part is here 
#class smth(another class)
class Fish(Animal):

    def __init__(self):
        super().__init__() #this the part 2 of inheritance

    def breathe(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water")


nemo= Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)