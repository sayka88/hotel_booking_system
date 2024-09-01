import unittest
from datetime import date
from hotel.reservation import Reservation
from hotel.guest import Guest
from hotel.room import SingleRoom

class TestReservation(unittest.TestCase):

    def setUp(self):
        """Создаем начальные данные для тестов"""
        Reservation.reservation_counter = 1  # Сбросить счетчик перед каждым тестом
        self.guest = Guest("John Doe", "john@example.com")
        self.room = SingleRoom(101, 100)
        self.check_in_date = date(2024, 9, 10)
        self.check_out_date = date(2024, 9, 15)
        self.reservation = Reservation(self.guest, self.room, self.check_in_date, self.check_out_date)

    def test_initial_reservation(self):
        """Проверка начального бронирования"""
        self.assertEqual(self.reservation.total_cost, 500)  # 5 ночей * 100 за ночь

    def test_modify_reservation(self):
        """Проверка изменения бронирования"""
        new_check_in_date = date(2024, 9, 12)
        new_check_out_date = date(2024, 9, 17)
        self.reservation.modify_reservation(new_check_in_date, new_check_out_date)
        self.assertEqual(self.reservation.total_cost, 500)  # 5 ночей * 100 за ночь

    def test_cancel_reservation(self):
        """Проверка отмены бронирования"""
        self.reservation.cancel_reservation()
        self.assertTrue(self.room.check_availability())

    def test_get_reservation_details(self):
        """Проверка деталей бронирования"""
        details = self.reservation.get_reservation_details()
        self.assertEqual(details['reservation_id'], 1)
        self.assertEqual(details['guest'], 'John Doe')
        self.assertEqual(details['room_number'], 101)
        self.assertEqual(details['check_in_date'], self.check_in_date)
        self.assertEqual(details['check_out_date'], self.check_out_date)
        self.assertEqual(details['total_cost'], 500)  # 5 ночей * 100 за ночь

if __name__ == "__main__":
    unittest.main()

