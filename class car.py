class Car:
    # Class variable to track number of cars
    car_count = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.car_count += 1  # Increment count whenever a new car is created

    def display_info(self):
        return f"{self.make} {self.model}"

    @classmethod
    def total_cars(cls):
        return cls.car_count

# Example usage
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Civic")
car3 = Car("Tesla", "Model 3")

print(car1.display_info())  # Toyota Camry
print(f"Total cars created: {Car.total_cars()}")  # 3