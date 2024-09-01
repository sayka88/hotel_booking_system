class Reservation:
    reservation_counter = 1

    def __init__(self, guest, room, check_in_date, check_out_date):
        self.reservation_id = Reservation.reservation_counter
        Reservation.reservation_counter += 1
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        num_days = (self.check_out_date - self.check_in_date).days
        return num_days * self.room.rate_per_night

    def modify_reservation(self, new_check_in, new_check_out):
        self.check_in_date = new_check_in
        self.check_out_date = new_check_out
        self.total_cost = self.calculate_total_cost()

    def cancel_reservation(self):
        self.room.update_availability(True)

    def get_reservation_details(self):
        return {
            'reservation_id': self.reservation_id,
            'guest': self.guest.name,
            'room_number': self.room.room_number,
            'check_in_date': self.check_in_date,
            'check_out_date': self.check_out_date,
            'total_cost': self.total_cost
        }

