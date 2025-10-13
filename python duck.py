class Duck:
    def quack(self):
        print("Quack! Quack!")
    
    def fly(self):
        print("Flap flap!")

class Airplane:
    def quack(self):
        print("Engines roar (pretend quack)!")
    
    def fly(self):
        print("Zoom zoom!")

def make_it_fly(thing):
    # We don’t care about type, only that it has .fly() and .quack()
    thing.quack()
    thing.fly()

# Works for both
duck = Duck()
plane = Airplane()

make_it_fly(duck)
make_it_fly(plane)
