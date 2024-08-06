"""Create a base class Vehicle with attributes like make and model. Define methods like accelerate (prints a generic message) and brake (prints another generic message). Create subclasses Car and Motorcycle inheriting from Vehicle. Override the accelerate and brake methods in the subclasses to provide more specific behavior (e.g., "Car accelerating" for Car.accelerate)."""
# Base class Vehicle
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def accelerate(self):
        print("Vehicle accelerating...")
    def brake(self):
        print("Vehicle braking...")


# Subclass Car inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors
    def accelerate(self):
        print("Car accelerating... Vroom!")
    def brake(self):
        print("Car braking... Screech!")


# Subclass Motorcycle inheriting from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, make, model, engine_size):
        super().__init__(make, model)
        self.engine_size = engine_size
    def accelerate(self):
        print("Motorcycle accelerating... Zoom!")
    def brake(self):
        print("Motorcycle braking... Whoa!")


# Example usage
if __name__ == "__main__":
    car = Car("Toyota", "Corolla", 4)
    print(f"Make: {car.make}, Model: {car.model}, Doors: {car.num_doors}")
    car.accelerate()
    car.brake()
    motorcycle = Motorcycle("Honda", "CBR500R", 500)
    print(f"Make: {motorcycle.make}, Model: {motorcycle.model}, Engine Size: {motorcycle.engine_size}cc")
    motorcycle.accelerate()
    motorcycle.brake()
