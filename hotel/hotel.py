class Hotel:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.rooms = []
        self.reservations = []

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room_number):
        self.rooms = [room for room in self.rooms if room.room_number != room_number]

    def find_available_rooms(self, room_type, check_in_date, check_out_date):
        available_rooms = []
        for room in self.rooms:
            if room.room_type == room_type and room.check_availability():
                available_rooms.append(room)
        return available_rooms

    def make_reservation(self, guest, room_number, check_in_date, check_out_date):
        room = next((room for room in self.rooms if room.room_number == room_number and room.check_availability()), None)
        if room:
            reservation = Reservation(guest, room, check_in_date, check_out_date)
            room.update_availability(False)
            self.reservations.append(reservation)
            guest.add_reservation(reservation)
            return reservation
        else:
            print(f"Room {room_number} is not available.")
            return None

    def view_all_reservations(self):
        return [reservation.get_reservation_details() for reservation in self.reservations]

