from hotel.hotel import Hotel
from hotel.room import SingleRoom, DoubleRoom, Suite
from hotel.guest import Guest

def main():
    hotel = Hotel("Grand Hotel", "City Center")
    room1 = SingleRoom(101, 100)
    room2 = DoubleRoom(102, 150)
    room3 = Suite(103, 200)

    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(room3)

    guest = Guest("John Doe", "john.doe@example.com")
    check_in = 1
    check_out = 5

    available_rooms = hotel.get_available_rooms(check_in, check_out)
    if available_rooms:
        room = available_rooms[0]
        reservation = hotel.make_reservation(guest, room, check_in, check_out)
        guest.add_reservation(reservation)
        print(f"Reservation made for {guest.name} in room {room.number} from {check_in} to {check_out}")
    else:
        print("No available rooms for the selected dates.")

    # Modify reservation
    reservation.modify_reservation(2, 6)
    print(f"Reservation modified for {guest.name} in room {room.number} from {reservation.check_in} to {reservation.check_out}")

    # Cancel reservation
    reservation.cancel_reservation()
    print(f"Reservation canceled for {guest.name} in room {room.number}")

    # Update guest details
    guest.update_details("Jane Doe", "jane.doe@example.com")
    print(f"Guest details updated: {guest.name}, {guest.contact_info}")

if __name__ == "__main__":
    main()

