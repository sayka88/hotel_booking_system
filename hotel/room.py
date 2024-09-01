class Room:
    def __init__(self, number, room_type, rate):
        self.number = number
        self.room_type = room_type
        self.rate = rate
        self.availability = {}

    def is_available(self, check_in, check_out):
        for date in range(check_in, check_out):
            if self.availability.get(date, True) is False:
                return False
        return True

    def update_availability(self, check_in, check_out, status):
        for date in range(check_in, check_out):
            self.availability[date] = status

    def calculate_rate(self):
        return self.rate

class SingleRoom(Room):
    def __init__(self, number, rate):
        super().__init__(number, 'Single', rate)

class DoubleRoom(Room):
    def __init__(self, number, rate):
        super().__init__(number, 'Double', rate)

class Suite(Room):
    def __init__(self, number, rate):
        super().__init__(number, 'Suite', rate)

