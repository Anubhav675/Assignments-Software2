class Elevator:
    def __init__(self, top_floor, bottom_floor):
        self.top_floor = top_floor
        self.bottom_floor = bottom_floor
        self.current_floor = bottom_floor

    def floor_up(self):

        self.current_floor += 1
        print(f'You are at {self.current_floor}')

    def floor_down(self):
        self.current_floor -= 1
        print(f"You are at {self.current_floor}")

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            while self.current_floor != floor:
                self.floor_up()
        elif floor < self.current_floor:
            while self.current_floor != floor:
                self.floor_down()

# elevator1 = Elevator(10,1)
# elevator1.floor_up()
# elevator1.floor_up()
# print(f"You are currently at {elevator1.current_floor}")
# elevator1.go_to_floor(5)



