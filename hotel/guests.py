class Guest:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def view_reservations(self):
        return self.reservations

    def update_details(self, new_name, new_contact_info):
        self.name = new_name
        self.contact_info = new_contact_info

