import datetime
from room import Room
from reservation import Reservation
from guest import Guest
from hotel import Hotel

# Создаем номера
room1 = Room(101, 'Single', 100)
room2 = Room(102, 'Double', 150)
room3 = Room(103, 'Suite', 200)

# Создаем отель и добавляем номера
hotel = Hotel("Sunshine Hotel", "New York")
hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

# Создаем гостя и бронируем номер
guest = Guest("John Doe", "johndoe@example.com")
check_in_date = datetime.date(2024, 9, 10)
check_out_date = datetime.date(2024, 9, 15)

reservation = hotel.make_reservation(guest, 101, check_in_date, check_out_date)

# Проверяем информацию о бронировании
print(guest.view_reservations())

