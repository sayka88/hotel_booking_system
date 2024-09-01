import unittest
from hotel.hotel import Hotel
from hotel.room import SingleRoom
from hotel.guest import Guest

class TestHotel(unittest.TestCase):
    def test_add_room(self):
        hotel = Hotel("Test Hotel", "Test Location")
        room = SingleRoom(101, 100)
        hotel.add_room(room)
        self.assertIn(room, hotel.rooms)

    def test_remove_room(self):
        hotel = Hotel("Test Hotel", "Test Location")
        room = SingleRoom(101, 100)
        hotel.add_room(room)
        hotel.remove_room(room)
        self.assertNotIn(room, hotel.rooms)

    def test_get_available_rooms(self):
        hotel = Hotel("Test Hotel", "Test Location")
        room = SingleRoom(101, 100)
        hotel.add_room(room)
        available_rooms = hotel.get_available_rooms(1, 5)
        self.assertIn(room, available_rooms)

    def test_make_reservation(self):
        hotel = Hotel("Test Hotel", "Test Location")
        room = SingleRoom(101, 100)
        guest = Guest("Test Guest", "test@example.com")
        hotel.add_room(room)
        reservation = hotel.make_reservation(guest, room, 1, 5)
        self.assertIn(reservation, hotel.reservations)

if __name__ == "__main__":
    unittest.main()

