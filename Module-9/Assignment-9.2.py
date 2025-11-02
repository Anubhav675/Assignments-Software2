class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed):
        updated_speed = self.current_speed + speed
        if updated_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
            #print("You cannot exceed the maximum speed!!")
        elif updated_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = updated_speed


car = Car("ABC-123", 142)
# print(f'License plate: {car.license_plate}\nMaximum speed: {car.maximum_speed}\nCurrent speed: {car.current_speed} km/h\nTravelled distance: {car.travelled_distance} km')
car.accelerate(30)
car.accelerate(70)
car.accelerate(50)
#print(f"Current speed: {car.current_speed} km/h")
car.accelerate(-200)
#print(f"Current speed: {car.current_speed} km/h")
