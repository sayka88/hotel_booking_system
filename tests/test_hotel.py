import unittest
from datetime import date
from hotel.hotel import Hotel
from hotel.room import SingleRoom
from hotel.guest import Guest  # Убедитесь, что этот импорт существует
from hotel.reservation import Reservation

class TestHotelSystem(unittest.TestCase):
    def setUp(self):
        self.hotel = Hotel()
        self.guest = Guest("John Doe")
        self.check_in_date = date(2024, 9, 10)
        self.check_out_date = date(2024, 9, 15)

        # Добавьте комнаты для тестирования
        self.hotel.add_room(SingleRoom(101, 100))
        self.hotel.add_room(SingleRoom(102, 120))

    def test_make_reservation(self):
        reservation = self.hotel.make_reservation(self.guest, 101, self.check_in_date, self.check_out_date)
        self.assertIsNotNone(reservation)
        self.assertEqual(reservation.guest.name, "John Doe")
        self.assertEqual(reservation.room.room_number, 101)
        self.assertEqual(reservation.check_in_date, self.check_in_date)
        self.assertEqual(reservation.check_out_date, self.check_out_date)
        self.assertEqual(reservation.total_cost, 500)  # Пример стоимости

    def test_modify_reservation(self):
        reservation = self.hotel.make_reservation(self.guest, 101, self.check_in_date, self.check_out_date)
        new_check_in = date(2024, 9, 12)
        new_check_out = date(2024, 9, 17)
        reservation.modify_reservation(new_check_in, new_check_out)
        self.assertEqual(reservation.check_in_date, new_check_in)
        self.assertEqual(reservation.check_out_date, new_check_out)
        self.assertEqual(reservation.total_cost, 600)  # Проверьте правильность расчета

    def test_cancel_reservation(self):
        reservation = self.hotel.make_reservation(self.guest, 101, self.check_in_date, self.check_out_date)
        reservation.cancel_reservation()
        room = self.hotel.get_room_by_number(101)
        self.assertTrue(room.check_availability())

    def test_list_available_rooms(self):
        available_rooms = self.hotel.list_available_rooms()
        self.assertGreater(len(available_rooms), 0)  # Убедитесь, что есть доступные комнаты

if __name__ == "__main__":
    unittest.main()

