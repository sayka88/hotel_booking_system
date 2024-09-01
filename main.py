from datetime import date
from hotel import Hotel, SingleRoom, Guest

def main():
    # Создаем объект отеля
    hotel = Hotel("Grand Hotel", "Downtown")

    # Добавляем комнаты
    room1 = SingleRoom(101, 100)
    room2 = SingleRoom(102, 120)
    hotel.add_room(room1)
    hotel.add_room(room2)

    # Создаем гостя
    guest = Guest("John Doe", "john.doe@example.com")

    # Даты заезда и выезда
    check_in_date = date(2024, 9, 10)
    check_out_date = date(2024, 9, 15)

    # Создаем бронь
    reservation = hotel.make_reservation(guest, 101, check_in_date, check_out_date)

    # Выводим детали брони
    print("Reservation Details:")
    print(reservation.get_reservation_details())

    # Выводим все брони отеля
    print("\nAll Reservations:")
    for reservation in hotel.reservations:
        print(reservation.get_reservation_details())

    # Обновляем доступность комнат
    room1.update_availability(False)  # Комната 101 теперь недоступна

    # Выводим список всех доступных комнат
    print("\nAvailable Rooms:")
    for room in hotel.rooms:
        if room.check_availability():
            print(room.get_room_details())

if __name__ == "__main__":
    main()

