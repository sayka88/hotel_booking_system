class Room:
    def __init__(self, room_number, room_type, rate, availability=True):
        self.room_number = room_number
        self.room_type = room_type
        self.rate = rate
        self.availability = availability

    def check_availability(self):
        return self.availability

    def update_availability(self, status):
        self.availability = status

    def get_room_details(self):
        return f"Room {self.room_number}: {self.room_type}, Rate: {self.rate}, Available: {self.availability}"

# Определение подклассов для разных типов комнат
class SingleRoom(Room):
    def __init__(self, room_number, rate, availability=True):
        super().__init__(room_number, "Single", rate, availability)

class DoubleRoom(Room):
    def __init__(self, room_number, rate, availability=True):
        super().__init__(room_number, "Double", rate, availability)

class Suite(Room):
    def __init__(self, room_number, rate, availability=True):
        super().__init__(room_number, "Suite", rate, availability)

