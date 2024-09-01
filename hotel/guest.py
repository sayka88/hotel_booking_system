class Guest:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def view_reservations(self):
        return [reservation.get_reservation_details() for reservation in self.reservations]

    def update_details(self, new_name=None, new_contact_info=None):
        if new_name:
            self.name = new_name
        if new_contact_info:
            self.contact_info = new_contact_info

