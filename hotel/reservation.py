class Reservation:
    def __init__(self, guest, room, check_in, check_out):
        self.guest = guest
        self.room = room
        self.check_in = check_in
        self.check_out = check_out
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        duration = self.check_out - self.check_in
        return duration * self.room.rate

    def modify_reservation(self, new_check_in, new_check_out):
        self.room.update_availability(self.check_in, self.check_out, True)
        self.check_in = new_check_in
        self.check_out = new_check_out
        self.room.update_availability(self.check_in, self.check_out, False)
        self.total_cost = self.calculate_total_cost()

    def cancel_reservation(self):
        self.room.update_availability(self.check_in, self.check_out, True)

