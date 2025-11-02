class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 2000

    def accelerate(self, speed):
        updated_speed = self.current_speed + speed
        if updated_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
            #print("You cannot exceed the maximum speed!!")
        elif updated_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = updated_speed
    def drive(self, hour):
        increased_distance= hour * self.current_speed
        #print(increased_distance)
        self.travelled_distance = increased_distance + self.travelled_distance



car = Car("ABC-123", 142)
#print(f"Initial distance: {car.travelled_distance} km")
car.current_speed = 60
car.drive(1.5)
#print(f"Distance after driving 1.5 hours at 60 km/h: {car.travelled_distance} km")