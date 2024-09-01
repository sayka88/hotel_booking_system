from .room import Room, SingleRoom, DoubleRoom, Suite
from .reservation import Reservation
from .guest import Guest

class Hotel:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def make_reservation(self, guest, room_number, check_in_date, check_out_date):
        room = self.find_room(room_number)
        if room and room.check_availability():
            reservation = Reservation(guest, room, check_in_date, check_out_date)
            self.reservations.append(reservation)
            room.update_availability(False)
            return reservation
        else:
            raise ValueError("Room is not available or does not exist.")

    def find_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

