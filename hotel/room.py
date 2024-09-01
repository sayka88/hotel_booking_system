class Room:
    def __init__(self, room_number, room_type, rate_per_night):
        self.room_number = room_number
        self.room_type = room_type
        self.rate_per_night = rate_per_night
        self.is_available = True

    def check_availability(self):
        return self.is_available

    def update_availability(self, status):
        self.is_available = status

    def get_details(self):
        return {
            'room_number': self.room_number,
            'room_type': self.room_type,
            'rate_per_night': self.rate_per_night,
            'is_available': self.is_available
        }

