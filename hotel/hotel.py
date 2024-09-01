class Hotel:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room):
        self.rooms.remove(room)

    def get_available_rooms(self, check_in, check_out):
        available_rooms = []
        for room in self.rooms:
            if room.is_available(check_in, check_out):
                available_rooms.append(room)
        return available_rooms

    def make_reservation(self, guest, room, check_in, check_out):
        reservation = Reservation(guest, room, check_in, check_out)
        self.reservations.append(reservation)
        room.update_availability(check_in, check_out, False)
        return reservation

