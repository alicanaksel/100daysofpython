def add(*args):
    sum=0
    for n in args:
        sum +=n
    
    return sum

# print(add(3,5,6,2,1,6,4,5))

def calculate(n, **kwargs):
    print(kwargs)
    #code firstly n+ adds and then multiply with "multiply"
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
calculate(2,add=3, multiply=5)

class Car:
    def __init__(self,**kw):
        #this first two lines is a bit primitive cuz if i dont type make it might returns error
        # self.make= kw["make"]
        # self.model= kw["model"]
        self.made= kw.get("make")
        self.model= kw.get("model")
        self.colour= kw.get("colour")
        self.seats= kw.get("seats")

my_car=Car(make="Nissan",model="Skyline") 
print(my_car.model) #if i were to ask seats it would return None but in primitive error