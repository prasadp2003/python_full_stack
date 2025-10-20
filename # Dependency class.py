# Dependency class
class Engine:
    def start(self):
        print("Engine started")

# Dependent class
class Car:
    def __init__(self, engine):
        self.engine = engine  # Dependency injected via constructor

    def drive(self):
        self.engine.start()
        print("Car is driving")

# Injecting the dependency
engine = Engine()
my_car = Car(engine)
my_car.drive()